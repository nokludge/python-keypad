class MatrixKeypad:
    def __init__(self, key_map, rows, columns, gpio):
        self.__gpio = gpio
        self.__gpio.setmode(self.__gpio.BOARD)
        self.__keypad = key_map
        self.__rows = rows
        self.__columns = columns

    def get_key(self):
        self.__gpio.setup(self.__columns, self.__gpio.OUT)
        self.__gpio.setup(self.__rows, self.__gpio.IN, pull_up_down=self.__gpio.PUD_UP)

        for index in self.__columns:
            self.__gpio.output(index, self.__gpio.LOW)

        row_value = self.__get_pressed_row()

        if row_value is None:
            self.__reset_all_pins()
            return

        self.__gpio.setup(self.__columns, self.__gpio.IN, pull_up_down=self.__gpio.PUD_DOWN)
        self.__gpio.setup(self.__rows[row_value], self.__gpio.OUT)
        self.__gpio.output(self.__rows[row_value], self.__gpio.HIGH)
        col_value = self.__get_pressed_column()

        if col_value is None:
            self.__reset_all_pins()
            return

        self.__reset_all_pins()
        return self.__keypad[row_value][col_value]

    def __get_pressed_row(self):
        result = None
        for i in range(len(self.__rows)):
            if self.__gpio.input(self.__rows[i]) == self.__gpio.LOW:
                result = i
        return result

    def __get_pressed_column(self):
        result = None
        for i in range(len(self.__columns)):
            if self.__gpio.input(self.__columns[i]) == self.__gpio.HIGH:
                result = i
        return result

    def __reset_all_pins(self):
        self.__gpio.setup(self.__rows, self.__gpio.IN, pull_up_down=self.__gpio.PUD_UP)
        self.__gpio.setup(self.__columns, self.__gpio.IN, pull_up_down=self.__gpio.PUD_UP)
