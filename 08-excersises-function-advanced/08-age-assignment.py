def age_assignment(*names, **ages):
    sorted_names = sorted(names)

    return "\n".join(map(lambda name: f"{name} is {ages[name[0]]} years old.", sorted_names))

print(age_assignment("Peter", "George", G=26, P=19))