import re

a = 'python'

a_search = re.search( r'pyt' , a )
print( a_search )
print( a_search.group() )
print( a_search.span() )
print( a_search.start() )
print( a_search.end() )
print()

"""

[a-z] a到z
[^a-z] 不含a到z
.     任意字

+     前一個字可以出現 1 次以上
*     前一個字可以出現 0 次以上
?     前一個字可以出現 0 次或 1 次
{m,n}   前一個字可以出現 m 到 n 次


^     必須以後面字為開頭 (^pyt)
$     必須以前面字為結尾 (on$)

\     後面符號以 正常 符號處理 ( r"ui+yui" , \+ )
\s    空格
\n    換行

"""


b = "Jan 1987"
b_search = re.search( r'([A-Za-z]+)\s([0-9]+)' , b )
print( b_search )
print( b_search.group() )
print( b_search.groups() )
print( re.split(r"[J18]",b) )
