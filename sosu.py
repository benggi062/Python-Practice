# number=int(input())
# button=False
# if number ==2:
#     print("입력 받은 숫자는 소수 입니다.")

# for i in range(2,number):
#     button=False
#     if number % i == 0:
#         print("입력 받은 숫자는 소수가 아닙니다.")
#     button=True

# if button:
#     print("입력 받은 숫자는 소수 입니다.")

        
nums=list(map(int,input().split()))
list_num=0
for i in nums:
    max_price=max(nums)
    if nums[list_num]>nums[list_num+1]:
        nums.remove(i)

    list_num+=1
print(max(nums)-min(nums))

    
    
    




        
       


