#file i/o exercises

#1 - read file
# user_file = input("File name to open: ")
#
def read_file(x):
    fh = open(x, 'r')
    content = fh.read()
    fh.close()
    print(content)

# read_file(user_file)

#2
user_file = input("File name to write to: ")
# text = str(input("What do you want to write to this file? "))

def write_file(x):
    with open(x, 'w') as x:
        print((input("First line:")), file = x)
        again = input("Do you want to add another line? (y/n)")
        while again == 'y':
            print((input("Next line:")), file = x)
            again = input("Do you want to add another line? (y/n)")

write_file(user_file)
read_file(user_file)
