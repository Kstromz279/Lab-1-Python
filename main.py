# Author: Khalil Stroman kzs5955@psu.edu
# Collaborator:Param Nigam pqn5106@psu.edu

# Collaborator: Menghao Li   mxl5939@psu.edu
# Collaborator: Matthew Orehek muo53@psu.edu
degree = input("Enter temperature: ")
degree = float(degree)
unit = input("Enter unit in F/f or C/c: ")
if unit == "C" or unit == "c": 
  fah = (degree * 1.8) +32 
  print(f"{degree}° in Celsius is equivalent to {fah}° Fahrenheit.") 
elif unit == "F" or unit == "f" : 
  cel = (degree-32)/1.8
  print(f"{degree}° in Fahrenheit is equivalent to {cel}° Celsius.")
else : 
  print("Invalid unit(bad).")