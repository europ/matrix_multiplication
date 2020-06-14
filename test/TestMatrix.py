import os
import sys
import pytest

from utils import Mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mx_mul


class TestMatrix:
    @pytest.mark.parametrize(
        'error_message, matrix_name, input_values, output_values',
        [
            pytest.param(None, 'A', [1, 1], ['Matrix A', 'width: ', 'height: ', '\n'], id='initialize 1 x 1 matrix'),
            pytest.param(None, 'A', [2, 2], ['Matrix A', 'width: ', 'height: ', '\n'], id='initialize 2 x 2 matrix'),
            pytest.param(None, 'A', [8, 5], ['Matrix A', 'width: ', 'height: ', '\n'], id='initialize 8 x 5 matrix'),
            pytest.param(None, 'A', [1, 100], ['Matrix A', 'width: ', 'height: ', '\n'], id='initialize 1 x 100 matrix'),
            pytest.param(None, 'A', [100, 1], ['Matrix A', 'width: ', 'height: ', '\n'], id='initialize 100 x 1 matrix'),
            pytest.param(None, 'A', [100, 100], ['Matrix A', 'width: ', 'height: ', '\n'], id='initialize 100 x 100 matrix'),

            pytest.param("Incorrect 'width' value, expecting integer from <1, inf) range.",
                         'A', [0, 0], ['Matrix A', 'width: '], id='initialize 0 x 0 matrix'),

            pytest.param("Incorrect 'width' value, expecting integer from <1, inf) range.",
                         'A', [0, 1], ['Matrix A', 'width: '], id='initialize 0 x 1 matrix'),

            pytest.param("Incorrect 'height' value, expecting integer from <1, inf) range.",
                         'A', [1, 0], ['Matrix A', 'width: ', 'height: '], id='initialize 1 x 0 matrix'),

            pytest.param("Incorrect 'width' value, expecting integer from <1, inf) range.",
                         'A', [-1, 1], ['Matrix A', 'width: '], id='initialize -1 x 1 matrix'),

            pytest.param("Incorrect 'height' value, expecting integer from <1, inf) range.",
                         'A', [1, -1], ['Matrix A', 'width: ', 'height: '], id='initialize 1 x -1 matrix'),

            pytest.param("Incorrect 'width' value, expecting integer.",
                         'A', ['foo', 1], ['Matrix A', 'width: '], id='initialize "foo" x 1 matrix'),

            pytest.param("Incorrect 'height' value, expecting integer.",
                         'A', [1, 'foo'], ['Matrix A', 'width: ', 'height: '], id='initialize 1 x "foo" matrix')
        ]
    )
    def test___init__(self, error_message, matrix_name, input_values, output_values):
        mock = Mock(input_values, [])

        mx_mul.input = mock.mocked_input
        mx_mul.print = mock.mocked_print

        try:
            matrix = mx_mul.Matrix(matrix_name)
        except mx_mul.Error as e:
            assert e.message == error_message
        else:
            assert vars(matrix) == {'name': matrix_name, 'width': int(input_values[0]), 'height': int(input_values[1]), 'values': []}
        finally:
            assert mock.output == output_values

    @pytest.mark.parametrize(
        'error_message, matrix_name, input_values, output_values',
        [
            pytest.param(
                None,
                'A',
                ['2', '3', '1 2', '5 3', '6 7'],
                ['Matrix A', 'width: ', 'height: ', '\n',
                 'Matrix A values:', '', '', '', '\n'],
                id='matrix successfully loads the given values'
            ),
            pytest.param(
                None,
                'A',
                ['2', '3', '1 2', '5.7 3.7', '6.7 7.7'],
                ['Matrix A', 'width: ', 'height: ', '\n',
                 'Matrix A values:', '', '', '', '\n'],
                id='matrix successfully loads the given values (floating point numbers)'
            ),
            pytest.param(
                'Incorrect matrix row.',
                'A',
                ['5', '5', '1 1 1 1 1', '1 2'],
                ['Matrix A', 'width: ', 'height: ', '\n',
                 'Matrix A values:', '', ''],
                id='matrix fails on given values - incorrect count of values in row'
            ),
            pytest.param(
                'Incorrect row value(s), expecting integer(s) or floating point value(s).',
                'A',
                ['2', '2', '1 1', '1 a'],
                ['Matrix A', 'width: ', 'height: ', '\n',
                 'Matrix A values:', '', ''],
                id='matrix fails on given values - incorrect value in row'
            )
        ]
    )
    def test_load_values(self, error_message, matrix_name, input_values, output_values):
        mock = Mock(input_values, [])

        mx_mul.input = mock.mocked_input
        mx_mul.print = mock.mocked_print

        matrix = mx_mul.Matrix(matrix_name)

        try:
            matrix.load_values()
        except mx_mul.Error as e:
            assert vars(e) == {'message': error_message, 'error_code': 1}
        else:
            attributes = vars(matrix)

            assert attributes['name'] == matrix_name
            assert attributes['width'] == int(input_values[0])
            assert attributes['height'] == int(input_values[1])
            for i in range(len(attributes['values'])):
                assert attributes['values'][i] == [float(item) for item in input_values[2:][i].split()]

        finally:
            assert mock.output == output_values

    @pytest.mark.parametrize(
        'matrix_name, input_values, output_values, result_values',
        [
            pytest.param(
                'A',
                ['5', '5', '0 0 0 0 0', '0 0 0 0 0', '0 0 0 0 0', '0 0 0 0 0', '0 0 0 0 0'],
                ['Matrix A', 'width: ', 'height: ', '\n',
                 'Matrix A values:', '', '', '', '', '', '\n'],
                [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
                id='matrices multiplication - only zeros'
            ),
            pytest.param(
                'A',
                ['5', '5', '0 0 0 0 0', '0 0 0 0 0', '0 0 2 0 0', '0 0 0 0 0', '0 0 0 0 0'],
                ['Matrix A', 'width: ', 'height: ', '\n',
                 'Matrix A values:', '', '', '', '', '', '\n'],
                [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 4, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
                id='matrices multiplication - middle value and zeros'
            ),
            pytest.param(
                'A',
                ['5', '5', '1 1 1 1 1', '1 1 1 1 1', '1 1 1 1 1', '1 1 1 1 1', '1 1 1 1 1'],
                ['Matrix A', 'width: ', 'height: ', '\n',
                 'Matrix A values:', '', '', '', '', '', '\n'],
                [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
                id='matrices multiplication - "1 1 1 1 1" rows in both matrices'
            ),
            pytest.param(
                'A',
                ['5', '5', '1 2 3 4 5', '1 1 1 1 1', '1 1 1 1 1', '1 1 1 1 1', '1 1 1 1 1'],
                ['Matrix A', 'width: ', 'height: ', '\n',
                 'Matrix A values:', '', '', '', '', '', '\n'],
                [[15, 16, 17, 18, 19], [5, 6, 7, 8, 9], [5, 6, 7, 8, 9], [5, 6, 7, 8, 9], [5, 6, 7, 8, 9]],
                id='matrices multiplication - "1 1 1 1 1" rows in both matrices except the first row'
            ),
            pytest.param(
                'A',
                ['5', '5', '1 2 3 4 5', '1 2 3 4 5', '1 2 3 4 5', '1 2 3 4 5', '1 2 3 4 5'],
                ['Matrix A', 'width: ', 'height: ', '\n',
                 'Matrix A values:', '', '', '', '', '', '\n'],
                [[15, 30, 45, 60, 75], [15, 30, 45, 60, 75], [15, 30, 45, 60, 75], [15, 30, 45, 60, 75], [15, 30, 45, 60, 75]],
                id='matrices multiplication - "1 2 3 4 5" rows in both matrices'
            ),
            pytest.param(
                'A',
                ['5', '5', '1.2 2.4 3.6 4.8 5.2', '1.2 2.4 3.6 4.8 5.2',
                 '1.2 2.4 3.6 4.8 5.2', '1.2 2.4 3.6 4.8 5.2', '1.2 2.4 3.6 4.8 5.2'],
                ['Matrix A', 'width: ', 'height: ', '\n',
                 'Matrix A values:', '', '', '', '', '', '\n'],
                [[20.64, 41.28, 61.92, 82.56, 89.44], [20.64, 41.28, 61.92, 82.56, 89.44], [20.64, 41.28, 61.92, 82.56, 89.44],
                 [20.64, 41.28, 61.92, 82.56, 89.44], [20.64, 41.28, 61.92, 82.56, 89.44]],
                id='matrices multiplication - "1.2 2.4 3.6 4.8 5.2" rows in both matrices (floating point numbers)'
            )
        ]
    )
    def test___mul__(self, matrix_name, input_values, output_values, result_values):
        mock = Mock(input_values, [])

        mx_mul.input = mock.mocked_input
        mx_mul.print = mock.mocked_print

        matrix = mx_mul.Matrix(matrix_name)
        matrix.load_values()

        result = matrix * matrix

        assert result == result_values
        assert mock.output == output_values
