! Write an algorithm and draw a flowchart to read a year find it is leep year or not.
	integer year
	print*, 'Enter a year :'
	read*, year
	if(mod(year,100) .eq. 0) then
		if(mod(year,400) .eq. 0) then
			print*, year, ' is leep year'
		else
			print*, year, 'is not leep year'
		endif
	else
		if(mod(year,4) .eq. 0) then
			print*, year, 'is leep year'
		else
			print*, year, 'is not leep year'
		endif
	endif
	stop
	end
