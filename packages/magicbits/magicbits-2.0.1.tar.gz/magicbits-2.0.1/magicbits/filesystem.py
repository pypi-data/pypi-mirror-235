class File:
    def __init__(self, name, content) -> None:
        self.name = name
        self.content = content

class Directory:
    def __init__(self, name ) -> None:
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def list_content(self):
        for child in self.children:
            if isinstance(child, File):
                print(f"File: {child.name}\nContent: {child.content}")
            elif isinstance(child, Directory):
                print(f'Directory: {child.name}')
                child.list_content()

class FileSystem:
    def __init__(self) -> None:
        self.root = Directory('SY')
    
    def create_file(self, path, content):
        parts = path.split('/')
        dir_path, file = parts[:-1], parts[-1]
        current_dir = self.root
        for part in dir_path:
            found = False
            for child in current_dir.children:
                if isinstance(child, Directory) and child.name == part:
                    current_dir = child
                    found = True
                    break
            if not found:
                new_dir = Directory(part)
                current_dir.add_child(new_dir)
                current_dir = new_dir
        
        new_file = File(file, content)
        current_dir.add_child(new_file)

    def list_content(self):
        print('File System Contents')
        self.root.list_content()

if __name__ == '__main__':
    filesys = FileSystem()
    filesys.create_file('Pictures/test.txt', 'Hello This is Text')
    filesys.list_content()