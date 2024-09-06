import os


def create_readme(startpath, level=1):
    items = os.listdir(startpath)
    items.sort()
    trash = {
        '.gitignore',
        '.trash',
        'venv',
        '.obsidian',
        'pull.py',
        '.git',
        'README.MD'
    }

    for index, item in enumerate(items):
        if item in trash:
            continue

        path = os.path.join(startpath, item)
        is_last = index == len(items) - 1

        string = f"{'#' * level + ' '}"
        has_ext = item.find('.md')
        
        if has_ext != -1:
            print(f"[[{item.replace('.md', '')}]]")
        else:
            print(string + item)
        
        if os.path.isdir(path):
            create_readme(path, level+1)
            

if __name__ == "__main__":
    start_directory = "."
    create_readme(start_directory)
