def ft_map(function_to_apply, list_of_inputs):
    """
    Apply the function function_to_apply for all the elements eo list_of_inputs
    """
    for item in list_of_inputs:
        yield function_to_apply(item)


def sucessor(x: int) -> int:
    return x + 1


my_list = list(range(9))
print(my_list)
print(list(ft_map(sucessor, my_list)))
