def longest_range(array):
    numbers = {x:0 for x in array}
    right = left = 0
    for number in array:
        if numbers[number] == 0:
            left_count = number - 1
            right_count = number + 1

            while left_count in array:
                numbers[left_count] = 1
                left_count -= 1
            left_count += 1

            while right_count in array:
                numbers[right_count] = 1
                right_count += 1
            right_count -= 1

            if (right-left) <= (right_count-left_count):
                right = right_count
                left = left_count
    return [right,left] and numbers

print(longest_range([11,7,3,4,2,1,0]))

