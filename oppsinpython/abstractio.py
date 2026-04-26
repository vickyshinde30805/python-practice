class car:
    def __init__(self):
        self.cluch=False
        self.brk=False
        self.acc=False
    def start(self):
        self.cluch=True
        self.brk=False
        self.acc=True
        print("car is starting")
c1=car()
c1.start()
#it shows the only required output car is starting to the user do not show the unnnecessary code steps 