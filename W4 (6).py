def check_Perfect_number(n):
    s=0
    if n<2:
        print("Not Perfect number ")
        return
    else:
        for i in range (1,n):
            if n%i == 0:
                s += i

        if s == n:
            print("Perfect number ")
        else:
            print("Not Perfect number ")

Num = int(input("Enter a Number : "))
check_Perfect_number(Num)
