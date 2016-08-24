def divisor_count(num1):
    count=0
    for num in range(1,num1+1):
        if num1%num==0:
            count=count+1
        else:
            continue
    return count
divisor_count(40320)



            
