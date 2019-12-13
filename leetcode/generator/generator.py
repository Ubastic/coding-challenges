import re
from pathlib import Path
from typing import (
    List,
    NamedTuple,
    Sequence,
)
from urllib.parse import quote

import click
from bs4 import BeautifulSoup
from requests import (
    Response,
    Session,
)

CODE_REGEX = re.compile(r'submissionCode\s*:\s*\'([\s\S]*)\'\s*,\s*editCodeUrl', re.MULTILINE)
UNICODE_ESCAPE_REGEX = re.compile(r'\\u[0-9A-Z]{4}')

BASE_URL = 'https://leetcode.com'
BASE_DIR: Path = Path(__file__).parent.parent
SOLUTIONS_DIR: Path = BASE_DIR / 'solutions'

DIFFICULTY_LEVEL = (
    None,
    'easy',
    'medium',
    'hard',
)

LANGUAGE_FILE_EXTENSION = {
    'python': 'py',
    'python3': 'py',
    'kotlin': 'kt',
    'c': 'c',
    'c++': 'cpp',
    'javascript': 'js',
    'java': 'java',
    'haskell': 'hs',
}
LONGEST_LANGUAGE = max(map(len, LANGUAGE_FILE_EXTENSION)) + 1


class Submission(NamedTuple):
    id: str
    statusDisplay: str
    lang: str
    url: str


class Question(NamedTuple):
    id: int
    slug: str
    title: str
    difficulty: str


def create_link(name: str, url: str, wrap: bool = True) -> str:
    return f'[{name}]({quote(url) if wrap else url})'


def from_response(r: Response) -> BeautifulSoup:
    """
    Convert Response text to BeautifulSoup instance using html.parser feature
    """
    return BeautifulSoup(r.text, features="html.parser")


def get_submissions(s: Session, question: str) -> Sequence[Submission]:
    r = s.get(
        f'{BASE_URL}/graphql/',
        json={
            "operationName": "Submissions",
            "variables": {
                "offset": 0,
                "limit": -1,
                "lastKey": None,
                "questionSlug": question,
            },
            "query": """
            query Submissions($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!) {
                submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {
                    lastKey
                    hasNext
                    submissions {
                        id\nstatusDisplay\nlang\nruntime\ntimestamp\nurl\nisPending\nmemory\n__typename
                    }
                    __typename
                }
            }
            """
        },
    )
    r.raise_for_status()
    data = r.json()
    submissions = data['data']['submissionList']['submissions']

    return [
        Submission(**{k: s[k] for k in Submission._fields})
        for s in submissions
    ]


def get_submission_code(s: Session, submission: Submission):
    r = s.get(f'{BASE_URL}/submissions/detail/{submission.id}/')
    r.raise_for_status()

    return UNICODE_ESCAPE_REGEX.sub(
        lambda m: chr(int(m.group()[2:], 16)),
        CODE_REGEX.search(r.text).group(1),
    )


def get_questions(s: Session) -> Sequence[Question]:
    r = s.get(
        f'{BASE_URL}/api/problems/all/',
        params={'status': 'Solved'},
    )
    r.raise_for_status()
    data = r.json()

    return [
        Question(
            id=q['stat']['question_id'],
            slug=q['stat']['question__title_slug'],
            title=q['stat']['question__title'],
            difficulty=DIFFICULTY_LEVEL[q['difficulty']['level']],
        )
        for q in data['stat_status_pairs']
        if q['status'] == 'ac'
    ]


def write_question_submission(s: Session, question: Question) -> None:
    submission_dir = SOLUTIONS_DIR / question.difficulty / question.slug
    submission_dir.mkdir(exist_ok=True)

    submission, *_ = get_submissions(s, question.slug)
    code = get_submission_code(s, submission)

    print(f'Write solution for "{question.title}"')

    submission_file = submission_dir / f'solution.{LANGUAGE_FILE_EXTENSION[submission.lang]}'
    submission_file.write_text(code, 'utf-8')


@click.command()
@click.option(
    '-s',
    '--session-id',
    type=str,
)
def main(session_id) -> None:
    with Session() as s:
        s.cookies['LEETCODE_SESSION'] = session_id
        SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)

        questions = get_questions(s)
        difficulties = {q.difficulty for q in questions}

        for difficulty in difficulties:
            (SOLUTIONS_DIR / difficulty).mkdir(exist_ok=True)

        questions_info: List[str] = []
        for question in sorted(
                questions,
                key=lambda q: DIFFICULTY_LEVEL.index(q.difficulty),
                reverse=True,
        ):
            write_question_submission(s, question)
            link = create_link("solution", f"/leetcode/solutions/{question.difficulty}/{question.slug}/")

            questions_info.append(
                f'| {question.title} '
                f'| {question.difficulty.title()} '
                f'| {link} '
                f'|'
            )

        template = (BASE_DIR / 'README_template.md').read_text('utf-8')
        (BASE_DIR / 'README.md').write_text(
            template.format(solutions='\n'.join(questions_info))
        )


if __name__ == '__main__':
    main()
