
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