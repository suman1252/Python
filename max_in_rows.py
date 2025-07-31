def find_max_in_rows(matrix):
    max_in_rows = [max(row) for row in matrix]
    return max_in_rows
def main():
    # Sample input matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    max_numbers = find_max_in_rows(matrix)
    
    print(f"The maximum numbers of each row are: {max_numbers}")

main()