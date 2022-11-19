# prompt = "if you tell us who are you? we can personalize the messages you see."
# prompt += "\nWhat is youre first name?\n"

# active = True

# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
        
        
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
