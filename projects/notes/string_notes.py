#different types of strings
#text string
print("Hello \n")

#escape
print("Hello \\n")

#raw string - escape backslash not needed
print(r"Hello \n")

#byte string - plain binary data
print(b"Hello \n")
type(b"hello")

#unicode - universal standard
#used for other languages
print(u"Hello")
#prints cat emoji
print(u"\U0001F431")
#utf-8 is general standard for unicode

#converting from byte to unicode
b'Hello'.decode('utf-8')
#converting from unicode to byte
'Hello'.encode('utf-8')

#ascII - pronounced 'ask-ee'

#cesar sipher
#using ROT13 - add 13 to letter's position
letters = 'abcdefghijklmnopqrstuvwxyz'
ord('a') #output: 97 - 97 + 13 = 110
chr(113) # ouput: q
ord('z') #output: 122 - 122+13 = 135
chr(135) #ouput: \x87
string.ascii_letters #output: full alphabet lower, upper
string.ascii_lowercase #output: lowercase alpahbet only
string.ascii_lowercase[13] #ouput: 'n'
