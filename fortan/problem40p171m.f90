!#/bin/gfortran
! A person deposited some amount in a saving account in a bank . Bank pays 7% interest if deposited amount is less than or equal to tk 10000. and paus 6% if the amount is greater than tk 10000. draw a flow chart and a fortran program to fimd the interest.

	real ints
	print*, 'Enter your amount'
	read*, amounts
	if(amounts.le.10000.0) then
		ints = amounts * 0.07
	else 
		ints = amounts * 0.06
	endif
	print*,'interest', ints
	stop
	end
