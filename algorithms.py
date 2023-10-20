def fibonacci(a,b):
    lst = [a,b]
    i = 0
    counter = 0
    while lst[i] < 4000000:
        lst.append(lst[i]+lst[i+1])
        i += 1
    for i in lst:
        if i%2 == 0:
            counter += i
    print(counter)


def prime_factor(a):
    i = 1
    lst = []
    biggest = 0
    while i < a:
        while (a/i) != int(a/i):
            i += 1
        lst.append(i)
        a = a / i
        i += 1
    for x in lst:
        if x >= biggest:
            biggest = x
    print(biggest)


def palindrome():
    a = 10
    while a < 1000:
        b = 10
        while b < 1000:
            num = a*b
            num = str(num)
            half = len(num)/2
            first_half = num[:half]
            second_half = num[-half:]
            if first_half == second_half:
                print(a)
                print(b)
        b += 1
    a += 1



def searchfile():
    userid = 12345
    found = False
    filehandle = open("boo.txt", "r")
    per_line = filehandle.readline()
    while len(filehandle) > 0:
        id = per_line[:5].strip()
        content = per_line[6:].strip()
        if userid == id:
            found = True
            break
        per_line = filehandle.readline()

    filehandle.close()
