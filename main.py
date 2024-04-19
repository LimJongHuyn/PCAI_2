def check_available():
        return 'It works!'

def split_odd(nums=[1,2,3,4]):
    odds=[]
    evens=[]
    for i in nums:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    return (odds, evens)


if __name__=='__main__':
        # print(check_available())
        print(split_odd([1,2,3,4,5,6,7,8,9,1,2,3,4,56,7,8,9,84,95,6,1]))
