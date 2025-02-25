"""
Solution to the "CBT" milestone project.
Find the problem at:
https://docs.google.com/presentation/d/1BH-P4RbhZK3YNmhIua4yMPxFEkuDnyXJ89chy7-uTQA/edit#slide=id.g2efb2b170aa_0_369
"""

question_one = """
1. What is 2 + 2?
a) 3
b) 4
c) 5
d) 6
"""

question_two = """
2. What color is the sky on a clear day?
a) Red
b) Blue
c) Green
d) Yellow
"""

question_three = """
3. How many legs does a spider have?
a) 6
b) 7
c) 8
d) 9
"""


question_four = """
4. What sound does a cow make?
a) Meow
b) Bark
c) Moo
d) Quack
"""

question_five = """
5. What is the opposite of 'hot'?
a) Warm
b) Cold
c) Cool
d) Boiling
"""


questions = [
    {'question': question_one, 'answer': 'b'},
    {'question': question_two, 'answer': 'b'},
    {'question': question_three, 'answer': 'c'},
    {'question': question_four, 'answer': 'c'},
    {'question': question_five, 'answer': 'b'},
]


score = 0
POINTS_FOR_EACH_QUESTION = 1

for question in questions:
    print(question['question'])
    print("\n")
    choice = input("Enter an option from a to d: ").lower().strip()
    if choice == question['answer']:
        score += POINTS_FOR_EACH_QUESTION

print(f"At the end of the the CBT exam, you scored {score} points.")

