email = input("Enter Youe Email Address: ")

username = email[:email.index('@')]
domain = email[email.index('@') +1:]

print(f' Your usename is {username} & domain name is {domain}')