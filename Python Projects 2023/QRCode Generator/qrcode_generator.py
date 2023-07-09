"""
Created on Sun Jul  9 19:16:55 2023

@author: Sami RAJICHI

@project: QRCode Generator
"""

import qrcode


class CustomQr:

    def __init__(self, qr_size: int, padding: int):
        """
        This method represents the initializer of the class.
        It creates an instance from the QRCode class, and requires a size and box padding 
        as parameters
        """
        self.qr = qrcode.QRCode(box_size=qr_size, border=padding)

    def create_qr(self, code_color: str, background_color: str, filename: str):
        """
        This method serves in simulating a QRCode:
            1- It takes first some data that will be stored as code
            2- Makes an image that holds the data 
            3- Then, saves it within the location of the this python script
        """
        data: str = input('Enter data: ')

        try:
            self.qr.add_data(data)
            self.image = self.qr.make_image(
                fill_color=code_color, back_color=background_color)
            self.image.save(filename)
            print('Successfully Generated..')
        except Exception as e:
            print(f'{e}')


# Main function
if __name__ == '__main__':
    qr = CustomQr(30, 3)
    qr.create_qr('purple', 'white', 'sample.png')
