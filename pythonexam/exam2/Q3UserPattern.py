def user_patternt(rows):
    num = 1
    row = 1

    for i in range(rows, 0, -1):
        for j in range(row):
            # print the number and leave space for the next coming digit
            print(num, end=" ")
            num += 1
        # this print is for line break
        print()

        # Adjust the row length
        if i > rows // 2 + 1:
            row += 1
        else:
            row -= 1


# The input for rows
rows = int(input("Enter the number of rows : "))
user_patternt(rows)
