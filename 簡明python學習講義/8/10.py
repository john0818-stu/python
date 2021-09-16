c = "一二三四五"

ans = [ [ "  " for j in range(5) ] for i in range(8) ]

with open ('schedule.dat' , 'r' , encoding='utf8') as infile :
    
    for line in infile :

        line = line.strip()

        print( line )

        if len(line) :

            x0 , *x1 = line.split()

            for s in x1 :

                s0 , *s1 = s.split(":")

                if s1[0].isdigit() :

                    for i in "".join(s1) :

                        ans[int(i)-1][c.index(s0)] = x0[0]

                else :

                    g , a = int(s1[0][0]) , abs(eval(s1[0]))+1

                    for i in range( g , g + a ):

                        ans[i-1][c.index(s0)] = x0[0]
       
print( "  |" , " ".join(c) + "\n" + "-"*( (len(c)+1)*3 ) )

for i in range(9) :

    if i == 9//2 :

        print( "-"*( (len(c)+1)*3 ) )

    else :
        
        j = i if i > 9//2 else i + 1

        print( j , "| " + " ".join( ans[j-1] )  )
