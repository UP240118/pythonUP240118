# 1
a = "Thrity" 
b = "Days"
c = "Of"
d = "Python"
print (a, b, c, d)

# 2
e = "Coding"
f = "For"
g = "All"
print(e, f, g)

# 3, 4, 5
Company = "Coding For All"
print (Company, len(Company))

# 6, 7, 8
h = Company.upper()
i = Company.lower()
print (h,"-",i)
print (Company.capitalize(),"-",Company.title(),"-",Company.swapcase())

# 9
Company1 = "Coding For All"
Company1 = Company1.strip("Coding")
print(Company1)

# 10
print("Coding" in Company)

# 11, 12, 13, 14
Company = Company.replace("Coding", "Python")
print(Company)

Company = Company.split()
print(Company)

C1 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
C1 = C1.split(",")
print(C1)

# 15, 16, 17
C2 = "Coding For All"
C2 = C2[0]
print(C2)

C3 = "Coding For All"
C3 = C3[-1]
print(C3)

C4 = "Coding For All"
C4 = C4[10]
print(C4)

#18, 19
C5 = "Python For Everyone"
C5 = C5.split()
Ac1 = ""
for C5 in C5:
  Ac1 += C5[0].upper()
print(Ac1)

C6 = "Coding For All"
C6 = C6.split()
Ac2 = ""
for C6 in C6:
    Ac2 += C6[0].upper()
print(Ac2)

#20, 21, 22
C = "Coding For All"
print(C.index("C"))
print(C.index("F"))
print(C.rfind("l"))

#23, 24, 25, 26
B = "You cannot end a sentence with because because because is a conjunction"
print(B.index("because"))
print(B.rindex("because"))
print(B.split("because"))
print(B.find("because"))

#28, 29
text = "Coding For All"
result = text.startswith("Coding")
print(result)

text = "Coding For All"
result = text.endswith("Coding")
print(result)

#30
text = " Coding For All "
result = text.strip(" ")
print(result)

#31
D = "30DaysOfPython"
t = "tirthy_day_of_python"
print(D.isidentifier())
print(t.isidentifier())

#32

#33
