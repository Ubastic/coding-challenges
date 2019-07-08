def next_version(version):
    nums = version.split('.')
    for i, n in reversed([*enumerate(nums)]):
        nn = int(n) + 1

        if nn < 10:
            nums[i] = nn
            break
        elif i:
            nums[i] = 0
        else:
            nums[i] = nn

    return '.'.join(map(str, nums))
