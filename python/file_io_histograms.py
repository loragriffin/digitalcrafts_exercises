# def read_file(x):
#     print(content)

user_file = input("File name: ")

fh = open(user_file, 'r')
content = fh.read()
fh.close()

count = {}

for n in content:
    if n not in count:
        count[n] = 1
    else:
        count[n] += 1

print(count, '\n')

word_list = content.split()
word_lib = {}

for n in word_list:
    if n not in word_lib:
        word_lib[n] = 1
    else:
        word_lib[n] += 1

print(word_lib, '\n')
