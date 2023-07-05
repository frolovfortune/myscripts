def remove_quotes_from_file(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove quotes from each line
    modified_lines = [line.replace('"', '') for line in lines]

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

# Usage: Call the function and provide the file path
remove_quotes_from_file('path/to/your/file.txt')
