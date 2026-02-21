def is_pr(a):
    i=2
    pr = True
    while(i<a/2):
        if a%i==0:
            pr = False
            break
        i=i+1
    if pr == True:
        print(a,"is Prime Number")
    else:
        print(a,"is not a Prime Number")

n = int(input("Enter a number \n"))
is_pr(n)
