import itertools

def solution(dishes):
    no_name_dishes = [dish[1:] for dish in dishes]
    ingredients = sorted(set(itertools.chain.from_iterable(no_name_dishes)))
    dishes_by_ingredient = []
    for ingredient in ingredients:
        dishes_by_ingredient.append([ingredient])
        for dish in dishes:
            if ingredient in dish[1:]:
                dishes_by_ingredient[len(dishes_by_ingredient)-1].append(dish[0])

    two_or_more_dishes = list(filter(lambda x: len(x) > 2, dishes_by_ingredient))
    return [[dish[0]] + sorted(dish[1:]) for dish in two_or_more_dishes]


dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

for line in solution(dishes):
    print(line)
