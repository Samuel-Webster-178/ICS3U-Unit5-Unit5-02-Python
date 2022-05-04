#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the area of a triangle
#     with inputted radius


def area(height, base):
    # I calculate area

    # process
    area = height * base / 2

    # output
    print("\nThe area of the triangle is {0} cm².".format(area))


def main():
    # I am main, I receive input and call functions

    # input
    str_height = input("Input triangle height in cm: ")
    str_base = input("Input triangle base in cm: ")
    try:
        float_height = float(str_height)
        float_base = float(str_base)
    except Exception:
        print("Invalid input")
    finally:
        area(float_height, float_base)
        print("\nDone.")


if __name__ == "__main__":
    main()
