def gcd(a,b):
	m,n = a,b
	u1,u2 = 1,0
	v1,v2 = 0,1
	while n > 0:
		q = m/n
		r = m - (q*n)
		m,n = n,r
		u2,u1 = u1 - q*u2, u2
		v2,v1 = v1 - q*v2, v2
	print('d = ' + str(m))
	print('u = ' + str(u1))
	print('v = ' + str(v1))

gcd(7,40)