speletajs=input("Ievadi savu vārdu: ")

speletajs=speletajs.lower()
# komanda "mainīgā nosaukums.lower ()" - Lielos burtus konvertē par mazajiem.

speletajs=speletajs.capitalize()
# komanda "mainīgā nosaukums. capitalize()" - Simbolu virknē birmo burtu konvertē par lielo burtu.
print(speletajs)


vards1="spindzele"

minejums=input(f"uzmini vārdu - {vards1[0]} _ _ {vards1[3]} _ _ {vards1[6]}{vards1[7]}{vards1[8]}: ")

#metode mainīgaijs[burts kārtas skaitlis] un simbolu virknes skaitlis sākas 0.

minejums=minejums.lower()

if vards1==minejums:
    print("Uzminēji!")
else:
    print("Neuzminēji!")
print("Spēles beigas")
                                                                                            