from copy import copy


class Mock:

    def __init__(self, input_values, output_values):
        self.input = copy(input_values)
        self.output = output_values

    def mocked_input(self, *args):
        if not args:
            # save missing prompt as an empty string
            self.output.append('')
        else:
            self.output.append(*args)
        return self.input.pop(0)

    def mocked_print(self, *args, **kwargs):
        if not args:
            # save a newline print as one character
            self.output.append('\n')
        else:
            for arg in args:
                self.output.append(str(arg))
