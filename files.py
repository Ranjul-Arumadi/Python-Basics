try:
    f = open("details.txt", "x")
except FileExistsError:
    print("File is already ready")

#f = open("details.txt", "w")
#f.write("Name \t\t\t ID")



f = open("details.txt", "a")
for i in range(3):
    a = input("Enter name: ")
    b = input("Enter ID: ")
    f.write("\n")
    f.write(a)
    f.write("\t\t\t")
    f.write(b)

f.close()


f = open("details.txt", "r")
for line in f:
    print(line)
f.close()