steps = list(map(int, input("Enter the steps taken each day (separated by spaces): ").split()))
highest = max(steps)
lowest = min(steps)
average = sum(steps) / len(steps)
sorted_steps = sorted(steps, reverse=True)

print("Highest steps:", highest)
print("Lowest steps:", lowest)
print("Average steps:", average)
print("Steps in descending order:", sorted_steps)

