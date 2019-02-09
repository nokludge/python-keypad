python-keypad
-------------
Simple tiny Python GPIO keypad code. 

Installation
------------

```
git clone https://github.com/nokludge/python-keypad.git
cd python-keypad
python setup.py install
```

Usage
-----

```
import RPi.GPIO as GPIO
import keypad.MatrixKeypad as MatrixKeypad

key_map = [
    [1, 2, 3, "A"],
    [4, 5, 6, "B"],
    [7, 8, 9, "C"],
    ["*", 0, "#", "D"]
]
gpio_pins_for_rows = [29, 31, 33, 35]
gpio_pins_for_columns = [37, 36, 38, 40]
key_matrix = MatrixKeypad(key_map, gpio_pins_for_rows, gpio_pins_for_columns, GPIO())

if __name__ == '__main__':
    while True:
        key = key_matrix.get_key()

        if key == "B":
            break
```

License
-------

MIT

Author Information
------------------

http://www.kludge.io/
