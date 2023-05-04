while True:
  name = input()
  if name[0] =="#" :
    print("hjhah")
    continue
    # Continue for not getting out of the loop

    """
    continue statement ends the current iteration and jumps to the
    top of the loop and starts the next iteration
    """
  if name == "done" :
    print("correct")
    break
    # break for getting out of the loop
    """
    break ends the current loop and jumps to the statement immediately
    following the loop
    """
  print(name)
print("DONE")
