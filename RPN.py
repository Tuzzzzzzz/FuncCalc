from math import e, pi, sqrt, sin, cos, tan, asin, acos, atan, log, log2, log10
from collections import deque
import re


brackets_set = {"(", ")"}
op_set = {"+", "-", "*", "/", "^"}
pref_op_set = {"~", "sqrt", "sin", "cos", "tg", "ctg", "ln", "log2", "lg", "arcsin", "arccos", "arctg", "arcctg"}
const_set = {"pi", "e"}


func_dict = {
    "+": lambda a, b: a+b,
    "-": lambda a, b: a-b,
    "*": lambda a, b: a*b,
    "/": lambda a, b: a/b,
    "^": lambda a, b: a**b,
    "~": lambda a: -a,
    "sqrt": sqrt,
    "sin": sin,
    "cos": cos,
    "tg": lambda a: None if (a / (pi/2)) % 2 == 1 else tan(a),
    "ctg": lambda a: None if a % pi == 0 else 1/tan(a),
    "ln": log,
    "log2": log2,
    "lg": log10,
    "arcsin": asin,
    "arccos": acos,
    "arctg": atan,
    "arcctg": lambda a: pi/2 - atan(a)
}


def is_digit(string):
    return not(re.fullmatch(r'-?\d+\.?\d*', string) is None)


def str_to_str_arr(string):
    str_arr = []
    cur_str = ""
    string += " "
    for str in string:
        if str == " ":
            if cur_str != "":
                str_arr.append(cur_str)
                cur_str = ""
        elif str in op_set or str in brackets_set:
            if cur_str != "":
                str_arr.append(cur_str)
                cur_str = ""
            str_arr.append(str)
        else:
            cur_str += str
    return str_arr


def validation(str_arr):
    if len(str_arr) == 0:
        return False
    for el in str_arr:
        if el not in op_set and el not in pref_op_set and el != "x" \
                and el not in const_set and el not in brackets_set and not is_digit(el):
            return False
    return True


def unary_minus(str_arr):
    if str_arr[0] == "-":
        str_arr[0] = "~"
    for i in range(len(str_arr)-1):
        if str_arr[i] == "(" and str_arr[i+1] == "-":
            str_arr[i+1] = "~"


def str_arr_to_rpn_arr(str_arr):

    unary_minus(str_arr)

    rpn_arr = []
    stack = deque()
    priority_dict = {
        "+": 0,
        "-": 0,
        "*": 1,
        "/": 1,
        "^": 2,
        "(": -1,
    }

    fl = True

    for el in str_arr:

        if is_digit(el) or el == "x" or el in const_set:
            rpn_arr.append(el)

        elif el == "(" or el in pref_op_set:
            stack.append(el)

        elif el == ")":
            fl = False
            while len(stack):
                st_el = stack.pop()
                if st_el == "(":
                    fl = True
                    break
                rpn_arr.append(st_el)

        else:
            while len(stack) != 0 and (stack[-1] in pref_op_set or priority_dict[stack[-1]] >= priority_dict[el]):
                rpn_arr.append(stack.pop())

            stack.append(el)

    for i in range(len(stack)):
        st_el = stack.pop()
        if st_el == "(" or is_digit(st_el):
            fl = False
            break
        else:
            rpn_arr.append(st_el)

    if not fl:
        return None
    return rpn_arr


def operation(el, *args):
    return func_dict[el](*args)


def exception(func):
    def new_func(*args):
        try:
            return func(*args)
        except:
            return None
    return new_func

@exception
def rpn_arr_to_result(rpn_arr, x):
    stack = deque()
    for el in rpn_arr:
        if el == "x":
            stack.append(x)

        elif el == "pi":
            stack.append(pi)

        elif el == "e":
            stack.append(e)

        elif is_digit(el) or type(el) == float or type(el) == int:
            stack.append(el)

        elif el in op_set:
            b = float(stack.pop())
            a = float(stack.pop())
            new_el = operation(el, a, b)
            stack.append(new_el)

        elif el in pref_op_set:
            a = float(stack.pop())
            new_el = operation(el, a)
            stack.append(new_el)

    if len(stack) != 1:
        return None
    res = float(stack[0])
    if abs(res) < 1e-9:
        return 0
    return res


def calculate(string, x=None):
    if x is None and "x" in string:
        return None
    str_arr = str_to_str_arr(string)
    if not validation(str_arr):
        return None
    rpn_arr = str_arr_to_rpn_arr(str_arr)
    if rpn_arr is None:
        return None
    return rpn_arr_to_result(rpn_arr, x)


if __name__ == "__main__":
    while True:
        string = input("input string: ")
        if "x" in string:
            x = input("input x: ")
            result = calculate(string, calculate(x))
        else:
            result = calculate(string)
        print(f"result: {result}\n")