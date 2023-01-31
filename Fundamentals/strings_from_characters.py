def create_strings_from_characters(frequencies, string1, string2):
    # Write your code here.
    local_freq1 = dict(frequencies)
    local_freq2 = dict(frequencies)
    res1=0
    res2=0
    for each in string1:
        if each in local_freq1:
            if local_freq1[each] > 0:
                local_freq1[each] = local_freq1[each] - 1
                print(local_freq1)
                res1 += 1
            else:
                res1=0
                local_freq1 = dict(frequencies)
                break
    if res1 == len(string1):
        res1=1
    print(res1)
    for each in string2:
        if each in local_freq1:
            if local_freq1[each] > 0:
                local_freq1[each] = local_freq1[each] - 1
                print(local_freq1)
                res2 += 1
            else:
                res2=0
                break
    if res2 == len(string2):
        res2=1
    print(res2)
    res = res1+res2
    return res
