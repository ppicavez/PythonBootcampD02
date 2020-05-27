import time
from random import randint


def log(func):
    def wrapper(*args, **kwargs):
        # Open log file in append mode
        with open('machine.log', 'a+') as f:
            # Format the name of the function that call log
            function_name = " ".join(map(str.capitalize,
                                     func.__name__.split("_")))
            f.write("(ppicavez)Running: {:42}".format(function_name))
            # Calculate execution time of the function
            exec_t = time.time()
            result = func(*args, **kwargs)
            exec_t = time.time() - exec_t
            # Format exec time in ms or s
            if exec_t > 0.001:
                f.write("[ exec-time = %.3f s  ]\n" % exec_t)
            else:
                f.write("[ exec-time = %.3f ms ]\n" % (exec_t*1000))
        # return the normal result of the function
        return result
    return wrapper


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
