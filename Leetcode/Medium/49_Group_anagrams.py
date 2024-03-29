def group_anagram(strs):
    anagram_map = {}
    for s in strs:
        a = sorted(s)
        s_sorted = "".join(a)
        if s_sorted not in anagram_map:
            anagram_map[s_sorted] = [s]
        else:
            anagram_map[s_sorted].append(s)

    return list(anagram_map.values())


print(group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
