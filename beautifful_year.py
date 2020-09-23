a = input()
b = int(a)
b=b+1
 
 
while True:
    w= (b/1000)
    w = int(w)
 
    x = (b/100)%10
    x = int(x)
 
 
    y = b/10%10
    y = int(y)
 
    z = b%10
    z = int(z)
 
    if w !=x and w!=y and w!=z and x!=y and x!=z and y!=z:
        print(b)
        break
    else:
        b = b+1
