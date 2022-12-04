#1
cook_book = {}
with open('receipt.txt', 'rt', encoding='utf8') as file:
    for line in file:
        dish_name = line.strip()
        count = int(file.readline())
        ingredient_list = list()
        for i in range(count):
            ingredients = {}
            ingredient = file.readline().strip()
            ingredients['ingredient_name'], ingredients['quantity'], ingredients['measure'] = ingredient.split('|')
            ingredients['quantity'] = int(ingredients['quantity'])
            ingredient_list.append(ingredients)
        file.readline()
        cook_book[dish_name] = ingredient_list
print(cook_book)

#2
def get_shop_list_by_dishes(dishes, person_count):
    ingredient_list = dict()

    for dish_name in dishes:
        if dish_name in cook_book:
            for ingredients in cook_book[dish_name]:
                list_1 = dict()
                if ingredients['ingredient_name'] not in ingredient_list:
                    list_1['measure'] = ingredients['measure']
                    list_1['quantity'] = ingredients['quantity'] * person_count
                    ingredient_list[ingredients['ingredient_name']] = list_1
                else:
                    ingredient_list[ingredients['ingredient_name']]['quantity'] = \
                        ingredient_list[ingredients['ingredients_name']]['quantity'] + \
                        ingredients['quantity'] * person_count
        else:
            print(f'\n"Ошибка"\n')
    return ingredient_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

#3

import os
def rewrite_file(path1=None, path2=None, path3=None):
    if path1 or path2 or path3 is None:
        path1 = '1.txt'
        path2 = '2.txt'
        path3 = '3.txt'
        os.chdir('sorted')
        out_file = "result.txt"
        file1_path = os.path.join(os.getcwd(), path1)
        file2_path = os.path.join(os.getcwd(), path2)
        file3_path = os.path.join(os.getcwd(), path3)
        with open(file1_path, 'r', encoding='utf-8') as f1:
            file1 = f1.readlines()
        with open(file2_path, 'r', encoding='utf-8') as f2:
            file2 = f2.readlines()
        with open(file3_path, 'r', encoding='utf-8') as f3:
            file3 = f3.readlines()
        with open(out_file, 'w', encoding='utf-8') as f_total:
#
            if len(file1) < len(file2) and len(file1) < len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file2) < len(file1) and len(file2) < len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file3) < len(file1) and len(file3) < len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file1) > len(file2) and len(file1) > len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
            elif len(file2) > len(file1) and len(file2) > len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
            elif len(file3) > len(file1) and len(file3) > len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
    else:
        print('Ошибка')

    return rewrite_file()
