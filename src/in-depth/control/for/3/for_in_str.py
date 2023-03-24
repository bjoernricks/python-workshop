def count_characters(text):
    counts = {}
    for character in text:
        count = counts.get(character, 0)
        count = count + 1
        counts[character] = count
    return counts


lorem = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam"

print(count_characters(lorem))

# optional:
# * don't differentiate by case
# * sort occurrences
