sub1=int(input("Enter the marks of Subject1 "))
sub2=int(input("Enter the marks of Subject2 "))
sub3=int(input("Enter the marks of Subject3 "))
sub4=int(input("Enter the marks of Subject4 "))

total=sub1+sub2+sub3+sub4
print("Total:",total)



per=(sub1+sub2+sub3+sub4)/4
print("Percentage:",per)

if (sub1 and sub2 and sub3 and sub4)<40:
    print("Fail")

    if per>=80:
        print("Distinction")
    elif per>=70:
        print("First Class")
    elif per>=60:
        print("Second Class")
    elif per>=50:
        print("Pass Class")
    elif per<40:
        print("Fail")   