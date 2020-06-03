# Profiling - why is my python slow?
Sometimes, you find the code you write takes unacceptably long to run, and you don't know why.
*Profiling* means testing what parts of your code are using the most resources.
In this example, I show you how to use [rkern's line profiler](https://github.com/pyutils/line_profiler), which is a library for profiling python scripts.

## Working Example Instructions
Either:
* Run the example on the cloud by clicking on this link 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/C-H-Simpson/profiling_example/master) ( it may take a couple of minutes to start )
* Or, install the example on your own computer by cloning this repository

### Example 01 - how to use the profiler
* Open a terminal, navigate to the folder with the example
* Run the command
	`kernprof -v -l 01-obviously_slow.py`
* `kernprof` is the program that will do the profiling, `-v` means the result will be printed in the terminal instead of to a file, then `-l 01-obviously_slow.py` gives the program the name of the script to be profiled.
* You will see output that looks like this:
```
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19
buzz
fizz
22
23
fizz
buzz
26
fizz
28
29
fizzbuzz
Wrote profile results to 01-obviously_slow.py.lprof
Timer unit: 1e-06 s

Total time: 3.0211 s
File: 01-obviously_slow.py
Function: obviously_slow at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           @profile
     7                                           def obviously_slow(n_loops=30):
     8                                               """ This simple program loops through the integers 0-30 and prints
     9                                                   'fizz' if the number is divisible by 3, and
    10                                                   'buzz' if the number is divisible by 5.
    11                                                   It is made slow by a 'sleep' function.
    12                                               """
    13                                           
    14         1          5.0      5.0      0.0      output_mapping = (
    15                                                   (3, 'fizz'),
    16                                                   (5, 'buzz'),
    17                                               )
    18                                           
    19        31        368.0     11.9      0.0      for i in range(1, n_loops+1):
    20        30         77.0      2.6      0.0          output = ''
    21        90        311.0      3.5      0.0          for num, say in output_mapping:
    22        60        240.0      4.0      0.0              if i % num == 0:
    23        16        136.0      8.5      0.0                  output = ''.join((output, say))
    24        30         95.0      3.2      0.0          if output == '':
    25        16         97.0      6.1      0.0              output = f'{i}'
    26                                           
    27        30        509.0     17.0      0.0          print(output)
    28                                           
    29                                                   # the following line makes the program wait before continuing
    30        30    3019265.0 100642.2     99.9          sleep(0.1)

```
Let's pick apart what some of this means.
* First comes the output of the program, then the result of the profiling.

* We are presented with a table where the time effect of each line is broken down. The first columns shows the line number in the script that we profiled. The last column is the code on that line.
* 'Hits' is the number of times that line was executed. The meaning of the other columns should be obvious.

* What part of the code is the slowest? In this case it is `sleep(0.1)` - it takes 99.9% of the time of the program.

Usually it is not as obvious as this what the slowest part of the code is going to be!

### Example 2 - a more realistic example
* Run the command
	`kernprof -v -l 02-integration.py`
* The script '02-integration.py' does a numerical integration of a function.
* There are multiple implementations, and we will see which is fastest.

## Applying this to your own project
1. You need to install the line profiler. Within the environment for you project, do
  `conda install line_profiler` or `pip install line_profiler` (depending on your environment)
2. Put `@profile` before the function you want to profile as in the above example.
3. Run the script via the `kernprof` command, as in the above example.
4. See what parts of the code are taking the most time - could they be written in a different, faster way? 
5. Ask your colleagues and google search to try and find a better way!

Think about how fast your code needs to run? Is it OK if it takes a few minutes, a few hours... a few days?
