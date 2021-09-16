dna = "ACGTAAGTCCGAGTAATAGATAATCAGAATCGGAATCAAGAAGTCCGAAGTCCGAACGTAAG"

n = []

a = 0

ans = set()

while 1 :

    n += dna[a:a+8]

    a = a + 1

    h , x = 0 , 0 # 算有幾個 , 控制dna

    n1 = []

    while 1 :
        
        n1 += dna[x:x+8]

        x = x + 1

        if n1 == n :

            h = h + 1

        n1.clear()

        if x == len(dna) - 7 :

            break

    if h > 1 :

        ans.add( "".join(n)+" {}".format(h) )

    n.clear()

    if a == len(dna) - 7 :

        break
    
for i in ans :

    print( "".join(i) )
