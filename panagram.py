print "Enter a string "
x=raw_input()
def panagram(x):
    s=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in s:
        if i not in x:
            return False
        
    return True
true=panagram(x)
print  true        


