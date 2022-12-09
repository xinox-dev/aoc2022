class File:
    def __init__(self, name, size, level):
        self.name = name
        self.size = size
        self.level = level

    def view(self):
        print(f"{' ' * self.level}- {self.name} (file, size={self.size})")


class Catalog:
    def __init__(self, name, parent=None, level=0):
        self.parent = parent
        self.files = []
        self.name = name
        self.level = level

    def get_size(self):
        size = 0
        for file in self.files:
            if isinstance(file, File):
                size += file.size
            else:
                size += file.get_size()

        return size

    def add_file(self, file):
        self.files.append(file)

    def get_children(self):
        children = []
        for file in self.files:
            if not isinstance(file, File):
                children.append(file)

        return children

    def view(self):
        print(f"{' '*self.level}- {self.name} (dir)")
        for file in self.files:
            file.view()


def directories_of_100k(input):
    device = parse_to_tree(input)
    memory = 0
    for size in sizes_of_dirs(device):
        if size <= 100_000:
            memory += size

    return memory


def directory_to_delete(input):
    device = parse_to_tree(input)

    space_limit = 70_000_000
    need_space = 30_000_000
    size_of_device = device.get_size()
    space_to_free_up = need_space - (space_limit - size_of_device)
    memory_to_delete = size_of_device

    for size in sizes_of_dirs(device):
        if size >= space_to_free_up:
            memory_to_delete = min(memory_to_delete, size)

    return memory_to_delete


def sizes_of_dirs(file):
    memory = [file.get_size()]
    children = file.get_children()
    if children:
        for child in children:
            memory.extend(sizes_of_dirs(child))

    return memory


def parse_to_tree(input):
    device = Catalog('/')
    cursor = device
    ls_flag = False

    for log in input[1:]:
        if log[:4] == "$ cd":
            ls_flag = False
            name = log.split()[2]

            if name == "..":
                cursor = cursor.parent

            else:
                catalog = Catalog(name, cursor, level=cursor.level + 1)
                cursor.add_file(catalog)
                cursor = catalog

        if log == "$ ls":
            ls_flag = True
            continue

        if ls_flag:
            ftype, name = log.split()
            if ftype.isdigit():
                file = File(name, size=int(ftype), level=cursor.level + 1)
                cursor.add_file(file)
            continue

    return device


