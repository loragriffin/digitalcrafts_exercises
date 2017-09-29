#string exercises

#1 - uppercase a string
intro = "Hello!"
print("UPPERCASE STRING: ", intro.upper())

#2 - capitalize a string
print("Capitalized String: ", intro.capitalize())

#3 - reverse a string
print("Reversed string: ", intro[::-1])

#4 - leetspeak
#dictionary
leetspeak = {'A':4, 'E':3, 'G':6, 'I':1, 'O':0, 'S':5, 'T':7}
arrSentence = []
sentence = input("Input text for translation: ")
sentence = sentence.upper()

for n in sentence:
    if n in leetspeak:
        indx = sentence.index(n)
        arrSentence.append(str(leetspeak[n]))
    else:
        arrSentence.append(n)
sentence2 = ''.join(arrSentence)
print(sentence2)

#5 - long-long vowels
vowels = ['a', 'e', 'i', 'o', 'u']
user = input("Input word: ")
user = user.lower()
word = []

for n in range(len(user)):
    if user[n] in vowels and n + 1 < len(user) and user[n + 1] == user[n]:
        word.append(user[n] * 4)
    else:
        word.append(user[n])
print(''.join(word))

#6 - Caesar Cipher - first try
alpha = {'a':'m', 'b':'n', 'c':'o', 'd':'p', 'e':'q', 'f':'r', 'g':'s', 'h':'t', 'i':'u', 'j':'v',
'k':'w', 'l':'x', 'm':'y', 'n':'z', 'o':'a', 'p':'b', 'q':'c', 'r':'d', 's':'e', 't':'f', 'u':'g',
'v':'h', 'w':'i', 'x':'j', 'y':'k', 'z':'l'}
#caesar = ['mnopqrstuvwxyzabcdefghijkl']
user = input("Enter text to be encrypted: ")
user = user.lower()
encrypted = []

for n in user:
    if n in alpha:
        indx = user.index(n)
        encrypted.append(str(alpha[n]))

print(''.join(encrypted))

#10 - caesar cipher - second try
