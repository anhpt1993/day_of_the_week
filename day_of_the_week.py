# day of the week

def check(num):
    list = [1, 2, 3, 4, 5, 6, 7]
    if num in list:
        return True
    else:
        return False
def day(num):
    numbers = [1,2,3,4,5,6,7]
    weekday = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    if num in numbers:
        print("Number {} => {}".format(num,weekday[num-1]))

while True:
    try:
        num = int(input("Enter an integer from 1 to 7: "))
        if check(num) == False:
            print("Error, Out of range!")
            break
        else:
            #print(num)
            break
    except ValueError:
        print("You make me down! An integer, NOT a float or string please!!!")
        print()

day(num)
