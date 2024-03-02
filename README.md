# Problem3
TALENTRAX TECHNOLOGIES-Backend Developer Screening Assignment

Problem-3

Q3. our flight departs in a few days from the coastal airport; the easiest way down to
the coast from here is via toboggan.
The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
"Something's wrong with our computers; we can't log in!" You ask if you can take a
look.
Their password database seems to be a little corrupted: some of the passwords
wouldn't have been allowed by the Official Toboggan Corporate Policy that was in
effect when they were chosen.
To try to debug the problem, they have created a list (your puzzle input) of
passwords (according to the corrupted database) and the corporate policy when that
password was set.
For example, suppose you have the following list:
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy
indicates the lowest and highest number of times a given letter must appear for the
password to be valid. For example, 1-3 a means that the password must contain a at
least 1 time and at most 3 times.
In the above example, 2 passwords are valid. The middle password, cdefg, is not; it
contains no instances of b, but needs at least 1. The first and third passwords are
valid: they contain one a or nine c, both within the limits of their respective policies.
How many passwords are valid according to their policies?
To play, please identify yourself via one of these services:



Solution:

def count_valid_passwords(passwords):
    valid_count = 0

    for entry in passwords:
        # Split the entry into policy and password
        policy, password = entry.split(':')
        password = password.strip()  # Remove leading and trailing spaces

        # Split the policy into limits and the required character
        limits, char = policy.split(' ')
        min_limit, max_limit = map(int, limits.split('-'))

        # Count occurrences of the required character in the password
        char_count = password.count(char)

        # Check if the count is within the specified limits
        if min_limit <= char_count <= max_limit:
            valid_count += 1

    return valid_count

# Example usage with your provided input
password_list = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
result = count_valid_passwords(password_list)

print(f"The number of valid passwords is: {result}")


Explanation:

1.Function Definition:

def count_valid_passwords(passwords):
    valid_count = 0

    for entry in passwords:
        # ... rest of the code ...
    
    return valid_count

-This function takes a list of password entries as input and initializes a 
 variable 'valid_count' to 0 to count the number of valid passwords.


2.Loop through Password Entries:

for entry in passwords:
    # Split the entry into policy and password
    policy, password = entry.split(':')
    password = password.strip()  # Remove leading and trailing spaces

    # Split the policy into limits and the required character
    limits, char = policy.split(' ')
    min_limit, max_limit = map(int, limits.split('-'))

    # Count occurrences of the required character in the password
    char_count = password.count(char)

    # Check if the count is within the specified limits
    if min_limit <= char_count <= max_limit:
        valid_count += 1

- The function iterates through each password entry in the input list.
- It splits each entry into the policy and password using the colon ':' as a separator.
- The password is then stripped of leading and trailing spaces.
- The policy is further split into the limits (min and max occurrences) and the required character.
- The count of occurrences of the required character in the password is calculated.
- If the count is within the specified limits, the password is considered valid, and 'valid_count' is incremented.


3.Return Valid Count:

return valid_count

-The function returns the total count of valid passwords.


4.Example Usage:

password_list = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
result = count_valid_passwords(password_list)

print(f"The number of valid passwords is: {result}")

- An example list of password entries is provided, and the 'count_valid_passwords' function is called on it.
- The result is printed, indicating the number of valid passwords based on the specified policy.

code is a simple implementation of password validation based on a policy, where each entry consists of the policy, 
the required character, and the actual password. The function counts the number of valid passwords according to 
the given policy.
