# Ask the user for a filename
filename = input("Enter the filename to read: ")

try:
    # Try to open the file
    with open(filename, "r") as f:
        content = f.read()
    
    # Modify the content (example: make uppercase)
    modified = content.upper()

    # Save to output.txt
    with open("output.txt", "w") as f:
        f.write(modified)

    print("✅ File read successfully. Modified content saved to output.txt")

except FileNotFoundError:
    print("Error: That file does not exist.")
