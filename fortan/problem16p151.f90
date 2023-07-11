! writ an algorithm and draw a flowchart to find the sum of the following series and implement this into Fortran : 1 + 3 + 3^2 + 3^3 + ...... + 3^n 
	integer sum
	print*, '1 + 3 + 3^2 + 3^3 + ...... + 3^n '
	print*, 'To calculate the series ENTER n :'
	k = 0
	sum = 0
	read *, n
10  	sum = sum + 3**k
	k = k + 1
	if(k .le. n) goto 10
	print *, 'sum :',sum
	stop
	end
