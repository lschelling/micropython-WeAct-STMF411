from machine import Pin, ADC
from time import sleep

class joystick:
    def __init__(self, x_pin_no, y_pin_no, sw_pin_no):
        """
        !! Don't forget to connect x and y to ADC pins on Pico. !!
        """
        self.__analog_x = ADC(Pin(x_pin_no))
        self.__analog_y = ADC(Pin(y_pin_no))
        self.__button = Pin(sw_pin_no,Pin.IN, Pin.PULL_UP)
        self.__location = None

    def return_loc_data(self):
        """
        returns tuple x and y location data. The analog x and y value scaled to 0-65535. For example, maximum x is scaled to 65535 and min x is to 0.
        """
        xdata = self.__analog_x.read_u16()
        ydata = self.__analog_y.read_u16()
        return (xdata,ydata)

    def p_button_status(self):
        """
        prints button status, whether it is pressed or not.
        """
        button_value = self.__button.value()
        button_status = "not pressed"
        if button_value == 0:
            button_status = "pressed"
        print("Button status is: ", button_status)
        return button_value==0

    def give_location(self):
        """
        returns the location in string format. Location indicates where the joystick is.
        This functions is still in development progress so sometimes it can't locate the position and gives "Not Located" output.
        """
        self.__xdata = self.__analog_x.read_u16()
        self.__ydata = self.__analog_y.read_u16()
        print(self.__xdata,self.__ydata)
        if (30000 <self.__xdata < 34000) and  (30000 < self.__ydata < 34000):
            location = "Middle"
        elif (self.__xdata < 700) and  (1500 < self.__ydata < 34000):
            location = "Left"
        elif (self.__xdata < 700) and  (self.__ydata < 700):
            location = "Up-Left"
        elif (self.__xdata < 700) and  (34000 < self.__ydata < 67000):
            location = "Down-Left"
        elif (30000 <self.__xdata < 34000) and  (self.__ydata < 700):
            location = "Up"
        elif (30000 <self.__xdata < 34000) and  (34000 <self.__ydata < 67000):
            location = "Down"
        elif (40000 <self.__xdata < 67000) and  (34000 <self.__ydata < 67000):
            location = "Down-Right"
        elif (34000 <self.__xdata < 67000) and  (30000 <self.__ydata < 34000):
            location = "Right"
        elif (40000 <self.__xdata < 67000) and  (self.__ydata < 700):
            location = "Up-Right"
        else:
            location = "Not located"
            
        return location
