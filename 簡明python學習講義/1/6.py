n = int ( input ( "> " ) )

k = n + 1 

for j in range (n):
    
    print( j+1 , end=" ")
    
print()

for j in range (n-1 , 1 , -1 ):
    
    print( ( j + 3 * ( n-1 ) ) % 10 , " "*(2*n-3) , k%10 , sep="")
    
    k = k + 1 
    
for j in range( n , 0 , -1  ):
    
    print( (j + k - 1)%10 , end=" " )

print()


ans = [[" "]*n for i in range(n)]

dr = [-1,0,1,0]

r , c = 0 , 0

dc = [0,1,0,-1]

d = 0

for i in range( 2*n + 2*(n-2) ) :
    
    ans[r][c] = str((i+1)%10)

    if (r == 0 and c == 0) or (r==0 and c == n - 1 ) or (r == n - 1 and c == 0) or (r == n - 1 and c == n - 1):

        d += 1

    r += dr[d%4]
    c += dc[d%4]

    

            
for i in ans :
    print( " ".join(i) )
