# Function 'speak' defined as a placeholder (it is not used here, just defined)
def speak():
    pass

# Create the parent class 'Animal' dynamically using type()
# The 'Animal' class has:
# - A class-level attribute 'kingdom' set to "Animalia"
# - A method 'speak' (not implemented yet, it will be overridden in subclasses)
Animal = type('Animal', (), {'kingdom': 'Animalia', 'speak': speak})

# Define a specific method 'speak' for the 'Cat' class
def cat_speak(self):
    print('Meoww Meoww !!')

# Define the constructor (__init__) for the 'Cat' class, which adds 'color' attribute
def cat_init(self):
    self.color = 'White'

# Define a specific method 'speak' for the 'Dog' class
def dog_speak(self):
    print('Woof Woof !!')

# Define the constructor (__init__) for the 'Dog' class, which adds 'breed' attribute
def dog_init(self):
    self.breed = 'labrador'

# Create the 'Dog' class dynamically using type()
# - It inherits from the 'Animal' class
# - Adds the 'breed' attribute (initialized by dog_init)
# - Overrides the 'speak' method with dog_speak
Dog = type('Dog', (Animal,), {'__init__': dog_init, 'speak': dog_speak})

# Create the 'Cat' class dynamically using type()
# - It inherits from the 'Animal' class
# - Adds the 'color' attribute (initialized by cat_init)
# - Overrides the 'speak' method with cat_speak
Cat = type('Cat', (Animal,), {'__init__': cat_init, 'speak': cat_speak})

# Create objects of 'Dog' and 'Cat'
dog_obj = Dog()
cat_obj = Cat()

# Call the 'speak' method for both objects
dog_obj.speak()  # Output: Woof Woof !!
cat_obj.speak()  # Output: Meoww Meoww !!

# Print the 'kingdom' attribute (inherited from 'Animal') for cat_obj
print('Kingdom : ', cat_obj.kingdom)  # Output: Animalia

# Print the 'breed' attribute for dog_obj (initialized in dog_init)
print('Dog -> Breed : ', dog_obj.breed)  # Output: labrador

# Print the 'color' attribute for cat_obj (initialized in cat_init)
print('Cat -> Color : ', cat_obj.color)  # Output: White
