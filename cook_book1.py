def create_cook_book():
    cook_book1 = {}

    while True:
        dish_name = input("Введите название блюда (или 'выход' для завершения): ")
        if dish_name == "выход":
            break

        quantity_of_ingredients = int(input("Введите количество ингредиентов в блюде: "))

        ingredients = []
        for i in range(quantity_of_ingredients):
            ingredient_name = input("Введите название ингредиента: ")
            quantity = input("Введите количество ингредиента: ")
            measure = input("Введите единицу измерения: ")
            ingredients.append(f"{ingredient_name} | {quantity} | {measure}")

        cook_book1[dish_name] = ingredients

    with open("Открытие и чтение файла\cook_book1.txt", "w", encoding='utf-8') as f:
        for ingredient_name, ingredients in cook_book1.items():
            f.write(ingredient_name + "\n")
            f.write(str(len(ingredients)) + "\n")
            for ingredient in ingredients:
                f.write(ingredient + "\n")
            f.write("\n")

    print("Рецепты успешно сохранены в файле 'cook_book1.txt'!")

create_cook_book()