vards=input("Ievadi savu vārdu nominatīvā locijumā (Kas?):")

vards=vards.lower() 
# funkcija .lower()- visus burtus kovertē par mazajiem burtiem.

vards=vards.capitalize()
# funkcija .capitalize()- simbolu virknē pirmo burtu konvertē par lielo.

UzminiVardu1="saies"
minejums=None

while UzminiVardu1!=minejums:
    # != nav vienāds.
    minejums=input(f"Uzmini vārdu - {UzminiVardu1[2]+UzminiVardu1[0]+UzminiVardu1[4]+UzminiVardu1[1]+UzminiVardu1[3]}: ")

print("Pareizi!")

UzminiVardu2="saule"

while True:
    minejums=input(f"Uzmini vārdu - {UzminiVardu2[2]+UzminiVardu2[0]+UzminiVardu2[4]+UzminiVardu2[1]+UzminiVardu2[3]}: ")
    if UzminiVardu2==minejums:
        print("Pareizi!")
        break

UzminiVardu3="skola"

reizes=2

for i in range(3):
    minejums=input(f"Uzmini vārdu - {UzminiVardu3[2]+UzminiVardu3[0]+UzminiVardu3[4]+UzminiVardu3[1]+UzminiVardu3[3]}: ")
    if UzminiVardu3==minejums:
        print("Pareizi!")
        break
    else:
        if reizes>0:
            print(f"Neuzminēji. Atlikušas {reizes} reizes.")
            reizes-=1
        else:
            print(f"Neuzmineji, pareizais vārds bija <<{UzminiVardu3}>>😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔😔")
        
print("Spēles beigas!")

