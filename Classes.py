class Name(object): # Making a class
    def __init__(self, name, age): # Main function
        # Can call any data types using self.
        self.name = name # Input receivig variables 
        self.age = age # Input receivig variables
        self.li = ["Alterings", "Alterings2", "Alterings3", "Alterings4",]

    def speak(self): # calling the text function
        print(f"HI I am {self.name}, And I am {self.age} years old") # Text message

    def change_age(self,age): # Extra function
        self.age = age # Input receiver

    def add_weight(self, weight):
        self.weight = weight
        # weight += 2

Mackenzie = Name("Mackenzie", 13) # giving input
Muriel = Name("Muriel", 5)  # giving input
Mackenzie.change_age(12.5) # Using Change name function
Mackenzie.speak() # Calling the print method
Muriel.speak() # Calling the print method 
print(Mackenzie.name) # Writing the name directly
print(Mackenzie.li) # Prining the list directly
Mackenzie.add_weight(37) # Using the Weight Var
print(Mackenzie.weight) # Calling the weight method