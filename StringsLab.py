#Joseph DeFilippo period 8 10/1/2025

print("Task 1")
first_and_last_name = input("What is your first and last name?")
space = first_and_last_name.find(" ")
first_name = first_and_last_name[0:space]
last_name = first_and_last_name[space+1:]
print(first_name.title(), last_name.title())
print(first_name[0].lower() + first_name[1:].upper(), last_name[0].lower() + last_name[1:].upper())

print("Task 2")
phrase = "Once you start down the dark path, forever will it dominate your destiny."
print(phrase.upper())
modified_phrase = phrase.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
print(modified_phrase)

print("Task 3")
number = len(phrase)

first_section_of_phrase = phrase[0:number//3]
second_section_of_phrase = phrase[number//3:number//3 *2]
third_section_of_phrase = phrase[number//3 *2 :]
print(second_section_of_phrase)
print(third_section_of_phrase)
print(first_section_of_phrase)


print("Task 4")
five_digit_number = input("Please enter a 5 digit number ")
index_one = five_digit_number[0]
index_two = five_digit_number[1]
index_three = five_digit_number[2]
index_four = five_digit_number[3]
index_five = five_digit_number[4]

index_one_int = int(index_one)
index_two_int = int(index_two)
index_three_int = int(index_three)
index_four_int = int(index_four)
index_five_int = int(index_five)

sum = index_one_int + index_two_int + index_three_int + index_four_int + index_five_int
print(index_one, "+", index_two, "+", index_three, "+", index_four, "+", index_five, "=", sum)

print("Task 5")

phrase_2 = "Why, you stuck-up half-witted scruffy-looking nerf-herder."
#58
print(phrase_2[::2])
print(phrase_2[::-2])

print("Task 6")

from datetime import date


today = date.today()

today = today.strftime("%Y,%B,%d")


print(f"The date today is {today}")

day = today[13:15]
month = today[5:12]
year =today[0:4]

print("This is day", day, "of,", month, "of the year", year)
