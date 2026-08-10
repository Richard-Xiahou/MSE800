class TemperatureConverter:

  # initialization function
  def __init__ (self,):
    '''test init'''

  # convert temperature from Fahrenheit to Celsius or Celsius to Fahrenheit
  def getResult(self, temperature):

    prefix = temperature[0];
    value = temperature[1:];

    if prefix == "F":
      fahrenheit = float(value);
      celsius = (fahrenheit - 32) * 5 / 9;

      print ("{} degrees Fahrenheit is converted to {:.2f} degrees Celsius".format(temperature, celsius));
      return True;

    elif prefix == "C":
      celsius = float(value);
      fahrenheit = celsius * 9 / 5 + 32;

      print ("{} degrees Celsius is converted to {:.2f} degrees Fahrenheit".format(temperature, fahrenheit));
      return True;

    else:
      return False;


def main():

  # create a TemperatureConverter object
  ConverterObject = TemperatureConverter();

  temperature = input("Please enter the temperature (e.g. F51 or C11): ");

  result = ConverterObject.getResult(temperature);

  if result == False:
    print ("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.");


if __name__ == "__main__":
  main();