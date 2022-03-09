
#convert the first character to each element to uppercase
import pandas as pd
ser = pd.Series(['amrita', 'vishwa', 'vidyapeetham','chennai','campus'])
modified_ser= ser.str.title()  
print("Original series: ")
print(ser)
print("\nModified series: ")
print(modified_ser)
