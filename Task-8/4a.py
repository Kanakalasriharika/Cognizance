
import pandas as pd
ser = pd.Series(['amrita', 'vishwa',  'vidyapeetham', 'chennai' , 'campus'])
z=ser.str.capitalize()
for k in z:
 print(k,end=' ')
