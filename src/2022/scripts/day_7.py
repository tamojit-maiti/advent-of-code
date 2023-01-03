from pathlib import Path

# Path to data
DATA_FOLDER_PATH = Path.cwd() / 'src' / '2022' / 'data'
FILE_NAME = 'day_7_test.txt'
DATA_FILE_PATH = DATA_FOLDER_PATH / FILE_NAME

class Folder:

    def __init__(self, name: str) -> None:
        self.name = name
        self.files = {}             # file-name:size
        self.folders = []           # folder-name

    def add_file(self, filename: str, filesize: int) -> None:
        self.files[filename] = filesize

    def add_folder(self, folder_name: str)-> None:
        self.folders.append(folder_name)

    def get_size(self) -> int:
        total_size = 0
        if self.folders == []:
            total_size += sum(self.files.values())
            return total_size
        else:
            total_size += sum(self.files.values())
            total_size += sum([folder_dict[folder_name].get_size() for folder_name in self.folders])
            return total_size

# Folder Structure
folder_dict = {}

# Reading the data
with open(DATA_FILE_PATH) as f:
    for line in f:
        line = line.strip(' \n')

        if (line.startswith('$ cd')) & (line.endswith('..') == False):
            folder_name = line.split(' ')[-1]
            print('Folder Name Seen : {} '.format(folder_name))

        elif (line.startswith('$ cd')) & (line.endswith('..')):
            pass

        elif line.startswith('$ ls'):
            if folder_name not in folder_dict.keys():
                folder_dict[folder_name] = Folder(name = folder_name)
                print('Folder Name {} created.'.format(folder_name))
            else:
                print('Folder Name {} NOT created since it is already present.'.format(folder_name))
                pass
            
        
        elif line.startswith('dir'):
            child_folder_name = line.split(' ')[-1]
            child_folder = Folder(name = child_folder_name)
            folder_dict[folder_name].add_folder(child_folder_name)
            print('Child Folder {} added to main Folder {}.'.format(child_folder_name,folder_name))

        else:
            filesize = line.split(' ')[0]
            filename = line.split(' ')[1]
            folder_dict[folder_name].add_file(filename = filename, filesize = int(filesize))
            print('File {} added to folder name {}'.format(filename, folder_name))


total_size = 0
for key in folder_dict.keys(): 
    size = folder_dict[key].get_size()
    if size < 100000:
        total_size += size

# Answer to Part I
print(total_size)
        


