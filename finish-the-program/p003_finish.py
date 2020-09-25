# getting input from the user and assigning it to user

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

# the formula for calculating bmi

bmi = weight/(height**2)
# ** is the power of operator i.e height*height in this case

print("Your BMI is:" +f'{bmi}+"and you are: ")

#conditions
if ( bmi < 16):
   print("severely underweight")

<Fill the line>( bmi >= 16 and bmi < 18.5):
   print("underweight")

<Fill the line>( bmi >= 18.5 and bmi < 25):
   print("Healthy")

<Fill the line>( bmi >= 25 and bmi < 30):
   print("overweight")

<Fill the line>( bmi >=30):
   print("severely overweight")