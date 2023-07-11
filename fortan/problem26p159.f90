! write a program in fortran that reads values for the three sides of a triangle. calculate its perimeter and its area and output these values.
	print*, 'Enter 3 sides of triangle:'
	read*, a , b , c
	p = a + b + c
	s = p/2
	area = sqrt(s*(s - a) * (s-b) *(s-c))
	print*, 'perimeter:',p
	print*, 'Area:' , area
	stop
	end
