# In this code I demonstrated how the title function works
# Instead of this code I could have wrote a very simple code using title function, but there would be no logic used there.
name_1 = input("Name:\n")
surname_1 = input("Surname:\n")
def format_name(name, surname):
    name = name.upper()
    surname = surname.upper()
    a = ''
    c = ''
    for i in range(1,len(name)):
        a += name[i]
        b = a.lower()
    for j in range(1,len(surname)):
        c += surname[j]
        d = c.lower()
    return name[0] + b + " " + surname[0] + d
print(format_name(name_1,surname_1))
