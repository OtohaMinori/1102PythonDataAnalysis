'''
Date:2022.03.10
Name:幽霊Ｓ☄
SID:B10813180
Title:Ex.3
'''

'''
Q1.
Please print: My car is blue and has 4 seats.
'''


class Cars:
    def __init__(self, color, seat):
        self.color = color
        self.seat = seat

    def drive(self):
        return("My car is "+self.color+" and has "+self.seat+" seats.")


result = Cars("blue", "4")
print(result.drive())
