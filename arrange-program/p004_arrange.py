# Solution
def divisors(number):
divisor_list = []
for each_number in range(2,number):
if number%each_number == 0:
divisor_list.append(each_number)

return divisor_list

while True:
input_number = input('Input your number to check primality, type "exit" to exit the program:')
if input_number.lower() == "exit":
break
try:
input_number = int(input_number)
divisors_of_input_number = divisors(input_number)
print('Your input is primality' if len(divisors_of_input_number) == 0 else 'Your input is not primality')
except:
print('Input error')
continue