primes = [1, 2, 3, 5, 7, 11, 13]
# Can loop over lists
for number in primes:
    print(number)

# If you need to know the index, use enumerate()
for i, number in enumerate(primes):
    print(f'{i}: {number}')

# # Looping over a dictionary
# head_counts = {
#     "human resources": 40,
#     "marketing": 20,
#     "sales": 100,
#     "products": 300
# }
#
# for department in head_counts:
#     print(f"The {department} department has {head_counts[department]} employees")

# # for-else structure
# even = [3, 7, 9, 11, 13, 17]
# for number in even:
#     if number < 5:
#         print(f"Found {number} which is less than 5")
#         break
# else:
#     print("All numbers are greater than 5 in this list")
