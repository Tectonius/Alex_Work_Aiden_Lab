import os

os.chdir('/gpfs0/work/alex')

def fix_file_format(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    # Add a newline after '149:150'
    content = content.replace('149:150', '149:150\n')
    # Remove newlines immediately preceding colons
    fixed_content = content.replace('\n:', ':')
    
    new_directory = 'large_files/fixed_cpulls_300'
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    new_file_path = os.path.join(new_directory, os.path.basename(file_path))
    with open(new_file_path, 'w') as file:
        file.write(fixed_content)

def main():
    directory = 'large_files/cpulls_300/'
    for filename in os.listdir(directory):
        if filename.endswith('.out'):
            file_path = os.path.join(directory, filename)
            fix_file_format(file_path)
            print(f'Fixed file: {file_path}')

if __name__ == "__main__":
    main()