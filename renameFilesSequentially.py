''' Aditya Tiwari
    9/12/2021
    05:30pm '''

import os

path=os.chdir("C:\\Users\\aditya\\Pictures\\hour_of_code")

i=0
for file in os.listdir(path):
    new_file_name="pic_{}.jpg".format(i)
    os.rename(file,new_file_name)
    i=i+1
