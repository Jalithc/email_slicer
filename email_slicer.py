email = input("Enter your email: ").strip().lower()

username, domain = email.split('@')
print(f"Your username is {username} & your domain is {domain}")