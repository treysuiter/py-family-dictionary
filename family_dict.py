my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}

for member in my_family.items():

    print(f"{member[1]['name']} is my {member[0]} and is {str(member[1]['age'])} years old.")

fam_string = (f"{member[1]['name']} is my {member[0]} and is {str(member[1]['age'])} years old." for member in my_family.items())

print(fam_string)
