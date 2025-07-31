def calculate_series_sum(n):
    series_sum = 0
    current_term = 0
    series_str = ""
    
    for i in range(n):
        current_term = current_term * 10 + 2
        series_sum += current_term
        series_str += str(current_term)
        if i < n - 1:
            series_str += "+"
    
    return series_sum, series_str

def main():
    try:
        n = int(input("Enter the number of terms (n): "))
        
        if n < 1:
            print("The number of terms must be at least 1.")
            return
        
        series_sum, series_str = calculate_series_sum(n)
        print(f"The series is: {series_str}")
        print(f"The sum of the series up to {n} terms is: {series_sum}")
    except ValueError:
        print("Please enter a valid integer for the number of terms.")

if __name__ == "__main__":
    main()
