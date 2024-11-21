names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

def search_names(names, search_term):
    found = search_term in names
    
    if found:
        return f"'{search_term}' found in the list."
    else:
        return f"'{search_term}' not found in the list."


search_term = input("Enter the name to search: ")

result = search_names(names, search_term)

print(result)
