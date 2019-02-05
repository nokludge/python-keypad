class KeypadGPIOStub:
    BOARD = ""
    OUT = "out"
    LOW = 0
    PUD_UP = ""
    PUD_DOWN = ""
    IN = ""
    HIGH = 1

    def __init__(self):
        pass

    def setmode(self, value):
        pass

    def output(self, key, value):
        pass

    def setup(self, key, value, pull_up_down=""):
        pass

    def input(self, value):
        pass
