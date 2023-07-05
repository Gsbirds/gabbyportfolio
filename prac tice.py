def singleNumber(nums) -> int:
    d={}
    for n in nums:
        if n in d:
            d[n]+=1
        else:
            d[n]=1

        for value in d:
            print(value)
            # print (key)
            if value>=2:
                return True
            else:
                return False
              
print(singleNumber([2,14,18,22,22]))