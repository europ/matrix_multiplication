import os
import sys
import pytest

from utils import Mock

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
    '7', '\n',
    '28', '\n',
    '37', '\n'
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
    '18', '18', '18', '18', '18', '18', '\n',
    '32', '32', '32', '32', '32', '32', '\n',
    '47', '47', '47', '47', '47', '47', '\n'
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
    '34', '33', '40', '34', '33', '\n',
    '50', '47', '50', '42', '39', '\n',
    '83', '86', '90', '91', '94', '\n',
    '80', '87', '95', '101', '108', '\n',
    '6', '5', '5', '3', '2', '\n',
    '13', '14', '15', '16', '17', '\n',
    '38', '38', '40', '38', '38', '\n'
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
    '8', '8', '\n',
    '8', '8', '\n'
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
    '8', '8', '\n',
    '8', '8', '\n'
]

in_vals_6 = [
    '2',
    '2',

    '2',
    '2',

    '1.2 2.4',
    '3.6 4.8',

    '5.2 6.4',
    '7.6 8.8'
]

out_vals_6 = [
    'Matrix A', 'width: ', 'height: ', '\n',
    'Matrix B', 'width: ', 'height: ', '\n',
    'Matrix A values:', '', '', '\n',
    'Matrix B values:', '', '', '\n',
    'Result:',
    '24.48', '28.8', '\n',
    '55.2', '65.28', '\n'
]

in_vals_7 = [
    '2',
    '3',

    '4',
    '5'
]

out_vals_7 = [
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
        pytest.param(None, in_vals_6, out_vals_6, id='multiply matrices including real number'),

        pytest.param('Incorrect matrix size for multiplication.',
                     in_vals_7, out_vals_7, id='multiply incorrect matrices')
    ]
)
def test_main(error_message, input_values, output_values):
    mock = Mock(input_values, [])

    mx_mul.input = mock.mocked_input
    mx_mul.print = mock.mocked_print

    try:
        mx_mul.main()
    except mx_mul.Error as e:
        assert e.message == error_message
    finally:
        assert mock.output == output_values
