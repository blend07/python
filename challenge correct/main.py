from abc import ABC,abstractmethod

class person(ABC):
    def __init__(self,name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height
    
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value):
        if value<0:
            return ValueError("Weight can't be lower than 0")
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value<0:
            return ValueError("Height can't be lower than 0")
        
    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):

        print(f"Name: {self.name}, Age: {self.age}")
        print(f"BMI: {self.calculate_bmi()}, Category: {self.get_bmi_category()}")


class adult(person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)
    
    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi <24.9:
            return "Normal weight"
        elif bmi <29.9:
            return "Overweight"
        else:
            return "Obese"



class child(person):
    def calculate_bmi(self):
        return (self.weight / (self.height ** 2)) * 1.3
    
    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif bmi <18:
            return "Normal weight"
        elif bmi <24:
            return "Overweight"
        else:
            return "Obese"

class BMIApp:
    def __init__(self):
        self.people = []
    
    def add_person(self, person):
        self.people.append(person)
    
    def collect_user_data(self):
        name = input("Enter name: ")
        age = int(input("Age: "))
        weight = float(input("Weight(kg): "))
        height = float(input("Height(m): "))

        if age>=18:
            person = adult(name, age, weight, height)
        else:
            person = child(name, age, weight, height)