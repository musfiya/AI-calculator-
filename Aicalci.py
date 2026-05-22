import re

def ai_calculator(query):
    # Basic patterns for operations
    query = query.lower().strip()
    
    # Addition
    if "add" in query or "+" in query:
        numbers = re.findall(r'\d+', query)
        return sum(map(int, numbers))
    
    # Subtraction
    elif "subtract" in query or "-" in query:
        numbers = list(map(int, re.findall(r'\d+', query)))
        return numbers[0] - sum(numbers[1:])
    
    # Multiplication
    elif "multiply" in query or "x" in query or "*" in query:
        result = 1
        for num in map(int, re.findall(r'\d+', query)):
            result *= num
        return result
    
    # Division
    elif "divide" in query or "/" in query:
        numbers = list(map(int, re.findall(r'\d+', query)))
        try:
            return numbers[0] / numbers[1]
        except ZeroDivisionError:
            return "Error: Division by zero"
    
    else:
        return "Sorry, I couldn’t understand the query."

# Example usage
print(ai_calculator("Add 12 and 8"))       # ➝ 20
print(ai_calculator("Subtract 50 - 20"))   # ➝ 30
print(ai_calculator("Multiply 5 x 3"))     # ➝ 15
print(ai_calculator("Divide 100 / 25"))    # ➝ 4.0
