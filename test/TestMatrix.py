import os
import sys
import copy
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mx_mul


class TestMatrix:
    @pytest.mark.parametrize(
        'error_message, matrix_name, input_values, output_values',
        [
            pytest.param(None, 'A', [0, 0], ['Matrix A', 'width: ', 'height: ', '\n'], id='initialize 0 x 0 matrix'),
            pytest.param(None, 'B', [1, 1], ['Matrix B', 'width: ', 'height: ', '\n'], id='initialize 1 x 1 matrix'),
            pytest.param(None, 'C', [2, 2], ['Matrix C', 'width: ', 'height: ', '\n'], id='initialize 2 x 2 matrix'),
            pytest.param(None, 'D', [8, 5], ['Matrix D', 'width: ', 'height: ', '\n'], id='initialize 8 x 5 matrix'),
            pytest.param(None, 'E', [1, 100], ['Matrix E', 'width: ', 'height: ', '\n'], id='initialize 1 x 100 matrix'),
            pytest.param(None, 'F', [100, 1], ['Matrix F', 'width: ', 'height: ', '\n'], id='initialize 100 x 1 matrix'),
            pytest.param(None, 'G', [100, 100], ['Matrix G', 'width: ', 'height: ', '\n'], id='initialize 100 x 100 matrix'),

            pytest.param("Incorrect 'width' value, expecting non-negative integer.",
                         'H', [-1, 1], ['Matrix H', 'width: '], id='initialize -1 x 1 matrix'),

            pytest.param("Incorrect 'height' value, expecting non-negative integer.",
                         'I', [1, -1], ['Matrix I', 'width: ', 'height: '], id='initialize 1 x -1 matrix'),
        ],
    )
    def test___init__(self, error_message, matrix_name, input_values, output_values):
        output = []
        values = copy.copy(input_values)

        # mock for 'input()'
        def mock_input(string):
            output.append(string) # save prompt even it's empty
            return values.pop(0)

        # mock for 'print()'
        def mock_output(*args, **kwargs):
            for arg in args:
                output.append(str(arg)) # save printing output

        mx_mul.input = mock_input
        mx_mul.print = mock_output

        try:
            matrix = mx_mul.Matrix(matrix_name)
        except mx_mul.Error as e:
            assert e.message == error_message
        else:
            assert vars(matrix) == {'name': matrix_name, 'width': input_values[0], 'height': input_values[1], 'values': []}
        finally:
            assert output == output_values

    def test_load_values(self):
        pass

    def test__mul__(self):
        pass