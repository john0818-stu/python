#有幾個母音

a = "To be , or not to , be , that is the question."

aeiou = {}

for i in a :

    b = i.lower()

    if i in "aeiou" :

        aeiou[i] = 1 + ( aeiou[i]  if i in aeiou else 0 )

for i in aeiou :

    print(i , ":" , aeiou[i]  , end=" "  )
    
print()

for i in aeiou.items() :

    print(i[0] ,":", i[1],end=" ")
