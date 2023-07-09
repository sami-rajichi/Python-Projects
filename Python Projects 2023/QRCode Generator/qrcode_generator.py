"""
Created on Sun Jul  9 19:16:55 2023

@author: Sami RAJICHI

@project: QRCode Generator
"""

import qrcode


class CustomQr:

    def __init__(self, qr_size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=qr_size)

    def create_qr(self, code_color: str, background_color: str, filename: str):

        data: str = input('Enter data: ')

        try:
            self.qr.add_data(data)
            self.image = self.qr.make_image(
                fill_color=code_color, back_color=background_color)
            self.image.save(filename)
            print('Successfully Generated..')
        except Exception as e:
            print(f'{e}')


if __name__ == '__main__':
    qr = CustomQr(30, 3)
    qr.create_qr('purple', 'white', 'sample.png')
