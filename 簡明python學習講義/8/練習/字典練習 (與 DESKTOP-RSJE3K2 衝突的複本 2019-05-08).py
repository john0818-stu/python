#有幾個母音

a = "To be , or not to , be , that is the question."

aeiou = {}

for i in a :

    b = i.lower()

    if i in "aeiou" :

        aeiou[i] = 1 + ( aeiou[i] if i in aeiou else 0 ) 

print(aeiou)

#字母順序
for i in sorted( aeiou ) :

    print(i,":" , aeiou[i] , end=" " , sep="" )

print()

#字母出現次數
for i in sorted( aeiou , key = lambda x : -aeiou[x]  ) :

    print(i,":" , aeiou[i] , end=" " , sep="" )

print()

#y最多次
a = sorted( aeiou , key = lambda x : -aeiou[x]  )[0]

print( a )

