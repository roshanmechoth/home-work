def array(k):
     k=k+1
     for i in range (1,k):
           for j in range(1,k):
                  print('{:3}'.format(i*j)),
           print("\n")

def main():
     print"enter a number "
     a=int(raw_input())
     array(a)     

if __name__ == '__main__':
    main()
