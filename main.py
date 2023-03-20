import re
import webbrowser

# Define the regular expression pattern for the phone number
pattern = r'^(\+1)?\d{10}$|^\(\d{3}\)\s*\d{3}-\d{4}$'

# Get the user input for the phone number
phone_number = input('Please enter your phone number: ')

part1 = phone_number[:3]
part2 = phone_number[3:6]
part3 = phone_number[6:]
#Open google
query = f'''intext:"{phone_number}" OR intext:"+1{phone_number}" OR intext:"1{phone_number}" OR intext:"({part1}) {part2}-{part3}"'''
print(query)
webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")

# Validate number
if re.match(pattern, phone_number):
    print('Phone number is valid')
else:
    print('Invalid phone number format. Please enter in the format (area code) rest of number or +1number or 1number')
