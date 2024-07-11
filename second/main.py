from pathlib import Path

def get_cats_info(path):
    try:
        with open(path, "r") as file:
            cats = [el.strip() for el in file.readlines()]
            cats_list = []
            for cat in cats:
                cat_data = cat.split(',')
                if len(cat_data) == 3:
                    cat_dict = {'id': cat_data[0], 'name': cat_data[1], 'age': cat_data[2]}
                    cats_list.append(cat_dict)
                else:
                    answer = 'data is not complete'
                    return answer
        return cats_list
    except (TypeError, FileNotFoundError):
        answer = 'path is not correct'
        return answer

p = Path("C:\\Users\\kasht\\OneDrive\\Documents\\GitHub\\python_modul4_hw\\second\\data.txt")
result = get_cats_info(p)
print(result)