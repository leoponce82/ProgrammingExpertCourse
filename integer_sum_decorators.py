def flatten_lists(func):
    def wrapper(*args):
        flatten = []
        print(args)
        for each_item in args:
            if type(each_item) == list:
                for each in each_item:
                    flatten.append(each)
            else:
                flatten.append(each_item)
        print(flatten)
        result = func(*flatten)
        return result

    return wrapper


def convert_strings_to_ints(func):
    def wrapper(*args):
        new_args = []
        print(args)
        for each in args:
            if type(each)==str:
                if each.isdigit():
                    new_args.append(int(each))
            else:
                new_args.append(each)
        print(new_args)
        result = func(*new_args)
        return result

    return wrapper


def filter_integers(func):
    def wrapper(*args):
        new_args = []
        for each in args:
            if type(each) == int:
                new_args.append(each)
        print(new_args)
        result = func(*new_args)
        return result

    return wrapper


@flatten_lists
@convert_strings_to_ints
@filter_integers
def integer_sum(*args):
    # Write your code here.
    return sum(list(args))


args = ["1", "2", -0.9, 4, [5, "hi", "3"]]
result = integer_sum(*args)
print(result)
