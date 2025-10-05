FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def main():
    #keep asking for input unless it is a number
    while True:     
        temp = input("Enter the temperature to convert: ")
        try:
            temp = float(temp)
            break
        except ValueError:
            print("Invalid temperature please enter a Numeric value")

    temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

    if temp_unit == "F":
        celsius = convert_to_celsius(temp)
        print(f"{celsius}\u00B0C")

    elif temp_unit == "C":
        fahrenheit = convert_to_fahrenheit(temp)
        print(f"{fahrenheit}\u00B0F")
    

def convert_to_celsius(fahrenheit):
    c = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return c


def convert_to_fahrenheit(celsius):
    f = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return f
    

if __name__ == "__main__":
    main()