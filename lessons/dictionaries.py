"""Demostrations of dictionaries capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary 
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# Print a dictionary literal represention 
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students.") 

# Remove a key-value pair from a dictionary 
# by its key.
schools.pop("Duke")

# Test for the existance of a key

is_duke_present: bool = "Duke" in schools 
print(f"Duke is present: {is_duke_present}")

if "Duke" in schools:
    print("Found the key 'Duke' in schools.") 
else:
    print("No key 'Duke' in schools.")

# Update / Reassign a key-value pair
schools["UNC"] = 20_000
schools["NCSU"] += 200

print(schools)

# Demostration of dictionary literals

# Empty dictionary literal
schools = {}
print(schools)

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
