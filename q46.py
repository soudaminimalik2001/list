question_list = [
"How many continents are there?", # pehla question
"What is the capital of India?", # doosra question
"NG mei kaun se course padhaya jaata hai?" # teesra question
]

options_list = [
#pehle question ke liye options
["Four", "Nine", "Seven", "Eight"],
#second question ke liye options
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#third question ke liye options
["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

solution_list = [3, 4, 1]
print("game started")

a=0
while a<=3:
    print(question_list[a])
    i=0
    while i<=len(options_list):
        s=options_list[a][i]
        print(s)
        i=i+1
    user=int(input('enter your answer'))
    if user==solution_list[a]:
        print("your answer is correct")
        print('next question')
    else:
        print("your answer is wrong")
        break
    a=a+1
#KBC Game