#dictionary exercises - letter summary

word = input("What would you like a lettery summary of? ")

count = {}

for n in word:
    if n not in count:
        count[n] = 1
    else:
        count[n] += 1

print(count)

#word summary
para = input("Word Histogram: ")

word_list = para.split()
word_lib = {}

for n in word_list:
    if n not in word_lib:
        word_lib[n] = 1
    else:
        word_lib[n] += 1

print(word_lib)
