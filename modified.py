# Step 1: Create input.txt
with open("input.txt", "w") as f:
    f.write("Hi am Shee, software developer")

# Step 2: Read input.txt
with open("input.txt", "r") as f:
    content = f.read()

# Step 3: Modify (make uppercase)
modified = content.replace("Hi am Shee, software developer", "Hi am shiks, Tech enthisiast")

# Step 4: Write to output.txt
with open("output.txt", "w") as f:
    f.write(modified)

print("Done! Check output.txt")
