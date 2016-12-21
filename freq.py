def freq(s):
    a_count={}
    for i in s:
        a_count[i]=0
    for alpha in s:
        a_count[i]+=1
    return a_count    
        
# You can avoid an extra loop like this
def freq(s):
    alpha_count = {}
    for alpha in s:
        if s in alpha_count:
            alpha_count[alpha] += 1
        else:
            alpha_count[alpha] = 1
    return alpha_count
