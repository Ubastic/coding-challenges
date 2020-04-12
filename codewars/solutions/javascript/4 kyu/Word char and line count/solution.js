class DocumentParser {
    constructor(reader) {
        this.reader = reader;
        this.reset();
    }

    reset() {
        this.wordCount = 0;
        this.charCount = 0;
        this.lineCount = 0;
    }

    * characters() {
        for (let chunk = this.reader.getChunk(); chunk.length; chunk = this.reader.getChunk())
            yield* chunk;
    }

    parse() {
        let isWord = false;

        for (let c of this.characters()) {
            this.lineCount = this.lineCount || 1;

            if (c === "\n") {
                this.lineCount++;
                this.wordCount += isWord;
                isWord = false;
            } else if (c === " ") {
                this.wordCount += isWord;
                isWord = false;
            } else {
                isWord = true;
            }

            this.charCount += c !== "\n";
        }

        this.wordCount += isWord;
    }
}