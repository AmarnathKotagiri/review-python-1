from reviewpythontha import my_lambda

def my_lambda_test():
    import io
    import sys
    capturedOutput = io.StringIO()               # Create StringIO object
    sys.stdout = capturedOutput                  #  and redirect stdout.
    my_lambda('Oklahoma','hats',13)                                # Call function.
    sys.stdout = sys.__stdout__                  # Reset redirect.
    assert capturedOutput.getvalue() == '-1\n'
