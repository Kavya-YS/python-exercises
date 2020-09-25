
def calculate_the_divisor(divisor):
"It calculates the divisor of the number"
list_of_divisors = []
for each_value in range(1,divisor+1):
if divisor % each_value == 0:
list_of_divisors.append(each_value)

return list_of_divisors


if __name__ == "__main__":
input_number = int(input("Enter the number"))
divisor_number = calculate_the_divisor(input_number)
print("The divisors are",divisor_number)
