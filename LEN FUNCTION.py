# Function which return length of string
def findLength(string):

    # Initialize count to zero
    count = 0

    # Counting character in a string
    for i in string:
        count+= 1
    # Returning count
    return count

# Driver code
string = input("Enter the word")
print(findLength(string))
