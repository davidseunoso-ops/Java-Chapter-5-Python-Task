text5_4 = """
a) Error: The semicolon after the while header causes an infinite loop, and there's a missing left brace.
Correction: Replace the semicolon by a {, or remove both the ; and the }.

b) Error: Using a floating-point number to control a for statement may not work, because floating-point numbers are represented only approximately by most computers.
Correction: Use an integer, and perform the proper calculation to get the values you desire.

c) Error: The missing code is the break statement in the statements for the first case.
Correction: Add a break statement at the end of the statements for the first case.

d) Error: An improper relational operator is used in the while's continuation condition.
Correction: Use <= rather than <, or change 10 to 11.
"""

print(text5_4)


text5_5_to_5_10 = """
5.5
1. Initialization
2. Controlled condition
3. Increment
4. Statement


5.6
Both loops are used for iteration. However, the while loop is more effective when we have no idea of the number of times a process is supposed to run. Therefore, it uses a sentinel, while a for loop is used when we know the number of times an event is supposed to occur, which is often referred to as counter-controlled.


5.7
In this instance, a while is more effective since we already understand that a do-while runs the body at least once before checking the condition.


5.8
The break statement ends a loop or iteration, while continue skips the remaining part of the current iteration and moves to the next iteration.


5.9
a) Instead of i+, it should be i++ for the increment.

b)


c) I think that the increment should be i-- since we are trying to do a countdown from 19 to 1.

d) The question asks for numbers in the range 1–50, but the condition here gives us numbers from 1–51. Therefore, the condition should be corrected.


5.10
It prints * four times and # five times.
"""

print(text5_5_to_5_10)


