import random

class Hashmap:
    def __init__(self):
        self.array_size = 5
        self.val_array = [None for _ in range(self.array_size)]
        self.key_array = [None] * self.array_size

    def cal_hash(self, string):
        # Calculates hash using linear probing
        sum = 0
        for char in string:
            sum += ord(char)
        index = sum % self.array_size
        while self.key_array[index] != None and self.key_array[index] != string: # if index is not free and if some key already occupied the index
            sum += 1
            index = sum % self.array_size
        return index # if the index value is NULL, finally return it
    
    def __setitem__(self, key, value):
        index = self.cal_hash(key)
        self.key_array[index] = key
        self.val_array[index] = value

    def __getitem__(self, key):
        index = self.cal_hash(key)
        while (self.key_array[index] != key):
            index += 1
            index %= self.array_size
        return(self.val_array[index])    
    

dictionary = Hashmap()

for i in range(1, 6):
    day = f'day{i}'
    dictionary[day] = random.randint(10, 30)

# printing the keys and the values dictionary
print(f"dictionary keys: {dictionary.key_array}")
print()
print(f"dictionary values: {dictionary.val_array}")
print()

for i in range(1, 6):
    day = f'day{i}'
    print(f"{day}: {dictionary[day]}")
