import random

def sort(nums, nums2):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

    for k in range(len(nums2)-1, 0, -1):
        for l in range(k):
            if nums2[l] > nums2[l+1]:
                temp2 = nums2[l]
                nums2[l] = nums2[l+1]
                nums2[l+1] = temp2


numserd = [1, 7, 7, 1, 5, 2, 7, 2, 8, 3, 8]
print("The first sample list 👨‍💻☝")
print("""
<!--------------!>
""")
print(numserd)
# nums2 = [345, 345, 35, 354, 1, 3, 87, 243, 65, 234, 65]
# print(nums2)
p = []

for i in range(100):
    i = random.randint(0, 1000)
    p.append(i)
numserd.extend(p)
random.shuffle(numserd)
print(numserd)
print("<!--------------!>")
print("""

This is before ☝
This is after 👇

""")
random.shuffle(p)
random.shuffle(numserd)
# numserd.extend(p)k
sort(numserd, p)
print(numserd)