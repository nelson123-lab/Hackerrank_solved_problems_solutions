def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    # Initialize an array to hold each row
    rows = [""] * numRows

    # Set the initial row and direction
    cur_row = 0
    direction = 1

    for char in s:
        # Add the current character to the current row
        rows[cur_row] += char

        # If we've reached the top or bottom row, switch direction
        if cur_row == 0:
            direction = 1
        elif cur_row == numRows - 1:
            direction = -1

        # Move to the next row
        cur_row += direction

    # Combine all rows into one string and return it
    return "".join(rows)
print(convert("PAYPALISHIRING", 3))
