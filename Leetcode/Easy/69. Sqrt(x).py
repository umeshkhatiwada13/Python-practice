def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return int(0)
    if x == 1:
        return 1
    init_number = 2
    while init_number <= x + 1:
        if init_number * init_number == x:
            return init_number
        elif init_number * init_number > x:
            return init_number - 1
        init_number = init_number + 1