import pprint


def create_cook_book():
    with open('cook_book.txt', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dishes_name = line.strip()
            ingridient_count = int(f.readline())
            ingridient = []
            for i in range(ingridient_count):
                ing = f.readline().strip()
                ingridient_name, quantity, measure = ing.split(' | ')
                ingridient.append({
                    'наименование': ingridient_name,
                    'количество': int(quantity),
                    'мера': measure
                })
            f.readline()
            cook_book[dishes_name] = ingridient
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_cook_book()
    dict_by_dishes = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                ingridient['количество'] *= person_count
                if ingridient['наименование'] not in dict_by_dishes:
                    pop_ingridient = ingridient.pop('наименование')
                    dict_by_dishes[pop_ingridient] = ingridient
                else:
                    pop_ingridient = ingridient.pop('наименование')
                    dict_by_dishes[pop_ingridient]['количество'] += ingridient['количество']

    return dict_by_dishes


res = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 4)
pprint.pprint(res, stream=None, indent=1, width=150, depth=2, compact=False, sort_dicts=False)
