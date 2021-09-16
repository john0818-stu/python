dna = "ACGTAAGTCCGAGTAATAGATAATCAGAATCGGAATCAAGAAGTCCGAAGTCCGAACGTAAG"

ans = {}

for d in range( 8 , len(dna)-1 ) :

    n = []

    a = 0

    while 1 :

        n += dna[a:a + d]

        a = a + 1
    
        h , x = 0 , 0 # 算有幾個 , 控制dna

        n1 = []

        while 1 :
        
            n1 += dna[x:x+d]

            x = x + 1

            if n1 == n :

                h = h + 1

            n1.clear()

            if x == len(dna) - d - 1 :

                break

        if h > 1 :

            ans["".join(n)] = h

        n.clear()

        if a == len(dna) - d - 1 :

            break
        
a = sorted( ans.items() , key = lambda x : -len(x[0]) )[0]

print( a[0] , ans[a[0]])
