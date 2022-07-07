def BMI_algorithm(BMI_score):
    if BMI_score < 18.5:
        print("*****")
        print("BMI: {}".format(round(BMI_score, 4)))
        print("Underweight")
    elif BMI_score < 24.9:
        print("*****")
        print("BMI: {}".format(round(BMI_score, 4)))
        print("Healthy weight")
    elif BMI_score < 29.9:
        print("*****")
        print("BMI: {}".format(round(BMI_score, 4)))
        print("Overweight")
    elif BMI_score < 34.9:
        print("*****")
        print("BMI: {}".format(round(BMI_score, 4)))
        print("Obese")
    else:
        print("*****")
        print("BMI: {}".format(round(BMI_score, 4)))
        print("Extremely Obese")
        
class BMI_calculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    def imperial_units(self):
        my_BMI = 703 * (self.weight / self.height**2)
        BMI_algorithm(my_BMI)
        
    def metric_units(self):
        my_BMI = self.weight / self.height**2
        BMI_algorithm(my_BMI)

def BMI_checker():
    while True:
        choice = input("Check BMI with Imperial or Metric units? ").lower()
        if choice == "imperial":
            weight = float(input("Input weight in lbs: "))
            height = float(input("Input height in inches: "))
            imp = BMI_calculator(weight, height)
            imp.imperial_units()
            return
        elif choice == "metric":
            weight = float(input("Input weight in kg: "))
            height = float(input("Input height in meters: "))
            met = BMI_calculator(weight, height)
            met.metric_units()
            return
        else:
            print("Unrecognized response")
            print("Try again")
