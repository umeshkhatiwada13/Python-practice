# Q2.
#
# In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.
#
# Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.
#
#     For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
#
# Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.
#
# It is guaranteed an answer exists.
#
#
#
# Example 1:
#
# Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
# Output: [0,2]
#
# Example 2:
#
# Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
# Output: [1,2]
def find_suff_team(req_skills, person, idx=0, current_team=[]):
    if idx == len(person):
        current_skills = set()
        for i in current_team:
            current_skills.update(person[i])

        if set(req_skills) <= set(current_skills):
            return current_team

        return []

    with_person = find_suff_team(req_skills, person, idx + 1, current_team + [idx])
    without_person = find_suff_team(req_skills, person, idx + 1, current_team)

    if with_person and without_person:
        return with_person if len(with_person) < len(without_person) else without_person
    elif with_person:
        return with_person
    else:
        return without_person


# Example 1
req_skills_1 = ["java", "nodejs", "reactjs"]
people_1 = [["java"], ["nodejs"], ["nodejs", "reactjs"]]
print(find_suff_team(req_skills_1, people_1))
# print(team_indices_1)  # Output: [0, 2]

# Example 2
req_skills_2 = ["algorithms", "math", "java", "reactjs", "csharp", "aws"]
people_2 = [["algorithms", "math", "java"], ["algorithms", "math", "reactjs"], ["java", "csharp", "aws"],
            ["reactjs", "csharp"], ["csharp", "math"], ["aws", "java"]]
print(find_suff_team(req_skills_2, people_2))


# print(team_indices_2)  # Output: [1, 2]


# Q3.
#
# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
#
#     Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
#     Each vowel 'a' may only be followed by an 'e'.
#     Each vowel 'e' may only be followed by an 'a' or an 'i'.
#     Each vowel 'i' may not be followed by another 'i'.
#     Each vowel 'o' may only be followed by an 'i' or a 'u'.
#     Each vowel 'u' may only be followed by an 'a'.
#
# Since the answer may be too large, return it modulo 10^9 + 7.

def helper(length, last_vowel):
    if length == 0:
        return 1
    count = 0
    if last_vowel == 'a':
        count += helper(length - 1, 'e')
    elif last_vowel == 'e':
        count += helper(length - 1, 'a') + helper(length - 1, 'i')
    elif last_vowel == 'i':
        count += helper(length - 1, 'a') + helper(length - 1, 'e') + helper(length - 1, 'o') + helper(length - 1, 'u')
    elif last_vowel == 'o':
        count += helper(length - 1, 'i') + helper(length - 1, 'u')
    elif last_vowel == 'u':
        count += helper(length - 1, 'a')
    return count


def count_length(n):
    return sum(helper(n - 1, a) for a in ['a', 'e', 'i', 'o', 'u'])


# Example 1
print(count_length(1))  # Output: 5

# Example 2
print(count_length(2))  # Output: 10

# Example 3
print(count_length(5))  # Output: 68


# Given an integer array nums and an integer k, return the number of good subarrays of nums.
#
# A good array is an array where the number of different integers in that array is exactly k.
#
#     For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
#
# A subarray is a contiguous part of an array.

def count_god_sub_array(nums, k):
    count = 0
    left = 0
    freq_map = {}
    distinct_count = 0
    for right, num in enumerate(nums):
        freq_map[num] = freq_map.get(num, 0) + 1

        if freq_map[num] == 1:
            distinct_count += 1

        while distinct_count > k:
            freq_map[nums[left]] -= 1
            if freq_map[nums[left]] == 0:
                distinct_count -= 1
            left += 1

        if distinct_count == k:
            count += right - left + 1

    return count


print("Count", count_god_sub_array([1, 2, 1, 2, 3], 2))


def count_good_sub_array(nums, k):
    count = 0
    left = 0
    freq_map = {}
    distinct_count = 0
    for right, num in enumerate(nums):
        freq_map[num] = freq_map.get(num, 0) + 1

        if freq_map[num] == 1:
            distinct_count += 1

        while distinct_count > k:
            freq_map[nums[left]] -= 1
            if freq_map[nums[left]] == 0:
                distinct_count -= 1
            left += 1

        if distinct_count == k:
            # Increment count for every valid subarray ending at the current position
            count += right - left + 1

    return count

print(count_good_sub_array([1, 2, 1, 2, 3], 2))  # Output: 7
