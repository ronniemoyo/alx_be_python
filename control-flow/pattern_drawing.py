def main():
    # Prompt the user to enter the size of the pattern
    size = int(input("Enter the size of the pattern: "))

    # Ensure the user enters a positive integer
    while size <= 0:
        size = int(input("Please enter a positive integer for the size of the pattern: "))

    # Draw the pattern using nested loops
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after completing a row
        row += 1

if __name__ == "__main__":
    main()
