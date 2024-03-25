brace_match = {
    ')': '(',
    '}': '{',
    ']': '['
}


def matching_braces(brace_string):
    stack = []
    for s in brace_string:
        if s in brace_match:
            # check if not empty for checking closing braces
            if stack and stack[-1] == brace_match.get(s):
                stack.pop()
            else:
                return False
        else:
            stack.append(s)
    # return true if stack is empty
    return True if not stack else False


def matchingBraces(braces):
    result_array = []
    # Write your code here
    for brace in braces:
        brace_dict = {}
        for b in brace:
            opening = brace_match.get(b)
            if opening in brace_dict.keys():
                num = brace_dict.get(opening, 0)
                brace_dict[opening] = num - 1
            num = brace_dict.get(b, 0)
            brace_dict[b] = num + 1
        total = 0
        for key, val in brace_dict.items():
            total += val

        val = 'YES' if total == 0 else 'NO'
        result_array.append(val)
        return result_array


def isValid(s):
    pair_map = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    stack = []
    for c in s:
        if c in pair_map:
            if stack and pair_map[c] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return False if stack else True


print(isValid('{}[]()'))
