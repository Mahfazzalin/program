!#/bin/gfortran
! write an algorithm to determine if an integer N>2 is a prime number. if N is not a prime , print N and all its divisors. "Implement this into FORTRAN to find all prime numbers < 500."
	i = 2 
	print*,'All prime number between 1 to 500'
	print*, i 
	n = 3
7	j = n/2
	k = 2 
10	if (n.eq.(n/k)*k) goto 20
	k = k+1
	if( k.le.j) goto 10
	print*, n
20	n = n+2
	if(n.le.500) goto 7
	print*,'done'
	stop
	end
