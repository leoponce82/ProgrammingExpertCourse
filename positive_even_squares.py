def positive_even_squares(*args):
    # Write your code here.
    print(args)
    all_nums = []
    for each_list in args:
        for each in each_list:
            all_nums.append(each)

    result = list(
        map(lambda x: x**2, (filter(lambda x: (x % 2 == 0) and (x > 0), all_nums)))
    )
    return result


args =[ [-5, 2, 3, 4, 5], [1, 3, 5, 6, 7], [-9, -8, 10] ]
result = positive_even_squares(*args)
print(result)
