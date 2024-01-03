from collections import Counter

pairs = []
print(len(pairs))
names = [name for pair in pairs for name in pair]

# Count occurrences of each name
name_count = Counter(names)

# Find names that appear more than twice
repeated_names = {name: count for name, count in name_count.items() if count > 2}

print("Names that appear more than twice:")
for name, count in repeated_names.items():
    print(f"{name}: {count} times")