# Given a list of numbers, print the average

nums = [50, 30, 101, 6]
sum = 0
size = len(nums)
for n in nums:
	sum += n
print(sum / size)
