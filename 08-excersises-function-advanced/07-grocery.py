def grocery_store(**items):
    result = sorted(items.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))

    return "\n".join(map(lambda x: f"{x[0]}: {x[1]}",  result) )

print(grocery_store(bread=2,
    pasta=2,
    eggs=20,
    carrot=1
))