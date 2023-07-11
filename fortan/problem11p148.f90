    ! write an algorithm to print the positive odd numbers less than 100
    program odd
    k = 1
5   print *, k
    k = k+2
    if(k.le.100) goto 5
    stop
    end program
