'''For extracting todos, just run it with path to target directory as an argument
it just extracts TODO keyword nothing more it doesnt check whether the line is inside a comment or if its a variable
'''

import os
import sys

supported_files = ['.c', '.cpp', '.h', '.py', '.js', '.ts']

def fish_for_todos(target_file: str):
    """Retrun report in console of todos in target files.
    """
    with open(target_file, 'r') as file:
        for i, line in enumerate(file.readlines()):
            if 'TODO' in line:
                print(f'{target_file}"')
                print(f'line {i+1}: {line}')

def find_all_files(target_directory: str):
    """Finds all files in the target directory and its subdirectories.
    :param target_directory: The directory to start searching from
    :type target_directory: str
    :return: A list of file paths found in the target directory and its subdirectories
    :rtype: list
    """
    dir_list = []
    for file_name in os.listdir(target_directory):
        file_path = f"{target_directory}\\{file_name}"
        if os.path.isdir(file_path):
            dir_list.extend(find_all_files(file_path))
        elif os.path.splitext(file_name)[1] in supported_files:
            dir_list.append(file_path)
        else:
            continue
    return dir_list

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: extract_todos.py <directory>')
        sys.exit(1)
    target_directory = sys.argv[1]
    files = find_all_files(target_directory)
    for file in files:
        fish_for_todos(file)
            
