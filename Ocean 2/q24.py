# 24. Temperature Converter: Write a program that converts Celsius to Fahrenheit or Fahrenheit to Celsius, depending on user input (1 point).
select = input("""Enter which convertion you want?
type f for (Fahrenheit to Celsius)
type c for (Celsius to Fahrenheit)
Your Choice : """)
if (select == 'f'):
    f = float(input("Enter temperature in Fahrenheit : "))
    fahrenheitToCelsius = ((f - 32) * 5)/9
    print("Value of", f, "degree Fahrenheit is",
          fahrenheitToCelsius, "degree Celsius.")
elif (select == 'c'):
    c = float(input("Enter temperature in Celsius : "))
    celsiusToFahrenheit = (c * 9)/5 + 32
    print("Value of", c, "degree Celsius is",
          celsiusToFahrenheit, "degree Fahrenheit.")
