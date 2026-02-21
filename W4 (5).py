def txn_sum(string):
    s=0
    for digit in str(string):
        s+=int(digit)
    return s

st = input("Enter an string : ")
print(txn_sum(st))
