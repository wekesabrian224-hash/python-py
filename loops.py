goal_steps = 10000

while True:  # Infinite loop (user exits with 'q' or 'quit')
    user_input = input("Enter your current step count (or 'q' to quit): ")

    if user_input === "q" or user_input === "quit":
        break

    current_steps = int(user_input)

    if current_steps < 0:
        print("Invalid input. Please enter a non-negative step count.")
        continue  # Skip to the next iteration if input is invalid

    if current_steps >= goal_steps:
        print("Congratulations! You reached your daily step goal!")
        break  # Exit the loop if goal is reached

    print("Keep going! You're almost there!")

    # Task 1: Define Variables
savings_goal = 1000  # Example savings goal
current_savings = float(input("Enter your starting savings amount: $"))

# Task 2: Implement a While Loop
while current_savings < savings_goal:
    # Task 3: Integrate Input and Outcome
    print(f"Keep saving! You're ${savings_goal - current_savings:.2f} away from your goal.")
    additional_savings = float(input("Enter the amount you've saved since last check: $"))
    current_savings += additional_savings

# Task 4: Display Results
print("Congratulations! You've reached your savings goal!")

# Step 4: Test and Refine
# (Run the program with different inputs to verify it works as expected)

# Step 5: Document and Maintain
# Comments explaining the while loop:
# The while loop continues as long as current_savings is less than savings_goal.
# In each iteration, it calculates and displays the remaining amount to save,
# prompts the user for additional savings, and updates the current_savings.
# The loop exits when current_savings is no longer less than savings_goal.

# Potential future enhancements:
# - Allow user to set their own savings goal
# - Track multiple savings goals
# - Add a feature to visualize savings progress

# Version control: Use git to track changes over time
# Example commands:
# git init
# git add savings_tracker.py
# git commit -m "Initial implementation of Savings Goal Tracker"

# Explanation of the Solution:

# 1. Variable Initialization:
#    - We set savings_goal to 1000 as an example target.
#    - We use input() to get the user's starting savings amount and convert it to a float.

# 2. While Loop Implementation:
#    - The condition 'current_savings < savings_goal' ensures the loop continues as long as
#      the user hasn't reached their goal.
#    - This is the core of our program, allowing repeated checks and updates.

# 3. Inside the While Loop:
#    - We calculate and display how much more the user needs to save.
#    - The f-string allows us to format the output, showing the amount to two decimal places.
#    - We prompt the user for their additional savings since the last check.
#    - We update current_savings by adding the additional amount.
#    - This process repeats with each loop iteration.

# 4. Loop Termination:
#    - The loop ends when current_savings is no longer less than savings_goal.
#    - This occurs when the user has met or exceeded their savings target.

# 5. Final Output:
#    - Once the loop ends, we print a congratulatory message.

# This solution demonstrates key aspects of while loops:
# - Setting up a condition (current_savings < savings_goal)
# - Repeatedly executing code while the condition is true
# - Updating variables that affect the loop condition (current_savings)
# - Automatically terminating when the condition becomes false
