def prime(n):
    #generate prime numbers from 0 to n with asymptotic analysis

    if n < 0: #list cant be less than zero
        return None 
    elif n == 2: #if list is two then two is the only prime between 0-2
        return [2]
    elif n ==1 or n == 0: #no prime numbers in 0-1 and 0-0
        return []    

	#checking input type
    if isinstance(n, str):
        raise TypeError
    if isinstance(n, float):
        raise TypeError
    if isinstance(n, list):
        raise TypeError
        
    try:
        prime_nums = [2] # initialize with 2 since n is greater than 2
        for i in range(3,n+1): #start from 3, avoid repeating 2
            factor_count=0
            for x in range (2,i):
                # start from 2 onwards
                if i % x == 0:
                    factor_count+=1
                    # inner loop breaking..
                    break # i is not a prime number 
            if factor_count==0:
                prime_nums.append(i)
    except TypeError as e:
        # n is not an integer
        raise(e)
    except NameError as e:
        # undefined variable
        raise(e)
        
    return prime_nums
    
