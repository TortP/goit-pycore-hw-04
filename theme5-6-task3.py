import sys
import os
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init(autoreset=True)

def print_directory_tree(path, indent=""):
    path = Path(path)
    if not path.exists() or not path.is_dir():
        print(Fore.RED + "Вказаний шлях не існує або це не директорія.")
        return
    
    for item in path.iterdir():
        if item.is_dir():
            print(indent + Fore.BLUE + f"📂 {item.name}")
            print_directory_tree(item, indent + "  ")
        else:
            print(indent + Fore.GREEN + f"📜 {item.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Будь ласка, вкажіть один шлях до директорії як аргумент.")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    print_directory_tree(directory_path)
