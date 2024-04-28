#sample_data=[1111,1011,1010,1001,1100,1001]
binary_num=input('enter nums').split()
for num in binary_num:
    decimal=int(binary_num,2)
    if  decimal % 5 == 0:
        print(binary_num,'is divisible by 5')
    else:
        print(binary_num,'is not divisible by 5')

        
    '''binary_nums = input('Enter binary numbers separated by spaces: ').split()

for binary_num in binary_nums:
    decimal = int(binary_num, 2)
    if decimal % 5 == 0:
        print(binary_num, 'is divisible by 5')
    else:
        print(binary_num, 'is not divisible by 5')'''
