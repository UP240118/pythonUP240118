#1
empty_list = list()
print(len(empty_list))

#2, 3, 4
Autos = ["Audi", "BMW", "Ford", "Nissan", "Toyota"]
print(len(Autos))
Fa = Autos[0]
Sa = Autos[2]
La = Autos[4]
print(Fa,",",Sa,",",La)
print("/////////////////////////////////////////////////////////////////////////////////////////")

#5. 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 
Mixed_Data_Types = ["Axel Yael Mtz Mtz", "18 Años", "1.90 Mts.", "Soltero", "Las Cumbres"]
It_Companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(Mixed_Data_Types)
print(It_Companies, len(It_Companies), "Compañias")
Fc = It_Companies[0]
Sc = It_Companies[3]
Lc = It_Companies[6]
print(Fc,",",Sc,",",Lc)

It_Companies2 = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
Ic = len(It_Companies2) - 7
It_Companies2[Ic] = "Lenovo"
print(It_Companies2)

It_Companies.append("Arduino")
print(It_Companies)

It_Companies3 = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
It_Companies3.insert(4, "Acer")
print(It_Companies3)

U = It_Companies[1].upper()
print(U)

Exist = "Microsoft" in It_Companies
print(Exist) 

It_Companies4 = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"] 
It_Companies4.sort()
print(It_Companies4)

It_Companies5 = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"] 
It_Companies5.reverse()
print(It_Companies5)
print("/////////////////////////////////////////////////////////////////////////////////////////")

#21, 22, 23, 24
It_Companies6 = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"] 
del It_Companies6[0]
print(It_Companies6)

It_Companies7 = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"] 
del It_Companies7[2]
print(It_Companies7)

It_Companies8 = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"] 
del It_Companies8[6]
print(It_Companies8)

It_Companies8.clear()
print(It_Companies8)
print("/////////////////////////////////////////////////////////////////////////////////////////")

#26, 27
front_end = ["HTML", "CSS", "JS", "react", "Redux"]
back_end = ["Node", "Express", "MongoDB"]

full_stack = front_end + back_end
print(full_stack)
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)