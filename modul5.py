import os
os.system('cls')
#1
'''my_list= ["Simon", "Victor", "Eric"]
for i in range(10):
    print(my_list)'''
#2
'''mina_namn= ["Simon", "Johan", "Victor"]
mina_namn[0]="Anne onym"

for i in mina_namn:
    print(i)'''
#3
'''my_list= ["Simon", "Victor", "Johan"]

my_list.append("viktor")

for i in my_list:
    print(i)'''
#4
'''my_list=["Simon", "Victor", "Johan"]

print(len(my_list))'''

#5
'''my_list=["Simon", "Victor", "Johan"]

my_list.pop(2)

print(my_list)'''

#6 & 7
'''my_list = []
while True:
    name=input("Skriv in ett namn('avsluta' för att avsluta och 'ta bort' för att ta bort) ")
    upper_name= name.upper()
    if upper_name =="AVSLUTA":
        exit()
    elif upper_name =="TA BORT":
        number = input("skriv in vilket namnet ligger på ")
        my_list.pop(int(number)-1)
    else: 
        my_list.append(name)

        print(my_list)'''

#8 
my_library = [{
                "brand": "Mercedes benz",
                "model": "G-wagon",
                "year": 2021, 
                "color": "Mattsvart"
              },
              {
                "brand": "Volkswagen",
                "model": "XL1",
                "year": 2015,
                "color": "Grå"
                },
                {
                "brand": "Peel",
                "model": "P-50",
                "year": "1962",
                "color": "Röd"
                }, 
                {
                "brand": "Ligier",
                "model": "js50",
                "year": "2019",
                "color": "Vit"
                }
                ]

#print(f"Min favorit bil är {my_library.} {my_library[0]} årsmodellen {my_library[0]}, och min favorit färg är {my_library[0]}")

my_car = my_library[1]


for i in my_library:
    print(f"{i['brand']} {i['model']} {i['year']} {i['color']}\n")

# print(
#     f"Min favorit bil är en {my_car['brand']} modell {my_car['model']} årsmodell {my_car['year']} färg {my_car['color']}\n")

# print(
#     f"Min andra favorit bil är en {my_car2['brand']} modell {my_car2['model']} årsmodell {my_car2['year']} med färgen {my_car2['color']}\n"
# )

# print(
#     f"Min andra favorit bil är en {my_car3['brand']} modell {my_car3['model']} årsmodell {my_car3['year']} med färgen {my_car3['color']}\n"
# )

# print(
#     f"Min andra favorit bil är en {my_car0['brand']} modell {my_car0['model']} årsmodell {my_car0['year']} med färgen {my_car0['color']}\n"
# )

