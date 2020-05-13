# Profiling - why is my python slow?
Sometimes, you find the code you write takes unacceptably long to run, and you don't know why.
*Profiling* means testing what parts of your code are using the most resources.
In this example, I show you how to use [rkern's line profiler](https://github.com/pyutils/line_profiler), which is a library for profiling python scripts.

## Working Example Instructions
Either:
* Run the example on the cloud by clicking on this link 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/C-H-Simpson/profiling_example/master) ( it may take a couple of minutes to start )
* Or, install the example on your own computer by cloning this repository

Then:
* Open a terminal, navigate to the folder with the example
* Run the command
	`kernprof -v -l 01-obviously_slow.py`
 `kernprof` is the program that will do the profiling, `-v` means the result will be printed in the terminal instead of to a file, then `-l 01-obviously_slow.py` gives the program the name of the script to be profiled.
* You will see output that looks like this:
```
0 fizz
0 buzz
3 fizz
5 buzz
6 fizz
9 fizz
10 buzz
12 fizz
15 fizz
15 buzz
18 fizz
Wrote profile results to 01-obviously_slow.py.lprof
Timer unit: 1e-06 s

Total time: 0.039268 s
File: 01-obviously_slow.py
Function: obviously_slow at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           @profile
     5                                           def obviously_slow(n_loops=20):
     6                                               """ This simple program loops through the integers 0-20 and prints,
     7                                                   'fizz' if the number is divisible by 3,
     8                                                   'buzz' if the number is divisible by 5.
     9                                                   It is made slow by a 'sleep' function.
    10                                               """
    11                                           
    12        21        110.0      5.2      0.3      for i in range(n_loops):
    13                                                   # is i divisible by 3?
    14        20         44.0      2.2      0.1          if i % 3 == 0:
    15         7         69.0      9.9      0.2              print(i, 'fizz')
    16        20         11.0      0.6      0.0          if i % 5 == 0:
    17                                                       # is i divisible by 5?
    18         4         23.0      5.8      0.1              print(i, 'buzz')
    19                                           
    20                                                   # the following line makes the program wait before continuing
    21        20      39011.0   1950.5     99.3          sleep(0.001)
```

Let's pick apart what some of this means.
First comes the output of the program, then the result of the profiling.

We are presented with a table where the time effect of each line is broken down. The first columns shows the line number in the script that we profiled. The last column is the code on that line.
'Hits' is the number of times that line was executed. The meaning of the other columns should be obvious.

What part of the code is the slowest? In this case it is `sleep(0.001)` - it takes 99.3% of the time of the program.


Usually it is not as obvious as this what the slowest part of the code is going to be!

## Applying this to your own project
1. You need to install the line profiler. Within the environment for you project, do
 `pip install line_profiler`
2. Put `@profile` before the function you want to profile
3. Run the script via the `kernprof` command, as above
4. See what parts of the code are taking the most time - could they be written in a different, faster way? 
5. Ask your colleagues and google search to try and find a better way!
