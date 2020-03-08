function natToInt(nat) {
    let res = 0;

    for (let node = nat; node !== zero; node = node())
        res++;

    return res;
}

function intToNat(int) {
    return int === 0 ? zero : succ(intToNat(int - 1));
}

function add(nat1, nat2) {
    return nat2 === zero ? nat1 : add(succ(nat1), nat2());
}

function mul(nat1, nat2) {
    return nat2 === zero ? zero : add(nat1, mul(nat1, nat2()));
}

function compareTo(nat1, nat2) {
    return natToInt(nat1) - natToInt(nat2);
}

function toString(nat) {
    return nat === zero ? 'zero' : `succ(${toString(nat())})`;
}