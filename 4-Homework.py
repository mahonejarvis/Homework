# 1. Use the DateTime module to get Current Date and Time, and save it to a variable. Then extract just the Full month name form that variable.

import datetime as dt

a = dt.datetime.now()
print("Current Date and Time ...", a)

from datetime import date
today = date.today()
print(today.strftime("%B\n"))

# 2. Write a simple function that takes 2 parameters -- a first name and a day name.
def message(fname, day_name):
    print('Hi', fname, 'Happy', day_name)
    
    #- Set a default value for the day name of Sunday.
    #- Have the function print out a greeting -- using the parameters -- that says something like "Hi first-name! Happy day-name!". Remember to use the variables in the greeting to replace first-name and day-name.  
    #- Invoke this function with 2 variables.
    #- Invoke this function with 1 variable only.
    
def greeting(f_Name, day_name):

    print("Hi", f_Name, "!! Happy", day_name, "!!")
    print('Hi', f_Name)

greeting("Jarvis", "Sunday")
greeting("Jarvis", "")

# 3. Import NumPy, use one of the NumPy methods and create an array with a shape of ... (2, 3, 2). You can use the reshape method -- `.reshape()`

import numpy as np
a1 = np.array(
                            [  
                                [ [0, 1,], [2, 3], [4, 5] ],
                                [ [6, 7], [8,9], [10,11] ]
                                
                            ]
                        )

print("Array shape ...", a1.shape)

# 4. Use NumPy `.linspace()` to create an array with 6 linearly spaced values between 0 and 20

g = np.linspace(0, 20, num=6)
print("Array g ...", g)

# 5. Make a Deep Copy of the above array you created.

import copy

xArray = [ 0., 4.,  8., 12., 16., 20.]
zArray = copy.deepcopy(xArray)

print("The xArray ...\n", xArray)
print("\nThe zArray ...\n", xArray)

# 6. What are 2 reasons we use NumPy arrays over Python Lists.
print('Numpy arrays are faster and use less memory than Python List.')
