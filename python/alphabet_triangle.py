def show_triangle(height=3):
    total_space = 2*height - 1
    x_count = height - 1
    for h_index in range(1, height + 1):
        for x in range(0, x_count):
            print(" ", sep="", end="")
        # end for
        for x in range(1, h_index + 1):
            print(chr(64+x), sep="", end="")
        # end for
        for x in range(h_index-1, 0, -1):
            print(chr(64+x), sep="", end="")
        # end for
        for x in range(0, x_count):
            print(" ", sep="", end="")
        # end for
        x_count -= 1
        print()
# end function


show_triangle(5)
