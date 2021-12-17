first_name = "Qusai"
last_name = "Trabeh"
age = 23

print(str(age))
print((first_name.upper()))
print((last_name.lower()))
print(first_name[1:])
print(last_name[:len(last_name) - 1])

# solution 02
text = "Python is a general purpose computer programming language"
print(text.count("computer"))
print(text.find("computer"))
print(text.replace(" ", ""))

# solution 03
greet = "Hello World"
index_of_space = greet.find(" ")
print(greet[index_of_space + 1:])