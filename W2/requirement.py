# %%
# 1
def calculate(min, max):
    print(sum([i for i in range(min, max+1)]))


# 請用你的程式補完這個函式的區塊
calculate(1, 3)  # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8)  # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

# %%
# 2


def avg(data):
    print(sum(employee["salary"]
          for employee in data["employees"])/data["count"])


# 請用你的程式補完這個函式的區塊
avg({
    "count": 3,
    "employees": [
        {
            "name": "John",
            "salary": 30000
        },
        {
            "name": "Bob",
            "salary": 60000
        },
        {
            "name": "Jenny",
            "salary": 50000
        }
    ]
})  # 呼叫 avg 函式

# %%
# 3

# Time: O(n^2)
# Space: O(1)


def maxProduct(nums):
    max = float('-inf')
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            product = nums[i] * nums[j]
            if max < product:
                max = product
    print(max)


maxProduct([5, -20, 2, 6])  # 得到 120

# %%
# 3

# Time: O(n)
# Space: O(1)


def maxProduct(nums):
	max = float('-inf')
	secMax = float('-inf')
	ans = float('-inf')
	for i in nums:
		if i > max:
			secMax = max
			max = i
		elif i > secMax:
			secMax = i
	min = float('inf')
	secMin = float('inf')
	for i in nums:
		if i < min:
			secMin = min
			min = i
		elif i < secMin:
			secMin = i
	ans =  max * secMax if max * secMax > min * secMin else min * secMin
	print('ans:', repr(ans).rjust(4), ',nums:' ,repr(nums).rjust(4))


# 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6])  # 得到 120
maxProduct([10, -20, 0, 3])  # 得到 30
maxProduct([-1, 2])  # 得到 -2
maxProduct([-1, 0, 2])  # 得到 0
maxProduct([-1, -2, 0])  # 得到 2
maxProduct([5, -20, 2, 6])  # 得到 30
maxProduct([5, 0, -2, -1])  # 得到 2
maxProduct([-5, 0, -2, -1])  # 得到 10
maxProduct([-1, 0, 2, -1])  # 得到 1
maxProduct([-0, -3, -2, -1])  # 得到 6

# %%
# 4


def twoSum(nums, target):
    history = {}
    for count, item in enumerate(nums):
        remaining = target - item
        if remaining in history:
            return [history[remaining], count]
        else:
            history[item] = count


# your code here
result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9

# %%
# 5

# Time: O(n)
# Space: O(1)


def maxZeros(nums):
    max_count = 0
    count = 0
    for num in nums:
        if num == 0:
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0
    print(max_count)


maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # 得到 4
maxZeros([1, 1, 1, 1, 1])  # 得到 0
maxZeros([0, 0, 0, 1, 1])  # 得到 3
