def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """

    def get_re(a, b, c):
        if a == '1' & b == '1':
            return '1', '0'
        elif a == '0' & b == '0':
            return '0', '0'
        else:
            return '0', '1'

    index = 0
    a_len = len(a)
    b_len = len(b)
    index = 0
    final = 0
    a = a[::-1]
    b = b[::-1]
    if a_len > b_len:
        for c in a:
            a, b = get_re(c, b[index])
            final += b
