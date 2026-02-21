def count_upper_lower(text):
    UC = 0
    LC = 0

    for ch in text:
        if ch.isupper():
            UC += 1
        elif ch.islower():
            LC += 1
    print("\nUppercase =", UC, ", Lowercase =", LC)
    

text = input("Enter Text\n")
count_upper_lower(text)

