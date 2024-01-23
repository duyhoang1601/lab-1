def print_sum_of_current_and_previous(num):
    previous_num = num[0]

    for current_num in num[1:]:
        current_sum = current_num + previous_num
        
        print(f"Sum of {current_num} and {previous_num}: {current_sum}")

        previous_num = current_num

numbers = list(range(1, 11))

print_sum_of_current_and_previous(numbers)
