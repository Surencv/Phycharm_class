# name = "simon" # declaring a string
# name = 1234 # not a string
h = "hello"
w = "world"
new = h + w
print(new)
print(h + "Surendar \n" + w)
print(h + w * 2)
print(h + " Surendar " + w)
# in or = not in
print('h' in "hello")
if "h" not in "hello":
    print("NO h in hello")
else:
    print("h in hello")

# "A"=="A" true or false, != not equals to,
# string slicing ex word[1:3] - respons it will print only es
# .split()
message = ("newzealnd is beatiful")
the_word = message.split()
print(the_word)
# lenghth of a string len()
print(len(the_word))
# find .find
the_word = message.find("is")
print(the_word)
# replace .replace()
the_word = message.replace("newzealnd", "India")
print(the_word)
