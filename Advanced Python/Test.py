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
