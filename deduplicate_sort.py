# An app that records the animals seen during a nature walk
# The list needs to be alphabetized and remove any duplicates automatically

# Build the animal list
def prepare_list(animals):
    return sorted(set(animals))


# remove any duplicates

animals = ["crow","cat", "bluejay", "cat", "woodpecker", "fox", "fox", "crow"]

result = prepare_list(animals)
print(result)