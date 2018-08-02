import pandas as pd
import numpy as np


class EvandExcelParser:
    def __init__(self, file_path = None):
        if file_path is None:
            print("Enter excel path please")
            raise Exception("Enter excel path")
        self.file_path = file_path
        try:    
            self.df = pd.read_excel(io=file_path)
            none_name = ['' for x in range(len(self.df['ایمیل']))]
            self.df['Fullname'] = np.asarray(none_name)
        except Exception as e:
            print("Error in opening excel file")
            raise e
        

    def verify_user(self, email = None, number = None):
        if email is not None:
            return self.__email_validation(email)
        elif number is not None:
            return self.__number_validation(number)
        else:
            print("you must enter at least email or phone number")
            raise Exception("Inputs bot true")

    def __email_validation(self, email):
        emails = self.df['ایمیل'].tolist()
        if email in emails:
            return emails.index(email)
    
    def __number_validation(self, number):
        numbers = self.df['شماره تماس'].tolist()
        if number in numbers:
            return numbers.index(number)

    def set_fullname(self, row, fullname):
        self.df.set_value(row, 'Fullname', fullname)

    def save_excel(self):
        writer = pd.ExcelWriter(self.file_path)
        self.df.to_excel(writer,'Sheet1')
        writer.save()