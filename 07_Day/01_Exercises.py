#1
It_Companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
print(It_Companies," - ",len(It_Companies))
#2
print("/////////////////////////////////////////////////////////////////////////////")
It_Companies.add("Twitter")
print(It_Companies)
#3
print("/////////////////////////////////////////////////////////////////////////////")
It_Companies2= {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
It_Companies2.update(["WhatsApp", "Nvidia", "AMD", "Intel", "Acer"])
print(It_Companies2)
#4
print("/////////////////////////////////////////////////////////////////////////////")
It_Companies2.remove("IBM")
print(It_Companies2)
#5
print("/////////////////////////////////////////////////////////////////////////////")
It_Companies.difference(It_Companies2)
It_Companies2.difference(It_Companies)
