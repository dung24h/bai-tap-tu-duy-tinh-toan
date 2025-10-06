import sys
n=int(input())
if n==0:
	print('False')
	sys.exit()
if n&(n-1)==0:
	print('True')
else:
	print('False')