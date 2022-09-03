
# task 1

your_age = 15
print(your_age)
your_height = 1.65
print(your_height)
your_weght = 51.3
print(your_weght)
your_gender = "male"
print(your_gender)

# task 2

time_sec = 367897
hours = time_sec // 3600
minutes = time_sec % 3600 // 60
seconds = time_sec % 3600 % 60
print(hours,":",minutes,":",seconds)

#task 3

n = 15
answer = n+n**2+n**3
print(answer)


#task 4

a = int(input('enter integer > 0: '))
largest = 0
while a > 0:
     b = a % 10
     if b > largest:
         largest = b
     a = a // 10
print('the largest figur is ', largest)




#task 5,6

check = float(input('check: '))
print(check)
costs = float(input('costs: '))
print(costs)
if check > costs:
    print('verdict: you are successful businessman')
    rent = (check - costs) / check
    print('rent:', rent)
elif check < costs:
    print('verdict: spending exceeds income')



#task 7: код не работает:((, говорит про любые маневры в строке 62 между p и f как про недопустимые

f = int(input('enter first day distance (km)'))
p = int(input('enter your purpose (km)'))
d = 1
while f < p:
    f = f + f * 0,1
    d = d + 1
print('Days', d)


















