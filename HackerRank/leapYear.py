def is_leap(year):
    leap = False    
    # Write your logic here
    
    if 1900 <= year <= 10**5:
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    leap=True
                else:
                    leap=False
            else:
                leap = True
        else:
          leap = False
          
    else:
        print('The year must be from 1900 to 10^5')        
    
    return leap

year = int(input('Write a year...'))
print(is_leap(year))