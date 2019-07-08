let generator = (sequencer, ...args) => {
    let iter = sequencer(...args);
    return {next: () => iter()}
};

let dummySeq = () => () => "dummy";


let factorialSeq = () => {
    let [start, accum] = [0, 1];
    return () => {
        if (start === 0) {
            start++;
            return accum;
        }
        accum *= start;
        start++;
        return accum;
    }
};

let fibonacciSeq = () => {
    let [prev, curr] = [0, 1];
    return () => {
        let v = curr;
        [prev, curr] = [curr, prev + curr];
        return v;
    }
};

let rangeSeq = (start, step) => () => {
    let v = start;
    start += step;
    return v;
};


const isPrime = num => {
    for (let i = 2; i < num; i++)
        if (num % i === 0) return false;
    return num > 1;
};

let primeSeq = () => {
    let i = 0;
    return () => {
        while (!isPrime(i)) {
            i++;
        }
        return i++;
    }
};

let partialSumSeq = (...args) => {
    let [i, s] = [0, 0];
    return () => {
        if (i >= args.length) {
            throw Error();
        }
        s += args[i++];
        return s;
    }
};