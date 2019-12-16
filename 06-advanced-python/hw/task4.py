"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:
> print(folder1)
V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1
А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True
"""

class PrintableFolder:
    
    def __init__(self, name, content = None):
        self.name = name
        self.content = content

    def __str__(self, depth = 0):
        string = ''
        if isinstance(self.content, PrintableFile):
            string = f'{string}\n {"|   " * depth}|-> {self.content.__str__(depth + 1)}'
        else:
            for item in self.content:
                string = f'{string}\n {"|   " * depth}|-> {item.__str__(depth + 1)}'
        return f'V {self.name}{string}'
    
     
    def __contains__(self, file_name):
        result = False
        contents = list(self.content)
        while contents:
            item = contents.pop()
            if isinstance(item, PrintableFolder):
                try:
                    contents.extend(item.content)
                except TypeError:
                    contents.append(item.content)
            elif file_name == item:
                result = True
        return result
                
class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self, depth = 0):
        return f'{self.name}'
 

file1 = PrintableFile('file1')
file2 = PrintableFile('file2')
file3 = PrintableFile('file3')
file4 = PrintableFile('file4')
folder4 = PrintableFolder('folder4', [])
folder3 = PrintableFolder('folder3', [folder4, file3, file4])
folder2 = PrintableFolder('folder2', [folder3, file2])
folder1 = PrintableFolder('folder1', [folder2, file1])

print(folder1)
print(file4 in folder1) #True
print(file1 in folder2) #False
