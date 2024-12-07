# Py2PlantUML
A collection of Python scripts to analyze Python code and generate class diagram PlantUML files for better visualization and documentation

<h1>PyClassDiagram</h1>
<h2>Usage</h2>
Run the script to analyze a Python file and generate a .puml file:

`python analyzer.py example.py`
<h1>Example</h1>
<p>Example Python Code :</p>

```
  class Animals:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animals):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"

class Cat(Animals):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return "Meow!"

class Owner:
    def __init__(self, owner_name):
        self.owner_name = owner_name

    def owns(self, pet: Animals):
        print(f"{self.owner_name} owns a pet named {pet.name}.")

```        


![image](https://github.com/user-attachments/assets/b1468d32-5f0a-47d0-9bb0-377fed184028)
