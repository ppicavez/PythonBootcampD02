class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


def what_are_the_vars(*args, **kwargs):
    # Create an instance of the object with class ObjectC
    obj = ObjectC()
    # use datas in tutple *args to create new members var_i
    # instanciate them with value of the tuple
    for i in range(len(args)):
        setattr(obj, f"var_{i}", args[i])
    # use datas in dict *args to create new members named with key and
    # instanciated with value
    for key, value in kwargs.items():
        # Verify if the instance has already a member named with key
        if hasattr(obj, key):
            return None
        setattr(obj, key, value)
    return obj


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
