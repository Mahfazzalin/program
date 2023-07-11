!write a fortran progrram which calculates the sum with four decimal places of the following series  1/1+1/3+1/5+.....+1/25
        print*, 'calculate the sum of 1/1+1/3+1/5+.....+1/25'
        print*, 'congratulation Minhajul Abedin Naim , this is your first fortran program'
        sum = 0.0
        k = 1
 7      sum = sum + 1.0/float(k)
        k = k+1
        if(k.le.25) goto 7
        write(6, 20) sum
 20     format(5x, 'sum =', f10.4)
        stop
        end
