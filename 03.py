print"Enter a number"
a=int(raw_input())
def fizzbizz(num):
     for i in range(1,num+1):
            if i%15==0:
                         print("fizzBizz")
            elif i%3==0:
                         print("fizz")
            elif i%5==0:
                         print("bizz")
            else:
                         print(i)
fizzbizz(a)
