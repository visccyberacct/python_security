#! /use/bin/env python3

# Assign `employee_id` to a four digit number as an initial value
employee_id = 4186

# Display the data type of `employee_id`
print(type(employee_id))

# Reassign `employee_id` to the same value but in the form of a string
employee_id = str(employee_id)

# Display the data type of `employee_id` now
print(type(employee_id))

# Assign `employee_id` to a four digit number as an initial value
employee_id = 4186

# Reassign `employee_id` to the same value but in the form of a string
employee_id = str(employee_id)

# Conditional statement that displays a message if the length of `employee_id` is less than five digits
if len(employee_id) != 5:
    print("This employee ID has less than five digits. It does not meet length requirements.")

# Assign `employee_id` to a four digit number as an initial value
employee_id = 4186

# Reassign `employee_id` to the same value but in the form of a string
employee_id = str(employee_id)

# Display the `employee_id` as it currently stands
print(employee_id)

# Conditional statement that updates the `employee_id` if its length is less than 5 digits
if len(employee_id) < 5:
    employee_id = 'E' + employee_id
    
# Display the `employee_id` after the update
print(employee_id)

# Assign `device_id` to a string that contains alphanumeric characters
device_id = "r262c36"

# Extract the fourth character in `device_id` and display it
print(device_id[3])

# Assign `device_id` to a string that contains alphanumeric characters
device_id = "r262c36"

# Extract the first through the third characters in `device_id` and display the result
print(device_id[0:3])

# Assign `url` to a specific URL
url = "https://exampleURL1.com"

# Extract the protocol of `url` along with the syntax following it, display the result
print(url[:8])

# Assign `url` to a specific URL
url = "https://exampleURL1.com"

# Display the index where the domain extension ".com" is located in `url`
print(url.index('.com'))

# Assign `url` to a specific URL
url = "https://exampleURL1.com"

# Assign `ind` to the output of applying `.index()` to `url` in order to extract the starting index of ".com" in `url` 
ind = url.index('.com')

# Assign `url` to a specific URL
url = "https://exampleURL1.com"

# Assign `ind` to the output of applying `.index()` to `url` in order to extract the starting index of ".com" in `url` 
ind = url.index(".com")

# Extract the website name in `url` and display it
print(url[8:ind])
    