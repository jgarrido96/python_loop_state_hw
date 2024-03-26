
# 1. The Range Riddle

# Task: 1 Your mood today


import random

days = ["Monday", "Tuesday", "Wednesday", "Thusrday", "Friday", "Saturday", "Sunday"]
moods = ["Happy", "Sad", "Energetic", "Calm"]
for day in range(len(days)):
    print(f'On {days[day]} I was feeling {random.choice(moods)}')

print('\n')
# 2. Double Scoop with Nested Loops

# Task 1: Your mood tracker
    
    
days = ["Monday", "Tuesday", "Wednesday", "Thusrday", "Friday", "Saturday", "Sunday"]
moods = ["Happy", "Sad", "Energetic", "Calm"]
times = ["Morning", "Afternoon", "Evening"]
for day in range(len(days)):
    for time in times:
        print(f'On {days[day]} {time} I was feeling {random.choice(moods)}')

print('\n')
# 3. Loop Condition Logic

# Task: 1
count = 0
while True:
    print("Woops, it's a copy.")
    count += 1
    if count == 5:
        break
print('\n')
# Task: 2
    
count = 0
while count < 5:
    print("Woops, it's a copy.")
    count += 1

# 4. Python's Random Game Night

# Task: 1

fruit_list = ["apples", "oranges", "blueberries", "strawberries", "watermelon"]
# print(fruit_list)
user_input = input(f"Guess which item will be selected next from the following list! {fruit_list}: " )
computer_choice = random.choice(fruit_list)

if user_input == computer_choice:
    print("Congratulations!! You guessed right!")
else:
    print(f"Sorry, that's not correct. The correct answer is {computer_choice}")

print('\n')
# 5. Looping Lists- The Rhythm of Repetition
    
# Task: 1

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for genre in genres:
    if genre == "Jazz":
        print(f"This is {genre} track #{genres.index(genre)+ 1}. Hope ya like Jazz.")
    elif genre == "Rock":
        print(f"This is {genre} track #{genres.index(genre)+ 1}. Time to rock and roll all night.")
    elif genre == "Hip-hop":
        print(f"This is {genre} track #{genres.index(genre)+ 1}. Let's have a party.")
    elif genre == "Classical":
        print(f"This is {genre} track #{genres.index(genre)+ 1}. Keep it classy, my friend.")
print('\n')
# Task 2:
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
counter = 0
while counter < len(genres):
    # print(f"This is a track #{genres[counter]}. Hope ya like Jazz.")
    if genres[counter] == "Jazz":
        print(f"This is {genres[counter]} track #{counter + 1}. Hope ya like Jazz.")
    elif genres[counter] == "Rock":
        print(f"This is {genres[counter]} track #{counter + 1}. Time to rock and roll all night.")
    elif genres[counter] == "Hip-hop":
        print(f"This is {genres[counter]} track #{counter + 1}. Let's have a party.")
        break
    elif genres[counter] == "Classical":
        print(f"This is {genres[counter]} track #{counter + 1}. Keep it classy, my friend.")
    counter += 1

print('\n')
# Task 3:
 #          0        1        2           3 
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
for genre in range(len(genres)):
    if genres[genre] != "Classical" and genres[genre] != "Jazz":
        print(f"The {genres[genre]} track's light show is ready! Hope you enjoy the show!")
    else:
        print(f"The {genres[genre]} track is not suitable for a light show.")

print('\n')

# 6. Advanced Looping Techniques

# Task: 1
new_list = []
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
# print(genres[1:4])


for genre in genres[1:4]:
    print(genre)
new_list.append(genres[1:4])
print(new_list)
print('\n')

# Task: 2
new_list = []
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
for genre in genres:
    new_list.append(genre + " Music")
print(new_list)
print('\n')

# Task: 3
for countdown in reversed(range(1,11)):
    print(countdown)
    if countdown == 1:
        print("The beat drops now!")
    



# while count > 0:
#     for count in countdown:
#         print(count)
#         count -= 1
# while count < 10:
#     count += 1
#     print(countup.index(count))
# else:
#     print("The beat drops now!")
#         print(f"This is {genre} track #{genres.index(genre)+ 1}. Keep it classy, my friend.")
