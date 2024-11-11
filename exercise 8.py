#List of names
names = ["Jake", "Zac", "Ian", "Ron", "Samm", "Dave"]

#Name to search 
target_name = "Samm"

#Flag to indicate if the name was found
found =False

#Iterate over the list and check for the target name
for name in names:
    if name == target_name:
        found = True
        break

if found:
    print(f"The name'{target_name}'was found in the list.")
else:
    print(f"The name'{target_name}'was not found in the list.")