
import math

def is_numeric(input_list):
    """
    input parameters:
        input_list:
            a list of values of any type
    output:
        Returns True if all of the elements in input_list
        are numeric, ie integer or float; otherwise
        returns False

    example:
        is_numeric([1, 2.0]) returns True
        is_numeric([2.0, 3, "10"]) returns False
    """
    pass

# tests
assert is_numeric([1, 2.0, -33]) == True
assert is_numeric(["1", 2.0, -33]) == False
assert is_numeric([1, "2.0", -33]) == False
assert is_numeric([1, 2.0, "-33"]) == False



def list_add(listx, listy):
    """
    input parameters:
        listx:
            a list of integers or floats
        listy:
            a list of integers or floats
    output:
        A list that contains the sum of both lists. If
        the input lists have unequal lengths then an
        error msg is printed and nothing is returned.

    example:
        list_add([1,2], [2,3]) returns [3,5]
    """
    pass

# tests
assert list_add([1], [2]) == [3]
assert list_add([1,2,3], [1,1,1]) == [2,3,4]
assert list_add([1], [0,1,1,1]) is None


def list_add_general(listx, listy):
    """
    input parameters:
        listx:
            a list of integers or floats
        listy:
            a list of integers or floats
    output:
        A list that contains the sum of both lists. If
        the input lists have unequal lengths then this
        function returns a list whose length is equal to
        the longer list and the extra elements are equal
        to those of the longer list.

    example:
        list_add_general([1, 2, 10, 20], [2, 3]) returns [3, 5, 10, 20]
    """
    pass

# tests
assert list_add_general([10], [2,3,4]) == [12,3,4]
assert list_add_general([10,2,3], [1,1,1]) == [11,3,4]
assert list_add_general([10,2,3,4], [0,0]) == [10,2,3,4]


def list_operation(listx, listy, op="addition"):
    """
    input parameters:
        listx:
            A list of integers or floats
        listy:
            A list of integers or floats
        op:
            A string that describes the operation.
            Defaults to "addition". Possible values are
            "addition", "subtraction", "multiplication",
            "division", "max", and "min".
    output:
        A list that contains the result of the operation `op`
        of both lists. If the input lists have unequal lengths
        then this function returns a list whose length is equal to
        the longer list and the extra elements are equal
        to those of the longer list. If there is a division by
        zero, that value will be returned as math.nan.

    example:
        list_operation([1, 5, 10], [2, 0]) returns [3, 5, 10]
        list_operation([1, 5, 10], [2, 0], "subtraction") returns [-1, 5, 10]
        list_operation([1, 5, 10], [2, 0], "division") returns [0.5, math.nan, 10]
    """

    pass

assert list_operation([10], [2,3,4]) == [12,3,4]
assert list_operation([10], [2,3,4], "subtraction") == [8,3,4]
assert list_operation([10], [2,3,4], "multiplication") == [20,3,4]
assert list_operation([10], [2,3,4], "max") == [10,3,4]
assert list_operation([10], [2,3,4], "min") == [2,3,4]

test = list_operation([1,1,1], [0.1,-0.1, 0, 0, 0], "division")
assert test[:2]== [10, -10]
assert math.isnan(test[2])
assert test[3:] == [0,0]

