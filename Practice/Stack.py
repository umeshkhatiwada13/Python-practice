brace_match = {
    ')': '(',
    '}': '{',
    ']': '['
}


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

print(matchingBraces(['{}[]()']))

