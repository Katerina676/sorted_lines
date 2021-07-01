import os

path = os.getcwd()
def find_files(path):
    list_doc = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if(file.endswith(".txt")):
                path_a = os.path.join(root,file)
                name = os.path.basename(path_a)
                list_doc.append(name)
    return list_doc

files_in_dir = find_files(path)

def open_files(files):
    dict_file = {}
    for i in files:
        with open(i, 'r', encoding='utf8') as file:
            count_lines = len(file.readlines())
            dict_file[i] = count_lines
    sorted_tuple = sorted(dict_file.items(), key=lambda x: x[1])
    dict_file_sort = dict(sorted_tuple)
    return dict_file_sort

def write_sorted_lines(files):
    for key, value in files.items():
        with open(key, 'r', encoding='utf8') as file:
            with open('all.txt', 'a', encoding='utf8') as f:
                f.write(f'\n{key} \n{value}\n')
                f.write(file.read())

dict_lines_in_files = open_files(files_in_dir)
print(dict_lines_in_files)
write_sorted_lines(dict_lines_in_files)
