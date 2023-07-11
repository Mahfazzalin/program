! Write a flowchart to print how many prime numbers between M and N. where M<N
	integer p
	p = 0 
	print*, 'Enter two integer number where 1st number is greater than 2nd.'
	
	read*, m,n
	if(m.eq.1) then
	m = m + 1
	end if
	if(m.eq.2) then
	p = p + 1
	m = m + 1
	endif
	if(m.gt.2) then
5	j = m/2
	k = 2
10	if(m.eq.((m/k)*k)) goto 20
	k = k + 1
	if(k.le.j) goto 10
	p = p + 1
20	m = m + 1
	if(m.lt.n) goto 5
	endif 
30	print*, 'number of prime numbers =', p
	stop
	end
