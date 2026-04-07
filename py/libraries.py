import os
import sys
import datetime
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(os.path.abspath(__file__))
print(sys.path[-1])
now = datetime.datetime.now()
today = datetime.date.today()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

# print(f"Now date: {now}")
# print(f"Today's Date: {today}")
# print(f"Current Date and Time: {formatted_date}")

random_number = random.randint(1,100)
random_choice = random.choice(['apple', 'grape', 'orange'])
mixed = [1,2,"hello",4,5,6.5]
random.shuffle(mixed)

print(f"Random Number: {random_number}")
print(f"Random Choice: {random_choice}")
print(f"Shuffled List: {mixed}")