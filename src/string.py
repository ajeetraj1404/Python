# Concept to understand the string
s = "Hello, Ajeet" # This is a string
print("Yo," + s)
#We can also use combination of single quote and double quote for strings
s1 = 'Hi, "how you doing"'
print(s1)
#Now multiple line string as input
s2 = '''Hi how
is your mother,
take care''' # Triple quotes helps in multiple line string if not used gives as null not found EOL:End of line
print(s2)

# String indexing
# String is a sequence of characters starts with index 0
print(s2[0]) # index 0 value in string s2
print(s2[1])
# Index error, no character present at given index
#print(s[20])

# Print all character in string one by one
for ch in s:
    print(ch)
