alp={}
s=input("Please enter a string :")
def frequency(s):
 for i in s:
   c=0
   for k in s:
       if i==k:
          c=c+1
          alp[i]=c
 for w in sorted(alp, key = alp.get, \
                reverse = True):
    print(w,"=","0"+str(alp[w]),end=" ")        
   frequency(s)
