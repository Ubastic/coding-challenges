def largest_sum(sentence):
    return max(sum(map(int, ss)) for ss in sentence.split('0'))
