__author__ = 'seamaster'


def my_sqrt(n):
    x = 1000
    while x*x > n:
        x = x // 2
        print(x)
    #print("After all those divisions: " + str(x))
    while x*x < n:
        x *= 2
        print("Trying to catch up with that huge number: " + str(x))
        y = x
        #print("1000er: " + str(x))
    #print("After adding many many thousends: " + str(x))
    x = x // 2
    print("just wondering: " + str(x))
    while x*x < n:
        print("This is {n} - {x} * {x}".format(**locals()))
        x += (y-(x)) // 2
    print("Oh too far. " + str(x))
        #y = x
    while x*x > n:
        x -= 1000000
        #print("Trying to calm down: " + str(x))
    while x*x < n:
        x += 1000
    while x*x > n:
        x -= 50
    #print("Nooo subtractions again: " + str(x))
    while x*x <= n:
        x += 1
        #print("subtracting one again: " + str(x))
    #print("Finally: " + str(x))
    return x-1


n = 0xB364369BF8639EBB55B7B62943452D1BEC599EE3C943D5ED311D8173D9EBA0E1

int_n = int(n)

e = int(0x10001)

x = my_sqrt(int_n)
print("Here is my square root -> "+ str(x))
if x % 2 == 0:
    x -= 1
counter = 0


while x > 0:

    y = n % x
    if counter % 1000000 == 0:
    #print(y)
        print("Attemp no. :" + str(counter) + " X = " + str(x))
    if y == 0:
        print("here i found something: " +str(x))
        break
    x -= 2
    counter += 1



#my_sqrt(17)
