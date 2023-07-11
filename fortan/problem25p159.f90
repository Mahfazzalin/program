! write a flowchart to find the smallest of a set of twenty numbers.

!algorithm

! define array a(20)
! read a 
!let small = a(1)
! do for k = 2 to 20
! 	if (small > a(k)) small = a(k)
!	enddo
!print the value of small 
!stop


!fortran program

	dimension a(20)
	write(6,10)
10	format(2x, 'Enter 20 number :' ,f8.2)
	read*, (a(i), i = 1,20)
	small = a(1)
	do 15 k = 2,20
	if(small > a(k)) then
	small = a(k)
	endif
15	continue
	
	write(6, 20) small
20	format(2x, 'smallest number :', f8.2)
	end
