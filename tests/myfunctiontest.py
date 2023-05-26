from reviewpythontha import my_function

def my_function_test():
    import io
    import sys
    capturedOutput = io.StringIO()               # Create StringIO object
    sys.stdout = capturedOutput                  #  and redirect stdout.
    my_function('Oklahoma','hats',13)                                # Call function.
    sys.stdout = sys.__stdout__                  # Reset redirect.
    assert capturedOutput.getvalue() == 'Unequal lengths\nMath is fun: 52\n52\n'
