def solution(args):
    start, stop, result = None, None, []
    for val in args + [None]:
        if start is None:
            start, stop = val, val
        elif val is None or val - stop != 1:
            if stop - start > 1:
                result.append('{}-{}'.format(start, stop))
            else:
                result.append(','.join(map(str, range(start, stop + 1))))
            start = stop = val
        else:
            stop = val

    return ','.join(result)