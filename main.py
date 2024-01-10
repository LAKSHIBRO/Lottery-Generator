import time

def random_number(minimum, maximum, existing_numbers):
    # Get the current time in microseconds
    now = time.time()
    # Extract the microseconds part (use modulus to wrap around)
    microseconds = int((now - int(now)) * 1e6)
    # Scale the microseconds part to the desired range
    scale = maximum - minimum + 1
    random_num = minimum + (microseconds % scale)
    # Ensure the number is unique
    while random_num in existing_numbers:
        microseconds += 1
        random_num = minimum + (microseconds % scale)
    return random_num

# Generate a set of unique random numbers
lottery_numbers = set()
for _ in range(6):  # Change this to generate more or fewer numbers
    lottery_numbers.add(random_number(1, 1000, lottery_numbers))

print(sorted(list(lottery_numbers)))
