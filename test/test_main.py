import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mx_mul

in_vals_1 = [
    '2',
    '3',

    '1',
    '2',

    '1 2',
    '5 3',
    '6 7',

    '5',
    '1'
]

out_vals_1 = [
    'Matrix A', 'width: ', 'height: ', '\n',
    'Matrix B', 'width: ', 'height: ', '\n',
    'Matrix A values:', '', '', '', '\n',
    'Matrix B values:', '', '', '\n',
    'Result:',
    '7',
    '28',
    '37'
]

in_vals_2 = [
    '5',
    '3',

    '6',
    '5',

    '1 1 2 3 5',
    '1 2 4 6 8',
    '1 3 6 9 12',

    '2 2 2 2 2 2',
    '3 3 3 3 3 3',
    '4 4 4 4 4 4',
    '0 0 0 0 0 0',
    '1 1 1 1 1 1'
]

out_vals_2 = [
    'Matrix A', 'width: ', 'height: ', '\n',
    'Matrix B', 'width: ', 'height: ', '\n',
    'Matrix A values:', '', '', '', '\n',
    'Matrix B values:', '', '', '', '', '', '\n',
    'Result:',
    '18', '18', '18', '18', '18', '18',
    '32', '32', '32', '32', '32', '32',
    '47', '47', '47', '47', '47', '47'
]

in_vals_3 = [
    '6',
    '7',

    '5',
    '6',

    '1 1 2 3 5 8',
    '1 2 3 4 5 6',
    '6 5 4 3 2 1',
    '8 5 3 2 1 1',
    '0 0 0 1 1 1',
    '1 1 1 0 0 0',
    '2 2 2 2 2 2',

    '2 4 6 8 10',
    '10 8 6 4 2',
    '1 2 3 4 5',
    '5 4 3 2 1',
    '1 1 1 0 0',
    '0 0 1 1 1'
]

out_vals_3 = [
    'Matrix A', 'width: ', 'height: ', '\n',
    'Matrix B', 'width: ', 'height: ', '\n',
    'Matrix A values:', '', '', '', '', '', '', '', '\n',
    'Matrix B values:', '', '', '', '', '', '', '\n',
    'Result:',
    '34', '33', '40', '34', '33',
    '50', '47', '50', '42', '39',
    '83', '86', '90', '91', '94',
    '80', '87', '95', '101', '108',
    '6', '5', '5', '3', '2',
    '13', '14', '15', '16', '17',
    '38', '38', '40', '38', '38'
]

# using spaces
in_vals_4 = [
    '   2   ',
    '   2   ',

    '   2   ',
    '   2   ',

    '   2   2   ',
    '   2   2   ',

    '   2   2   ',
    '   2   2   '
]

out_vals_4 = [
    'Matrix A', 'width: ', 'height: ', '\n',
    'Matrix B', 'width: ', 'height: ', '\n',
    'Matrix A values:', '', '', '\n',
    'Matrix B values:', '', '', '\n',
    'Result:',
    '8', '8',
    '8', '8'
]

# using tabulars
in_vals_5 = [
    '	2	',
    '	2	',

    '	2	',
    '	2	',

    '	2	2	',
    '	2	2	',

    '	2	2 	',
    '	2	2 	'
]

out_vals_5 = [
    'Matrix A', 'width: ', 'height: ', '\n',
    'Matrix B', 'width: ', 'height: ', '\n',
    'Matrix A values:', '', '', '\n',
    'Matrix B values:', '', '', '\n',
    'Result:',
    '8', '8',
    '8', '8'
]

in_vals_6 = [
    '2',
    '3',

    '4',
    '5'
]

out_vals_6 = [
    'Matrix A', 'width: ', 'height: ', '\n',
    'Matrix B', 'width: ', 'height: ', '\n',
]


@pytest.mark.parametrize(
    'error_message, input_values, output_values',
    [
        pytest.param(None, in_vals_1, out_vals_1, id='multiply matrices from assignment'),
        pytest.param(None, in_vals_2, out_vals_2, id='multiply simple matrices'),
        pytest.param(None, in_vals_3, out_vals_3, id='multiply advanced matrices'),
        pytest.param(None, in_vals_4, out_vals_4, id='trailing spaces'),
        pytest.param(None, in_vals_5, out_vals_5, id='trailing tabulars'),
        pytest.param('Incorrect matrix size for multiplication.', in_vals_6, out_vals_6, id='multiply incorrect matrices')
    ]
)
def test_main(error_message, input_values, output_values):
    output = []

    # mock for 'input()'
    def mock_input(string):
        output.append(string) # save prompt even it's empty
        return input_values.pop(0)

    # mock for 'print()'
    def mock_output(*args, **kwargs):
        for arg in args:
            output.append(str(arg)) # save printing output

    mx_mul.input = mock_input
    mx_mul.print = mock_output

    try:
        mx_mul.main()
    except mx_mul.Error as e:
        assert e.message == error_message
    finally:
        assert output == output_values
