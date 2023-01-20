# Dahlia's COT4500 Intro Assignment

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
My submission for COP4500 Intro Assignment. 

# How To Run
In the command prompt/terminal, make sure you are in the correct directory, the cot-4500-intro folder. Then write the following commands (depending on whether the pip or python3 command works on your system):
##### Pip Execution
```
  pip install -r requirements.txt
  pip src/main/intro_to_python.py
```
##### Python3 Execution
```
  pip install -r requirements.txt
  python3 src/main/intro_to_python.py
```

The first command will install third-party libraries necessary for the program to run successfully, more specifically numpy. This does so by finding the requirements.txt file and installing the libraries (and their versions).  

The second command compiles and runs the program.

The program will run on its out outputting 3 matrices of the following output:
1. Print a specific 3x3 matrix where a cell is 1 if i == j, else 0
2. Print the 3x3 matrix from #1 and then add 3 to every cell where i ≠j
3. Print the 3x3 matrix from #2 as a 3x2 by deleting the last column from the matrix created


