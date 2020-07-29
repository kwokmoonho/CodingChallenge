# find unique sets of integer that add up to '15' from the follwing array: [4, 5, 6, 89, 23, 5, 2, 3, 5]
# input = [4, 5, 6, 89, 23, 5, 2, 3, 5]
# output =

#  [ 4, 5, 6 ],
#  [ 2, 3, 4, 6 ],
#  [ 2, 3, 5, 5 ],
#  [ 5, 5, 5 ]

def subset_sum(answer,numbers, target, partial=[]):

    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        #print("sum(%s)=%s" % (partial, target))
        answer.append(partial)
        return partial
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(answer,remaining, target, partial + [n])

user_input = [4, 5, 6, 89, 23, 5, 2, 3, 5]
# sort array
user_input.sort()
answer = []
subset_sum(answer,user_input,15)
print(answer)
res = list(set(tuple(sorted(sub)) for sub in answer))
print(res)
