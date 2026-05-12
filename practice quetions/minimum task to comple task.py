def minimumEffort(tasks):
    # Sort by (minimum - actual) in descending order
    tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

    energy = 0   # Minimum initial energy required
    current = 0  # Current available energy

    for actual, minimum in tasks:
        # If current energy is less than minimum required
        if current < minimum:
            energy += (minimum - current)
            current = minimum

        # Complete the task
        current -= actual

    return energy


# Input number of tasks
n = int(input("Enter number of tasks: "))

tasks = []

# Input each task
print("Enter actual and minimum energy for each task:")
for i in range(n):
    actual, minimum = map(int, input().split())
    tasks.append([actual, minimum])

# Output result
print("Minimum initial energy required:", minimumEffort(tasks))
