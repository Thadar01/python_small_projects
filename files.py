# r = Read
# a = Append (updateß)
# w= write
# x= create

# Read - error if it doesn't exit

# f = open("name.txt")
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

# for line in f:
#     print(line)

# f.close()  # we should close file after opening the file

# try:
#     f = open("name_lists.txt")
#     print(f.read())
# except:
#     print("The file you want to read doesn't exist")
# finally:
#     f.close()

# Append - creates the file if it doesn't exist
# f = open("name_list.txt", "a")
# f.write("ARMY")
# f.close()

# f = open("name_list.txt", "r")
# print(f.read())
# f.close()

# Overwrite
f = open("name_list.txt", "w")
f.write("Yeah we are not seven wth you")
f.clos()
