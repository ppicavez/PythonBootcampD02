def ft_filter(function_to_apply, list_of_inputs):
    """
    Select only the elements of list_of_inputs where function to apply is True
    """
    return (item for item in list_of_inputs if function_to_apply(item))


def ft_is_odd(num):
    return num % 2


my_list = list(range(12))
print(my_list)
print(list(ft_filter(ft_is_odd, my_list)))
