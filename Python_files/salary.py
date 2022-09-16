sal = int(input("Enter basic salary:"))

if sal <= 10000:
    gross = sal + sal*0.20 + sal*0.80
    print("gross salary :", gross)
elif sal<=20000:
    gross = sal + sal*0.25 + sal*0.90
    print("gross salary:", gross)
elif sal>20000:
    gross = sal + sal*0.30 + sal*0.95
    print("gross salary:", gross)