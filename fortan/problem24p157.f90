! write a flowchart for choosing the largest of three distinct numbers x,y,z
	
	real large
	print*, 'Enter 3 number'
	read(5 , *) x, y, z
	large = x
	if( large .le. y ) large = y
	if( large .le. y ) large = y
	write(6,10) large
10	format(2x,'largest number =' ,f8.2)
	stop
	end
	
