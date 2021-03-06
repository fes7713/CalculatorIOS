#######################
# Signal and slot
#######################
import time
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt


class Ui_Functions():
    def __init__(self, window):
        self.ui = window.ui

        #######################
        # Define Variables
        #######################
        # it saves main number that will be displayed to the main display
        self.number = 0
        # it saves number after operator button is pressed. This number will be shown to the sub display above the main
        # diaplay
        self.subLine_number = 0

        # it saves previous operator action
        self.subline_action = None

        # When this afterEqual is on and if any keypad is pressed,
        # first clears the display and then add that keypad number.
        self.afterEqual = False

        # When decimal point is clicked, add decimal number.
        self.decimal_on = False
        ###################################################################

        #######################
        # Signal and slots
        #######################

        # Connect keypad buttons to pressed actions
        self.ui.button_0.clicked.connect(lambda: self.keypad_pressed(0))
        self.ui.button_1.clicked.connect(lambda: self.keypad_pressed(1))
        self.ui.button_2.clicked.connect(lambda: self.keypad_pressed(2))
        self.ui.button_3.clicked.connect(lambda: self.keypad_pressed(3))
        self.ui.button_4.clicked.connect(lambda: self.keypad_pressed(4))
        self.ui.button_5.clicked.connect(lambda: self.keypad_pressed(5))
        self.ui.button_6.clicked.connect(lambda: self.keypad_pressed(6))
        self.ui.button_7.clicked.connect(lambda: self.keypad_pressed(7))
        self.ui.button_8.clicked.connect(lambda: self.keypad_pressed(8))
        self.ui.button_9.clicked.connect(lambda: self.keypad_pressed(9))

        # This clears display and inside numbers
        self.ui.AC_buttom.clicked.connect(self.allClear_display)
        self.ui.C_button.clicked.connect(self.clear_display)
        # Calculates result using operator saved in self.subline_action and
        #               numbers saved in self.number and self.subline_number
        self.ui.equal_button.clicked.connect(self.equal_pressed)
        self.ui.add_button.clicked.connect(lambda: self.calcButton_pressed("add"))
        self.ui.subtract_button.clicked.connect(lambda: self.calcButton_pressed("substract"))
        self.ui.multi_button.clicked.connect(lambda: self.calcButton_pressed("multi"))
        self.ui.divide_button.clicked.connect(lambda: self.calcButton_pressed("divide"))

        # Multiply self.number by -1
        self.ui.sign_button.clicked.connect(self.reverseSign)

        # add decimal point to the self.number
        self.ui.dp_button.clicked.connect(self.decimal_clicked)

    #######################
    # functions for slots
    #######################

    # Define actions when one of keypad is pressed.
    def keypad_pressed(self, number):
        # after decimal number is pressed, just append inputted number to the text displayed in main display
        if self.decimal_on:
            # get text
            text = self.ui.display_textLine.text()
            print(text + str(number))
            # append number
            self.ui.number = float(text + str(number))

            # make result string
            string = str(self.number)
            # get integer part
            num_int = str(int(self.number))

            # get decimal part and adjust size and cut some decimal point to avoid text is going out of display
            # eg) if number was 3.33333333333333333 and exceeding the display then cut some decimal parts and become
            # 3.3333333 maybe
            num_decimal = string[len(str(num_int)): 12]
            # make a number
            self.number = float(num_int + num_decimal)
            self.ui.display_textLine.setText(str(self.number))
            return

        # you cannot input infinite number
        if len(str(self.number)) > 10:
            return

        # If afterEqual then first clear number
        if self.afterEqual:
            self.number = 0
            self.afterEqual = False

        # This is normal operation. Just multiply previous value by 10 and add inputted value.
        # Eg) number = 123, 3 was inputted, 123 * 10 + 3 = 1233
        self.number = self.number * 10 + number
        self.ui.display_textLine.setText(str(self.number))

    # Just reverse sign, Positive becomes negative, negative becomes positive
    def reverseSign(self):
        self.number *= -1
        self.ui.display_textLine.setText(str(self.number))

    # Clear all
    def allClear_display(self):
        self.number = 0
        self.subLine_number = 0
        self.subline_action = None
        self.ui.display_textLine.setText("0")
        self.ui.display_textSubLine.setText("")
        self.decimal_on = False
        self.afterEqual = True

    # Clear only number and display
    def clear_display(self):
        self.number = 0
        self.ui.display_textLine.setText("0")
        self.afterEqual = True

    # Add decimal point and go into decimal mode.
    def decimal_clicked(self):
        # Prevent user from inputting multiple decimal points Eg) 23....... No! 23. <= cannot put more dots
        if "." in self.ui.display_textLine.text():
            return
        self.decimal_on = True
        self.ui.display_textLine.setText(self.ui.display_textLine.text() + ".")

    # Calculate answer
    def equal_pressed(self):
        # Make sure user pressed one of operator button before the equal.
        # self.subline_action is None if user did not input one of operator like + or -
        # sub display shows 3+ and 4 is in main display then = is clicked,
        #       ->>>>> sub display become empty and main display becomes 7
        #   Next number input will clear display and shows that number
        # After Equal : main display : 7 (This is answer from previous calculation)
        #       4 is clicked, main display become 4, not 74, because it clears 7 and insert 4 (see keypad_pressed)
        if self.subline_action is not None:
            # Get operator and calculate
            if self.subline_action == "+":
                self.number += self.subLine_number
            elif self.subline_action == "-":
                self.number = self.subLine_number - self.number
            elif self.subline_action == "*":
                self.number *= self.subLine_number
            elif self.subline_action == "/":
                self.number = self.subLine_number / self.number

            # check for decimal number
            # if answer was 1.0 then make it 1
            if int(self.number) == self.number:
                self.number = int(self.number)
            # if answer exceeds display range then cut some decimal numbers.
            # 3.333333333333333 becomes 3.3333333333, more than 12 letter will be cut
            else:
                string = str(self.number)
                num_int = str(int(self.number))
                # This 12 defines the length of output
                num_decimal = string[len(str(num_int)): 12]
                self.number = float(num_int + num_decimal)
            print(self.number)
            # Clear sub display and insert answer to main display
            self.ui.display_textSubLine.setText("")
            self.ui.display_textLine.setText(str(self.number))
            self.subline_action = None
            # AfterEqual is on so next input will clear the answer shown in the display
            self.afterEqual = True
            self.decimal_on = False

    def calcButton_pressed(self, action):
        # if operator is saved in subline_action then calculate that equation and update sub display
        # sub display shows 3+ and 4 is in main display then + is clicked,
        #       ->>>>> sub display become 7+ and main display becomes 0
        if self.subline_action is not None:
            if self.subline_action == "+":
                self.subLine_number += self.number
            elif self.subline_action == "-":
                self.subLine_number -= self.number
            elif self.subline_action == "*":
                self.subLine_number *= self.number
            elif self.subline_action == "/":
                self.subLine_number /= self.number
                if int(self.subLine_number) == self.subLine_number:
                    self.subLine_number = int(self.subLine_number)

            self.ui.display_textSubLine.setText(str(self.subLine_number) + self.subline_action)
            self.number = 0
            self.ui.display_textLine.setText(str(self.number))

        # if no operator is saved then make sub_number number and let the main display ready for next input
        # Sub display is empty and main display shows 4 maybe, then + is clicked,
        # Sub display will show 4+ and main display will become 0
        else:
            self.subLine_number = self.number
        if action == "add":
            self.subline_action = "+"
        elif action == "substract":
            self.subline_action = "-"
        elif action == "multi":
            self.subline_action = "*"
        elif action == "divide":
            self.subline_action = "/"
        self.ui.display_textSubLine.setText(str(self.subLine_number) + self.subline_action)
        self.number = 0
        self.ui.display_textLine.setText(str(self.number))
        self.decimal_on = False



    # Not used in this project but if you wanna have key input then set this part up
    ########################
    # Key Setting (ASCII)###
    ########################
    def key_event(self, event):
        # event.key() to get keyboard input
        print(event.key())
        key = event.key()
        if 48 <= key <= 57:
            self.ui.update_pass(int(chr(key)))

        # 16777220 is Enter key code
        if key == 16777220:
            self.ui.mousePressEvent()
