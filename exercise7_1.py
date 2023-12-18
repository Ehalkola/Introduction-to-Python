# Copy a list from moodle called cafe, which contains lists: name, website, categories and
# location
cafe = {
    "name": "Imaginary Cafe Ltd.",
    "website": "https://edu.frostbit.fi/sites/cafe/en",
    "categories": [
        "cafe",
        "tea",
        "lunch",
        "breakfast"
        ],
    "location": {
        "city": "Rovaniemi",
        "address": "Test address 22",
        "zip_code": "FI-96100"
    },
}

# Create a printout for the "name" from the list
print(cafe["name"])

# Create a printout for cafe address
address = cafe["location"]["address"]
print(address)

# Create a printout for zipcode and city
city = ("".join(cafe["location"]["zip_code"]) + " " + (cafe["location"]["city"]))
print(city)

# Create a printout for the website
print(cafe["website"])

# Create a printout of the services and website
services = (", ".join(cafe["categories"]))
print(f"Services: {services}")

