age = int(input())
def human(age) :
    if age <= 7 :
        print ("в детский сад")
        return
    elif age <=  16:
        print("учись в школе")
        return
    elif age <= 25:
        print ("учись в институте")
        return
    else:
        print("иди работай")

print (human (30))   

# 2 exercise

a = input()
b = input()
def function(a,b):
    if a == str and b == str:
        print ("ok")
        return
    elif a != str and b != str:
        print("0")
        return
    elif a == b:
        print("1")
        return
    elif a != b and a > b:
        print("2")
        return
    elif a != b and b == "learn":
        print ("3")
    else:
        print("go home")
print(function) 
          