def get_cook_book():
    cook_book = {}
    with open('cook_book.txt', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            ingredients = []
            count = f.readline()
            for i in range(int(count)):
                name, quantity, measure = f.readline().strip().split('|')
                ingredients.append({'ingredient_name': name, 'quantity': quantity, 'measure': measure})
            cook_book.setdefault(dish_name, ingredients)
            empty = f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity']) * person_count
                measure = ingredient['measure']
                shop_list.setdefault(ingredient_name, {'quantity': quantity, 'measure': measure})
        else:
            print(f"Блюда '{dish}' нет в кулинарной книге.")
    print(shop_list)
    return shop_list

cook_book = get_cook_book()
dishes = ['Фахитос','Карбонара']
person_count = 2
get_shop_list_by_dishes(dishes, person_count)
