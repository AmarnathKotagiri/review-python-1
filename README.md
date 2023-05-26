[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8363246&assignment_repo_type=AssignmentRepo)
# Review Python THA
In this assignment you will practice using a `while` loop. You will also practice writing functions.

To submit, please perform the following:
1. Perform your work in the Python file [reviewpythontha.py](reviewpythontha.py).
1. Provide solutions for the following tasks:
   1. Iteration and Math with While (3 pts.)
   1. Functions and Parameters (5 pts.)
   1. Lambda Function (2 pts.)
1. Push your assignment to GitHub.

### Iteration and Math with While
Create a `while` loop that prints the value for even numbers only. Include the following text in the print: "Printing the value `i`." where `i` is the value printed. Your list must include the following values: 1, 2, 4, 5, 6, 7, 9, 10, 13, 14, 15, 16.

### Functions and Parameters
The following tasks will create a function with output. Perform the following tasks.
* Using the function `my_function` provide it with three parameters
  * `str1` a string passed into `my_function()`
  * `str2` another string passed into `my_function()`
  * `int1` an integer passed into `my_function()`
* Use an if-else statement to evaluate if the two strings have unequal lengths; if they do, print 'Unequal lengths', otherwise print 'Equal lengths'
* Still inside the function, perform a math operation using the length of `str2` with `int1`; set this equal to `math1`
* Print out `Math is fun: <outcome>` where `<outcome>` is the result of your math operation.
* At the end of the function, return the value for `math1`

Use your function by passing in some values:
  * For the first string, pass in `Oklahoma`
  * For the second string, pass in `hats`
  * For the integer, pass in the value `13`

### Lambda Function
Use the function `my_lambda` to complete this section. 
* Inside `my_lambda` create a simple lambda function that uses the same variables (your two strings and the integer) as the function `my_function` 
* Call the lambda function `t`.
* The expression will sum the string lengths together and subtract the integer
* Print out the result
