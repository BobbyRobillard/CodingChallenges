class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_cuisines = {}
        self.food_ratings = {}
        for i in range(len(foods)):
            self.food_ratings[foods[i]] = ratings[i]
            if cuisines[i] not in self.food_cuisines:
                self.food_cuisines[cuisines[i]] = [foods[i]]
            else:
                self.food_cuisines[cuisines[i]].append(foods[i])
            
    def changeRating(self, food: str, newRating: int) -> None:
        self.food_ratings[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        max_rated = []
        max_rating = -1
        foods = self.food_cuisines[cuisine]
        for food in foods:
            if self.food_ratings[food] > max_rating:
                max_rated = [food]
                max_rating = self.food_ratings[food]
            elif self.food_ratings[food] == max_rating:
                max_rated.append(food)
        max_rated.sort()
        return max_rated[0]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
commands = ["highestRated","changeRating","changeRating","changeRating","highestRated","highestRated","highestRated","highestRated","changeRating","changeRating","changeRating","changeRating"]
args = [["uudduznsjc"],["jyxxdmeqpy",3],["hxvyjar",19],["bmdzu",12],["uudduznsjc"],["uudduznsjc"],["uudduznsjc"],["uudduznsjc"],["hxvyjar",10],["yxsoc",6],["hxvyjar",14],["yxsoc",2]]
foods = ["ixoldpvcl","bmdzu","zmazdit","wdz","yxsoc","jyxxdmeqpy","hxvyjar","jktdotax","kgdct","kxuhddwif"]
cuisines = ["uudduznsjc","uudduznsjc","uudduznsjc","uudduznsjc","uudduznsjc","uudduznsjc","uudduznsjc","uudduznsjc","uudduznsjc","uudduznsjc"]
ratings = [5,9,4,6,8,6,17,9,11,4]
fr = FoodRatings(foods, cuisines, ratings)
for i, command in enumerate(commands):
    if command == "highestRated":
        print(fr.highestRated(args[i][0]))
    else:
        fr.changeRating(args[i][0], args[i][1])
