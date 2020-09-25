
import random

guess_log = []
generated_number = random.randint(1, 9)
while True:
# Get input
input_string = input('Guess a number between 1 and 9. Type "exit" to exit the game:')
if input_string.lower() == 'exit':
print('See you next time!')
break
# Check the input value
try:
guess_number = int(input_string)
if guess_number not in range(1, 10):
print('Your number is outrange.')
continue
except:
print('Input error.')
continue
# Compare
guess_log.append(guess_number)
if guess_number != generated_number:
print('Your guess is too high!' if guess_number > generated_number else 'Your guess is too low!')
else:
print('Exactly right! After {} guess(es).\n{}'.format(len(guess_log), guess_log))
# Reset
guess_log = []
generated_number = random.randint(1, 9)
