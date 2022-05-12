import re


class Luhn:
    def __init__(self, card_num):
        self.card = card_num.replace(" ", "")

    def valid(self):
        if re.search('[^0-9]', self.card) or len(self.card) < 2:
            return False

        suma = 0
        card = self.card[::-1]
        for index in range(0, len(card)):
            num = int(card[index])
            if index % 2 != 0:
                num *= 2
            if num > 9:
                num -= 9
            suma += num
        return suma % 10 == 0
