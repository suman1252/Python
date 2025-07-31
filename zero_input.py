def main():
    numbers = []
    
    while True:
        num = float(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        numbers.append(num)
    
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"The average of the entered numbers is: {average}")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()