if __name__ == "__main__":
    weight = float(input("Please input your weight (kg): "))
    height = float(input("Please input your height (m): "))

    bmi = weight / (height * height)

    print ("Your BMI is: {:.2f}".format(bmi))