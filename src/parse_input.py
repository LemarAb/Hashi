# This file is for parsing the input files
import os


def parse_input_field(file_path):
    contents = []  # Initializes contents of the field as a list

    with open(file_path) as t:
        # Gets rid of the of spaces for the x and y value in the input.
        size_info = t.readline().split()
        # X and Y value will always be at 0th and 1st position.
        x_size = int(size_info[0])
        y_size = int(size_info[1])

        print(f"Dimensions are {x_size}, {y_size}\n")
        # add buffer edge around input
        contents = [('.' * (y_size+2))]
        read = t.readlines()
        readLines = ['.' + string[:-1] + '.' + string[-1] for string in read]
        contents.extend(readLines)
        contents.extend([('.' * (y_size+2))])
    return x_size+2, y_size+2, contents
