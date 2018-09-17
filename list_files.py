file_name_input = input("Enter a file name: ")
file_name = file_name_input + ".txt"


list_of_lists = []
fileObject = open(file_name)
for line in fileObject:
    line_of_words = line.split()
    list_of_lists.append(line_of_words)


flat_list = []
for sublist in list_of_lists:
    for item in sublist:
        flat_list.append(item)

flat_list.sort()
print(flat_list)