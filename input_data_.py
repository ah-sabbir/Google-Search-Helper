import os
import pandas as pd
class data_generator:
    def __init__(self):
        self.read_me()
        if (os.path.isfile('input.xlsx')):
            self.file=pd.read_excel('input.xlsx')
            
        else:
            print('The input Text file has created ! ')
            print('''please make a sure first that you have
                    already entered data into the input.txt file ''')

    def read_me(self):
        readMe_text='''
        *****************  developed by Ahmmed Sabbir*************
name : mail tester
version : 3.00 
after installation python properly .............
these packages which are must be installed for python 3.7
1. dnspython
2. pandas
3. xlsxwriter
4. re

how to install a python package ?
:) it's simple with 2 steps
open command prompt and write " pip install <package name here>" then hit enter
      0 0
       ^
      ---
      welcome to the py's world
'''
        
        if not (os.path.isfile('read me.txt')):
            with open('read me.txt','w+') as read_m:
                read_m.write(readMe_text)
        else:
            pass



        
    def name_spliter(self,name):
        return name.split(" ")

    def get_data_list(self):
        list_=[]
        for line in data_generator.file['company name']:
            for name in self.name_spliter(line.replace(' ','\n')):
                list_.append(name)
        return list_
        



          
