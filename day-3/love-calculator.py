print("The Love Calculator is calculating your score...")
'''Вводим имена мужика '''
name1 = input('what is your name?')
name2 = input('what is their name?') 

combined_names = name1.lower() +name2.lower()

t_count = combined_names.count('t')
r_count = combined_names.count('r')
u_count = combined_names.count('u')
e_count = combined_names.count('e')

true_score = t_count + r_count + u_count + e_count

l_count = combined_names.count('l')
o_count = combined_names.count('o')
v_count = combined_names.count('v')
e_count_love = combined_names.count('e')

love_score = l_count + o_count + v_count + e_count_love

total_score = int(str(true_score) + str(love_score))
if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif 40 <= total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
