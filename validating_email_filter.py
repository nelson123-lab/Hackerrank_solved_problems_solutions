def fun(s):
    try:
        username, other = s.split("@")
        website, extension = other.split(".")
    except:
        return False
    username = username.replace("-", "").replace("_", "")
    if username.isalnum() == False:
        return False
    elif website.isalnum() == False:
        return False
    elif len(extension) > 3:
        return False
    else:
        return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
