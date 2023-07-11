!#/bin/gfortran
! write an algorithm and a fortran program to read a five- digit number and to compute the sum of the digits of the number.
	integer sum
	read*, n
	print*, 'enter your number.) 
	print*,'compute the sum of the digits of the number.'
	sum = 0 
10	sum = sum + mod(n,10)
	n = n/10
	if ( n.gt.0) goto 10
	print*, sum
	stop
	end
