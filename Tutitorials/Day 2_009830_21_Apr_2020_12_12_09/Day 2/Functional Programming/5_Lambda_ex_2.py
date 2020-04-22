#lambda example
d = lambda p: p * 2 
t = lambda p: p * 3 


x = 2 
x = d(x)     #x=4  function call pointing to that anonymous fun

x = t(x)     #x=12
x = d(x)     #24
print (x) 

