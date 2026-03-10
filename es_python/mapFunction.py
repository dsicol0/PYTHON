nums = [1 , 2, 3, 4]

# USING FOR LOOP
# squared = []

# for n in nums:
#     squared.append(n ** 2)
# print(squared)

squared = list(map(lambda x: x ** 2, nums))
print(squared)