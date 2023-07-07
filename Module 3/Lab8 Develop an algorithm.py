#!/usr/bin/env python3

# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]

# Display the contents of `approved_users`
print(approved_users)

# Diplay the contents of `approved_devices`
print(approved_devices)

# Assign `new_user` to the username of a new approved user
new_user = "gesparza"

# Assign `new_device` to the device ID of the new approved user
new_device = "3rcv4w6"

# Add that user's username and device ID to `approved_users` and `approved_devices` respectively
approved_users.append(new_user)
approved_devices.append(new_device)

# Display the contents of `approved_users`
print(approved_users)

# Diplay the contents of `approved_devices`
print(approved_devices)

# Assign `removed_user` to the username of the employee who has left the team
removed_user = "tshah"

# Assign `removed_device` to the device ID of the employee who has left the team
removed_device = "2ye3lzg"

# Remove that employee's username and device ID from `approved_users` and `approved_devices` respectively
approved_users.remove(removed_user)
approved_devices.remove(removed_device)

# Display `approved_users`
print(approved_users)

# Diplay `approved_devices`
print(approved_devices)

# Assign `username` to a username
username = "sgilmore"

# Conditional statement
# If `username` belongs to `approved_users`, then display "The user ______ is approved to access the system."
# Otherwise display "The user ______ is not approved to access the system."
if username in approved_users:
    print("The user {} is approved to access the system.".format(username))
else:
    print("The user {} is not approved to access the system".format(username))

# Assign `ind` to the index of `username` in `approved_users`
ind = approved_users.index(username)

# Display the value of `ind`
print(ind)

# Display the device ID at the index that matches the value of `ind` in `approved_devices`
print(approved_devices[ind])

# Assign `device_id` to a device ID
device_id = "4n482ts"

# Define a function named `login` that takes in two parameters, `username` and `device_id`
def login(username, device_id):

    # If `username` belongs to `approved_users`,
    if username in approved_users:

        # then display "The user ______ is approved to access the system.",
        print("The user", username, "is approved to access the system.")

        # assign `ind` to the index of `username` in `approved_users`,
        ind = approved_users.index(username)

        # and execute the following conditional
        # If `device_id` matches the element at the index `ind` in `approved_devices`,

        if device_id == approved_devices[ind]:

            # then display "______ is the assigned device for ______"
            print(device_id, "is the assigned device for", username)

        # Otherwise,
        else:

          # display "______ is not their assigned device"
          print(device_id, "is not their assigned device.")

    # Otherwise (part of the outer conditional and handles the case when `username` does not belong to `approved_users`),
    else:

        # Display "The user ______ is not approved to access the system."
        print("The username", username, "is not approved to access the system.")

# Call the function you just defined to experiment with different username and device_id combinations
login(approved_users[0],approved_devices[0])
login(approved_users[1],approved_devices[3])
login(approved_users[2],approved_devices[2])