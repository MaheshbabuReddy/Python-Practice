def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        sequence.append(n)
    return sequence

def steps_to_reach_one(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        steps += 1
    return steps

def largest_number_in_sequence(sequence):
    return max(sequence)

def visualize_sequence(sequence):
    print("Collatz Sequence:")
    for num in sequence:
        print(num, end=" , ")

# Input from the user
n = int(input("Enter a positive integer: "))

sequence = collatz_sequence(n)
steps = steps_to_reach_one(n)
largest_num = largest_number_in_sequence(sequence)

print("Sequence:", sequence)
print("Number of steps:", steps)
print("Largest number in the sequence:", largest_num)

visualize_sequence(sequence)