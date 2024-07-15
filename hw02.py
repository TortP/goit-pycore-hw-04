def get_cats_info(path):
    try:
        cats_info = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cat_dict = {"id": id, "name": name, "age": age}
                cats_info.append(cat_dict)
        return cats_info
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []


# Приклад використання функції
cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
