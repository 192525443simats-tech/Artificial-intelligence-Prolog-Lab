rooms = {"A": "Dirty", "B": "Dirty"}

location = "A"

while True:
    if rooms[location] == "Dirty":
        print(location, "is Dirty -> Cleaning")
        rooms[location] = "Clean"
    else:
        print(location, "is already Clean")

    if location == "A":
        location = "B"
    else:
        break

print("\nFinal State")
print(rooms)