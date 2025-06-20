'''
2.Write a function that reads a text file and returns its
lines.
Requirements:
Use with open(...) as f:
Catch and handle FileNotFoundError with a user-friendly message.
From main(), prompt user for file name, call read_lines, then print line
count
'''


def read_lines(file) -> int:
    try:
        line_count = 0
        with open(file, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            for line in lines:
                print(line)
    except FileNotFoundError:
        print(f"Error:'{file}' not found.")
        
    
    return line_count


if __name__ == "__main__":
    file= input("Enter the file name: ")
    
    print(read_lines(file))
