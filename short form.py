def initials(phrase):
    words = phrase.upper()
    result = ""
    for word in words:
        result += word[0]
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
