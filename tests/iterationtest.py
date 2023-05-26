from reviewpythontha import iteration_math

def iteration_math_test():
    import io
    import sys
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.
    iteration_math()                                # Call function.
    sys.stdout = sys.__stdout__                     # Reset redirect.
    assert capturedOutput.getvalue() == 'Printing the value 2\nPrinting the value 4\nPrinting the value 6\nPrinting the value 10\nPrinting the value 14\nPrinting the value 16\n'