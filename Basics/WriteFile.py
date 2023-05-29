# writing overrides the data in file present earlier and starts writing from 1st line
# appending adds the text from the line already present in the file
file_to_write = open("WriteFile.txt", "w")
for i in range(1, 2):
    file_to_write.write("\nHello! I am writing text.")
file_to_write.close()
