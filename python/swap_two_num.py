import sys


def swap_num_no_var(a, b):
    a = a + b
    b = a - b
    a = a - b
    print(a, b)
# end function


def swap_num_with_var(a, b):
    tmp = a
    a = b
    b = tmp
    print(a, b)
# end function


swap_num_no_var(int(sys.argv[1]), int(sys.argv[2]))
swap_num_with_var(int(sys.argv[1]), int(sys.argv[2]))
