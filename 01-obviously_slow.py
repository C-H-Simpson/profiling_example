"""This is just to demonstrate how the profiler works.
    It should be obvious what is slowing it down!"""

from time import sleep

@profile
def obviously_slow(n_loops=30):
    """ This simple program loops through the integers 0-30 and prints
        'fizz' if the number is divisible by 3, and
        'buzz' if the number is divisible by 5.
        It is made slow by a 'sleep' function.
    """

    output_mapping = (
        (3, 'fizz'),
        (5, 'buzz'),
    )

    for i in range(1, n_loops+1):
        output = ''
        for num, say in output_mapping:
            if i % num == 0:
                output = ''.join((output, say))
        if output == '':
            output = f'{i}'

        print(output)

        # the following line makes the program wait before continuing
        sleep(0.1)


obviously_slow()
