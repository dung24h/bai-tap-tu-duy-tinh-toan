def TB(a, b, c, d, x, y):
	tb=((a+b+c)+(d+x)*2+y*3)/10
	return tb

a1, a2, a3, a4, a5, a6=map(int, input().split())
diem=TB(a1, a2, a3, a4, a5, a6)
print('%.1f'%diem)	