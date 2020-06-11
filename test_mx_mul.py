import mx_mul


def test_main():
    input_values = [
        "2",
        "3",
        "1",
        "2",
        "1 2",
        "5 3",
        "6 7",
        "5",
        "1"
    ]
    output_values = []

    def mock_input(s):
        output_values.append(s)
        return input_values.pop(0)

    def mock_output(*args, **kwargs):
        for arg in args:
            output_values.append(str(arg))

    mx_mul.input = mock_input
    mx_mul.print = mock_output

    mx_mul.main()

    assert output_values == [
        'Matrix A',
        'width: ',
        'height: ',

        'Matrix B',
        'width: ',
        'height: ',

        'Matrix A values:',
        '',
        '',
        '',

        'Matrix B values:',
        '',
        '',

        'Result:',
        '7',
        '28',
        '37'
    ]
