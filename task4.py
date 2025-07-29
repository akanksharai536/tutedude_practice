try:
    file = open("sample.txt", "r")
    counter = 1
    for line in file:
        print(f"Line {counter}: {line.strip()}")
        counter += 1
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")