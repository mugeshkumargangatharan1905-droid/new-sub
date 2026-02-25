# Writing data to file
with open("data.txt", "w") as f:
    f.write("10\n20\n30\n40\n50")

# Reading and calculating average
with open("data.txt", "r") as f:
    numbers = [int(line.strip()) for line in f]

print("Numbers:", numbers)
print("Average:", sum(numbers) / len(numbers))
