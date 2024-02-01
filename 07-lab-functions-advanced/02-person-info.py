def get_info(name, town, age):
    return (f"This is {name} from {town} and he is {age} years old")

user_info = {"name": "Samuel", "town": "Burgas", "age": "10"}

print(get_info(**user_info))