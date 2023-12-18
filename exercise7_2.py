# Create following types of lists: fruits; includes items [apple, pear and banana], berries; [strawberry,
# blueberry, blackberry], vegetables; [carrot, kale, cucumber]

fruits = ["apple", "pear", "banana"]
berries = ["strawberry", "blueberry", "blackberry"]
vegetables = ["carrot", "kale", "cucumber"]

# Create a list called inventory, which contains previous lists
inventory = [fruits, berries, vegetables]

# Create a loop, which creates variables to store contents of inventory, create a second loop inside,
# of the first loop, which prints out the variables
for contents in inventory:
    content = " ".join(map(str, contents))
    for item in contents:
        print(item)

