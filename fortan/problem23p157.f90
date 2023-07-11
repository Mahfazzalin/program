! construct a flowchart of the following series and implement it into Fortran: sum = 1 + x + x^2 + ....+ x^k
	print*, ("To calculate this series , sum = 1 + x + x^2 + ....+ x^k")
	print*, ("Enter two number.")
	print*, ("1st enter k:")
	print*, ("2nd enter x:")
	read(5, *) k, x
	sum = 0.0
	n = 0
9	sum = sum + x ** n
	n = n + 1
	if ( n .le.k ) goto 9
	write(6,20) sum
20	format(3x, 'sum :' ,f8.2)
	stop
	end
! Mahfazzalin Shawon Reza
