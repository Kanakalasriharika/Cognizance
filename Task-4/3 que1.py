#print the list in tabular form
sl = []
def student_list(Roll_no, Name, Marks):
    sl.append([Roll_no, Name, Marks])
    
 
student_list(1301, "Jim    ",   87)
student_list(1302,  "Jhon   ", 80)
student_list(1303,  "Rickey ",85)
student_list(1304,  "Olive  ", 90)
student_list(1305,  "Leo    ",    76)
student_list(1306,  "Charles", 95)
 
 
def display():
    if(len(sl) != 0):
        print("Roll No    Name      Marks")
    for i in sl:
        print(f"{i[0]}       {i[1]}   {i[2]}")
 
display()
