class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
    def up(self):
        """Makes the elevator go up one floor."""
        self.current = self.current + 1 if self.current< self.top else self.current
        return "Current Floor {}".format(self.current)
    def down(self):
        """Makes the elevator go down one floor."""
        self.current = self.current - 1 if self.current > self.bottom else self.current
        return "Current Floor {}".format(self.current)
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        return "Current Floor {}".format(self.current)
    def __str__(self):
        return "Current Floor {}".format(self.current)
elevator = Elevator(-1, 10, 0)

elevator.up()
elevator.current
print(elevator)

elevator.down()
elevator.current
print(elevator)

elevator.go_to(10)
elevator.current
print(elevator)

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator) # should be 1
