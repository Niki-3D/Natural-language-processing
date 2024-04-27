import re

list_of_names = ["Joe Doe", "joedoe", "-Joe Doe", "joe doe", "joo doee", "   joe DOE  ", "Joe Doe", "joe doe", "Joee Do"]

def clean_name(name):
    return name.strip().title()

def remove_unnecessary_characters(name):
    return re.sub(r"[^\w\s]", "", name.strip()).replace("  ", " ")

print([clean_name(remove_unnecessary_characters(name)) for name in list_of_names])