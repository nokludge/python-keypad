import RPi.GPIO as GPIO
from keypad.MatrixKeypad import MatrixKeypad

key_map = [
    [1, 2, 3, "A"],
    [4, 5, 6, "B"],
    [7, 8, 9, "C"],
    ["*", 0, "#", "D"]
]
rows = [29, 31, 33, 35]
columns = [37, 36, 38, 40]
key_matrix = MatrixKeypad(key_map, rows, columns, GPIO())

if __name__ == '__main__':
    while True:
        key = key_matrix.get_key()

        if key == "B":
            break
