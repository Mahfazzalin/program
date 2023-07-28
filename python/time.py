from datetime import datetime 
import time
# while True:

def mahftime():
    dt = datetime.now()
    hour= dt.strftime("%H")
    print(hour)
    minute = dt.strftime("%M:%S")

    if int(hour) >=7 and int(hour)<= 24 :
        mahfhour = int(hour)-6
        if mahfhour>12:
            mahfhour = mahfhour-12
            ltnt="night"
        else:
            mahfhour=mahfhour
            ltnt= "light"
    else:
        mahfhour = int(hour)+24
        mahfhour = mahfhour-18
        ltnt= "night"
    
    time = str(mahfhour)+":"+ minute+" "+ltnt
    #print(hour)
    print(time)
    
    # return mahftime()

mahftime()