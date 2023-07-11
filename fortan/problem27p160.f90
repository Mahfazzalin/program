! write an algorithm and draw a flowchart to solve the quadratic equation Ax^2 + Bx + C = 0
	print*,'Ax^2 + Bx + C = 0'
	print*, 'Enter A B C'
	read*, a , b , c
	d = b*b - 4.0*a*c
	if(d.ge.0) then
		x1 = real((-b + sqrt(d))/ (2.0*a))
		x1 = real((-b - sqrt(d))/ (2.0*a))
		print*, '1st root',x1
		print*, '2nd root',x2
	else
		p = real((-b/(2.0*a)))
		q =  real(sqrt(d)/(2.0*a))
		print*, '1st root', p, '+', q
		print*, '2nd root', p, '-', q
	endif
	stop
	end
