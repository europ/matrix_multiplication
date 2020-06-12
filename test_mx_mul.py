import mx_mul
import pytest

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


@pytest.mark.parametrize(
    'input_values, output_values',
    [
        pytest.param(in_vals_1, out_vals_1, id='example 1'), # from PDF
        pytest.param(in_vals_2, out_vals_2, id='example 2'),
        pytest.param(in_vals_3, out_vals_3, id='example 3'),
    ],
)
def test_main(input_values, output_values):
    output = []

    def mock_input(string):
        output.append(string)
        return input_values.pop(0)

    def mock_output(*args, **kwargs):
        for arg in args:
            output.append(str(arg))

    mx_mul.input = mock_input
    mx_mul.print = mock_output

    mx_mul.main()

    assert output == output_values
