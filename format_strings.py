def format_strings(strings):
    # Combine the strings with '-' and format the result as required
    formatted_str = '-'.join(strings)
    formatted_str = formatted_str.capitalize() + '-Started-By-LNB'
    return formatted_str

def main():
    # Given strings
    strings = ["Data", "Science", "Mentorship", "Program"]
    
    result = format_strings(strings)
    
    print(result)

if __name__ == "__main__":
    main()
