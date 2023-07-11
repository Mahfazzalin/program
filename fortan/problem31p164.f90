!write an algorithm and a fortran program. which reads integer N and determines whether N is prime or not.
	print*,'Enter an integer number'
	read*, n 
	if(n.le.1) goto 20
	if(n.eq.2) goto 15
	j = n/2
	k = 2
10	if(n.eq.(n/k)*k) goto 20
	k = k + 1
	if(k.le.j) goto 10
15	print*,n, 'is a prime number'
	goto 25
20	print*,n, 'is not a prime number'
25	stop
	end
