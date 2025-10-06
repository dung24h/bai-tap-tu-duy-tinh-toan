a=float(input())
tmp=int(a)

if(a<0):
	b=(-a)*10
else: b=a*10
du=b%10

if(du==0): print(tmp, tmp, tmp)
else:
	
	if (a>0): print(int(a+1))
	else: print(int(a-1))
	print(int(a))
	if(du>=5): 
		if(a>0):print(int(a+1))
		else: print(int(a-1))
	else: print(int(a))