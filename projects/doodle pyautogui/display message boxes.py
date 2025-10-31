import pyautogui

# Alert box
pyautogui.alert('This is an alert box.')

# Confirmation box
response = pyautogui.confirm('Shall I proceed?')
print("User selected:", response)

# Confirmation box with custom buttons
choice = pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
print("User chose:", choice)

# Input prompt
name = pyautogui.prompt('What is your name?')
print("Name entered:", name)

# Password input (hidden text)
password = pyautogui.password('Enter password (text will be hidden)')
print("Password entered:", password)
