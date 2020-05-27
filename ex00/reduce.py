def ft_reduce(function_to_apply, list_of_inputs):
    """Iterate for all the list_of value
     Apply the function (2 arguments) and accumulate the result
    """
    my_list = list_of_inputs
    if len(my_list) == 0:
        return None
    while len(my_list) > 1:
        my_list[0] = function_to_apply(my_list[0], my_list.pop(1))
    return my_list[0]


def add_2_numbers(a, b):
    return a + b


my_list = list(range(1, 10))
print(ft_reduce(add_2_numbers, my_list))
