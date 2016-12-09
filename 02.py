print"enter a number "
a=int(raw_input())
def array(k):
     k=k+1
     for i in range (1,k):
           for j in range(1,k):
                  print('{:2}'.format(i*j)),
           print("\n")
array(a)     
