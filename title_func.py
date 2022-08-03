#title the words with title function
name2 = input("Name:\n")
surname2 = input("Surname:\n")

def capitalize_name(name,surname):
    name1 = name.title()
    surname1 = surname.title()
    print(f"{name1} {surname1}")
capitalize_name(name2,surname2)