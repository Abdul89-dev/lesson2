numbers_scores = [2, 12, 4, 6, 8, 40, 44, 80, 30, 24]

for numb in numbers_scores:
    a = numb + 1
print(a)

#2

for read in "I am Victor":
    print(read.upper())

				
#3
school = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
          {'school_class': '4b', 'scores': [2,5,4,3,2]},
          {'school_class': "4c", 'scores': [5,4,3,5,5]}
]

for school_class in school:
    sum(school_class ["scores"])
    print(school_class ["scores"])
    scores_avg = sum (school_class ["scores"])/ len (school_class ["scores"]) 
    print(f"Средняя оценка {scores_avg}")

# туто до меня не дошло

   
sum = 0
for i in school_class ["scores"]:
    sum = sum + i
print (sum)

result  = sum(school_class ["scores"]) / len (school_class ["scores"]) 
print(f"Средняя оценка по классу {result}")  
  