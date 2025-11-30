
#!/usr/bin/env python3
print("=== PROGRAM 1: Number Processing ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
print("Program 1 completed successfully!")
