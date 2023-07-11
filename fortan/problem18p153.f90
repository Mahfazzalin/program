!write an algorithm and draw a flowchart to find the sum of the following series and implement this into Fortran: "1 + x^2/2! + x^4/4! + .... + x^10/10!"
	integer fact
	print*, '1 + x^2/2! + x^4/4! + .... + x^10/10!'
	print*, 'Enter the value of x:'
	sum = 0.0
	k = 0
	read*, x
10	m = fact(k)
	sum = sum + x**K/float(m)
	k = k + 2
	if (k.le.10) goto 10
	print*, 'sum is :', sum
	end
	integer function fact(n)
	fact = 1
	if (n .eq. 0) goto 30
	j = 1
20	fact = fact * j
	j = j + 1
	if ( j .le. n ) goto 20
30	return
	end
