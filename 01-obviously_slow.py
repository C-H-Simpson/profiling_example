from time import sleep


@profile
def obviously_slow(n_loops=20):
    """ This simple program loops through the integers 0-20 and prints,
        'fizz' if the number is divisible by 3,
        'buzz' if the number is divisible by 5.
        It is made slow by a 'sleep' function.
    """

    for i in range(n_loops):
        # is i divisible by 3?
        if i % 3 == 0:
            print(i, 'fizz')
        if i % 5 == 0:
            # is i divisible by 5?
            print(i, 'buzz')

        # the following line makes the program wait before continuing
        sleep(0.001)


obviously_slow()
