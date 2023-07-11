! i will give you 1 lakh taka everyday in a month. and you will give one cent ist day , the 2nd day you give back me double. x + 2x +4x + ....+ nx
	print*, 'Enter your starting money(in cent) and days number:'
	read*, x,n
	sum = x 
	j = 1
	print*, 'day', j , 'money', sum
	k = 2 
10	sum = (sum + (2** k) * x)/100
!20	j = j + 1
	!print*, 'day', j , 'money', sum
	k = k + 2
	if(k.le.n) goto 10
	!if(j.lt.n) goto 20
	print*, 'day', n , 'money', sum
	print*, sum
	stop
	end
