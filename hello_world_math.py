# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy


def print_hi(name: str) -> str:
    # Use a breakpoint in the code line below to debug your script.
    return str('hi ') + name  # Press Ctrl+F8 to toggle the breakpoint.

def use_numpy_dependency(number: float)->float:
    return numpy.sqrt(number)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(print_hi('PyCharm'))
    print(use_numpy_dependency(4.))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
