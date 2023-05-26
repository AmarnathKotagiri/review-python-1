#### Iteration and Math with While
from operator import le

def iteration_math():
    num_list = [1, 2, 4, 5, 6, 7, 9, 10, 13, 14, 15, 16]
    # while loop goes here
    i = 0
    while i < len(num_list) :
        if num_list[i] % 2 == 0 :
            print("Printing the value", num_list[i])
        i+=1

iteration_math()

#### Functions and Parameters
def my_function(str1,str2,int1):
    # if-else statement here
    if len(str1) != len(str2) :
        print("Unequal lengths")
    else :
        print("Equal lengths")
    # math equation here
    math1 = len(str2) * int1
    # print statement here
    print("Math is fun:", math1)
    # return the variable math1
    return math1

numero = 13
string1 = 'Oklahoma'
string2 = 'hats'

my_function(string1,string2,numero)

#### Lambda Function
def my_lambda(str1,str2,num):
    # lambda function here
    t = lambda str1, str2, num : len(str1)+len(str2)-num
    # print statement here
    print(t(str1, str2, num))

my_lambda(string1,string2,numero)