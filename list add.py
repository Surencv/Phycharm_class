a = int(input("Please enter the number of string that you want to enter:"))
b = []
c = []
d = []
for i in range(a):
    b.append(input("Please enter the string that you want to enter:"))
print("\n".join(b))
print(b)
combined = ''.join(b)
vowels = "aeiou"
vowel_count = 0
for char in combined:
    if char in vowels:
        vowel_count += 1
print(vowel_count)
test_add = b + c + d
print(test_add)
