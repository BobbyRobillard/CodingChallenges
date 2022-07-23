class NumberContainers:

    def __init__(self):
        self.index_to_num = {}
        self.num_to_index = {}

    def __str__(self):
        return (str(self.index_to_num) + "\n" + str(self.num_to_index))

    def change(self, index: int, number: int) -> None:
        # 1) New index, new number
        if (index not in self.index_to_num) and (number not in self.num_to_index):
            self.index_to_num[index] = number
            self.num_to_index[number] = [index]
        # 2) New index, same number
        elif index not in self.index_to_num:
            self.index_to_num[index] = number
            self.num_to_index[number].append(index)
        # 3) Same index, new number
        elif number not in self.num_to_index:
            # Find index of old number at this place, remove from num_to_index
            old_num_index = self.index_to_num[index]
            self.num_to_index[old_num_index].remove(index)
            # Delete list from dict if empty
            if len(self.num_to_index[old_num_index]) == 0:
                del self.num_to_index[old_num_index]
            # Update value
            self.index_to_num[index] = number
            self.num_to_index[number] = [index]

    def find(self, number: int) -> int:
        if number in self.num_to_index:
            return min(self.num_to_index[number])
        return -1

s = NumberContainers()
actions = ["change","change","find","find","find","change","find","find","change","find","change","change","change","find","find","change","find","change","change","change"]
values = [[25,50],[56,31],[50],[50],[43],[30,50],[31],[43],[25,20],[50],[56,43],[68,31],[56,31],[20],[43],[25,43],[43],[56,31],[54,43],[63,43]]
results = []
for i, item in enumerate(actions):
    if item == "change":
        print("Chaning position:", values[i][0], "to", values[i][1])
        s.change(values[i][0], values[i][1])
        print(s)
        print()
    else:
        results.append(s.find(values[i][0]))
print(str(results))