class Solution:
    def __init__(self):
        self.recipesToIngredients = {}
        self.supplies = []
        self.recipes = []
    
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        self.supplies = supplies
        self.recipes = recipes
        # Map ingredients to recipes
        for i, r in enumerate(recipes):
            self.recipesToIngredients[r] = ingredients[i]

        # Call helper method with each recipe
        return [r if self.helper(r) else None for r in recipes]
    
    def helper(self, recipe):
        for i in self.recipesToIngredients[recipe]:
            if i not in self.supplies:
                return False if i not in self.recipes else self.helper(i)
        return True



recipes = ["ju","fzjnm","x","e","zpmcz","h","q"]
inredients = [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]]
supplies = ["f","hveml","cpivl","d"]

s = Solution()
res = s.findAllRecipes(recipes, inredients, supplies)
print(res)