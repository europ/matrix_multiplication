#!/usr/bin/env python3

import sys
import re


class Error(Exception):
    def __init__(self, message, error_code=1):
        self.message = message
        self.error_code = error_code


class Matrix:
    def __init__(self, name):
        self.name = name

        print(f"Matrix {self.name}")

        try:
            self.width = int(input("width: "))
        except ValueError:
            raise Error("Incorrect 'width' value, expecting integer.")

        if self.width < 1:
            raise Error("Incorrect 'width' value, expecting integer from <1, inf) range.")

        try:
            self.height = int(input("height: "))
        except ValueError:
            raise Error("Incorrect 'height' value, expecting integer.")

        if self.height < 1:
            raise Error("Incorrect 'height' value, expecting integer from <1, inf) range.")

        self.values = []

        print() # newline

    def load_values(self):
        print(f"Matrix {self.name} values:")

        field_separator = re.compile(r"\s+")

        for _ in range(self.height):
            row = []
            values = re.split(field_separator, input().strip())

            if len(values) != self.width:
                raise Error("Incorrect matrix row.")

            for value in values:
                try:
                    row.append(float(value))
                except ValueError:
                    raise Error("Incorrect row value(s), expecting integer(s) or floating point value(s).")

            self.values.append(row)

        print() # newline

    # this could be optimized using 'numpy' or by combining sum(), zip() and list comprehension
    def __mul__(self, other):
        result = [[0 for _ in range(other.width)] for _ in range(self.height)]

        for i in range(self.height):
            for j in range(other.width):
                for k in range(self.width):
                    result[i][j] += self.values[i][k] * other.values[k][j]

        return result


def main():
    matrix_A = Matrix("A")
    matrix_B = Matrix("B")

    if matrix_A.width != matrix_B.height:
        raise Error("Incorrect matrix size for multiplication.")

    matrix_A.load_values()
    matrix_B.load_values()

    result = matrix_A * matrix_B

    print("Result:")
    for row in result:
        for val in row:
            # remove trailing zeros from floating numbers
            print('%g' % (val), end=" ")
        print() # newline


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except Error as e:
        print(f"{e.__class__.__name__}. {e.message}")
        sys.exit(e.error_code)
