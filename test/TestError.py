import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import mx_mul


class TestError:
    @pytest.mark.parametrize(
        'error_text, error_code',
        [
            pytest.param('text example 1', None, id='exception with default attributes'),
            pytest.param('text example 2', 2, id='exception with custom error code - 2'),
            pytest.param('text example 3', 22, id='exception with custom error code - 22'),
            pytest.param('text example 4', 222, id='exception with custom error code - 222')
        ]
    )
    def test___init__(self, error_text, error_code):
        try:
            if error_code is None:
                raise mx_mul.Error(error_text)
            else:
                raise mx_mul.Error(error_text, error_code)
        except mx_mul.Error as e:
            if error_code is None:
                assert vars(e) == {'message': error_text, 'error_code': 1}
            else:
                assert vars(e) == {'message': error_text, 'error_code': error_code}
