let ensure = (c) => {if (!c) throw Error()};

class MemoryManager {
    constructor(memory) {
        this.memory = memory;
        this.memoryMapping = new Array(memory.length).fill(false);
        this.memoryMetaData = {};
    }

    allocate(size) {
        let freeBlockSize = 0;
        for (let i = 0; i < this.memoryMapping.length; i++) {
            freeBlockSize = this.memoryMapping[i] ? 0 : freeBlockSize + 1;

            if (freeBlockSize === size) {
                let blockStart = i - size + 1;
                this.memoryMapping.fill(true, blockStart, blockStart + size);
                this.memoryMetaData[blockStart] = size;
                return blockStart;
            }
        }
        ensure(false);
    }

    release(pointer) {
        ensure(this.memoryMetaData[pointer]);
        this.memoryMapping.fill(false, pointer, pointer + this.memoryMetaData[pointer]);
        delete this.memoryMetaData[pointer];
    }

    read(pointer) {
        ensure(this.memoryMapping[pointer]);
        return this.memory[pointer];
    }

    write(pointer, value) {
        ensure(this.memoryMapping[pointer]);
        this.memory[pointer] = value;
    }
}