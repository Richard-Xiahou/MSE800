class BMI:
  def __init__ (self,):
    '''test init'''

  def getResult(self, weight, height):
    bmi =  weight / (height * height);
    print ("Your BMI is: {:.2f}".format(bmi))

def main():
  BmiObject = BMI()
  BmiRes = BmiObject.getResult(56,1.70)

if __name__ == "__main__":
  main()