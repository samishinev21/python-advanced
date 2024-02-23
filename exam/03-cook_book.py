def cookbook(*recipes):
    recipes_by_cuisines = {}

    for recipe, cuisine, ingredients in recipes:
        if cuisine in recipes_by_cuisines:
            recipes_by_cuisines[cuisine].append((recipe, ingredients))
        else:
            recipes_by_cuisines[cuisine] = [(recipe, ingredients)]
    
    for cuisine, recipe in recipes_by_cuisines.items():
        recipes_by_cuisines[cuisine] = sorted(recipes_by_cuisines[cuisine], key=lambda item: item[0])

    sorted_cuisines = sorted(recipes_by_cuisines.items(), key=lambda item: (-len(item[1]), item[0]))

    result = ""

    for cuisine, recipes in sorted_cuisines:
        result += f"{cuisine} cuisine contains {len(recipes)} recipes:\n"

        for recipe in recipes:
            result += f"  * {recipe[0]} -> Ingredients: {', '.join(recipe[1])}\n"

    return result

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))