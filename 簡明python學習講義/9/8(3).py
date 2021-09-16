from sys import *

X,M,BIG,A=4,range(10),99999,range(4)

so=lambda a,b: (len(filter(lambda i:a[i]==b[i],A)),
                
      len([i for i in A for j in A if i!=j and a[i]==b[j]]))

def fd(rm,sc,N,a,b):
    
      if len(rm) in (1,5040): return [100-N,rm[0]]
      
      if not (rm and N):return [len(rm)*BIG,[]]
      
      m,r,n=b,[],a
      for i in rm:
         for j in sc:
              n=max(fd(filter(lambda x:so(x,i)==j,rm),sc,N-1,n,b)[0],n)
              if n>=b:break
         (m,r,n)=min((n,i,a),(m,r,a))
         if m<=a:return [m,r]
      return [m,r]
sc=[(x,y) for x in A for y in A+[X] if x+y<=X and (x,y)!=(X-1,1)]
g=reduce(lambda x,y:[a+[i] for a in x for i in M if i not in a],A,[[]])
K,a,s=0,[],[int(argv[1][i]) for i in A]
while a!=s: #go guess
      [n,a,K]=fd(g,sc,6-K,100,BIG)+[K+1]
      g=filter(lambda x:so(a,s)==so(a,x),g[:])
      print( a,so(a,s) )
