! Write an algorithm and draw a flowchart to find the product of the following series and implement this into Fortran : 1/2*3/4* 5/6....21/22
	print*, '1/2*3/4* 5/6....21/22'
	k = 1
	prod = 1.0
10	prod = prod * float(k)/(float(k +1))
	k = k+2
	if (k.le.21) goto 10
	print*, 'PRODUCT :', prod
	stop
	end
