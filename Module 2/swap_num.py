# Swapping with using third variable
a=87
b=55
temp=a #87
a=b #55
b=temp #87
print("A=",a)
print("B",b)

# Swapping without using third variable
a=87
b=55
a,b=b,a
print("A=",a)
print("B=",b)