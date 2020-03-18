let bowlingScore = frames => {
    let rolls = [...frames]
        .filter(s => s.trim())
        .map((f, i, self) => f === "X" ? 10 : f === "/" ? 10 - parseInt(self[i - 1]) : parseInt(f));

    let score = 0, r = 0;
    let isStrike = () => rolls[r] === 10;
    let isSpare = () => rolls[r] + rolls[r + 1] === 10;

    for (let _ of frames.split(" "))
        if (isStrike()) {
            score += 10 + rolls[r + 1] + rolls[r + 2];
            r++;
        } else if (isSpare()) {
            score += 10 + rolls[r + 2];
            r += 2;
        } else {
            score += rolls[r] + rolls[r + 1];
            r += 2
        }

    return score;
};