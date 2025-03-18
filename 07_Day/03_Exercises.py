# 1
age_list = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age_list)     

if len(age_set) == len(age_list):
    print("Ambos son Iguales")
elif len(age_set) > len(age_list):
    print("El set es mas grande")
else:
    print("La lista es mas grande")
# 2
# 3
sentence = "I am a teacher and I love to inspire and teach people"
words = set(sentence.split())
print(f"Las palabras unicas son - {len(words)}")