import os

print("For the this code type Python Run")
print("-----------------------------------")


run=input()
if run.lower()=="python run":

# Get the path from the user
    path = input("Enter the directory path where you want to create the files: ")

# Ensure the directory exists
if not os.path.exists(path):
    print(f"The directory '{path}' does not exist.")
else:
    # Create the files
    open(os.path.join(path, "index.html"), "w").close()
    open(os.path.join(path, "styles.css"), "w").close()
    open(os.path.join(path, "index.js"), "w").close()
    
    print(f"Files created in '{path}': index.html, styles.css, index.js")
