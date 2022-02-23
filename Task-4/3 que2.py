#extract and print the second record
sl = []
def student_list(Roll_no, Name, Marks):
    sl.append([Roll_no, Name, Marks])
    
student_list(1301, "Jim    ",   87)
student_list(1302,  "Jhon   ", 80)
student_list(1303,  "Rickey ",85)
student_list(1304,  "Olive  ", 90)
student_list(1305,  "Leo    ",    76)
student_list(1306,  "Charles", 95) 

 
def print_second_record():
    print(f"{sl[1][0]}          {sl[1][1]}      {sl[1][2]}")
    
print_second_record()
 
