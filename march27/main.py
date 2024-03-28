from students import Student
from teachers import Teacher

_student = Student()
_teacher = Teacher()

while True:
    who = input("""
Choose one            
----------
Student(s) 
Teacher(t)
Clear(c)              
Exit(e)               
""")
    if who == "e":  
        break
    if who == "s":
        print("--------------------")
        menu1 = input("""    
yapmak istediğiniz işlemi yazınız:
1.)add
2.)list
3.)info
4.)back
""")
        if menu1 == "add":
            _student.add_student()
        elif menu1 == "list":              
            _student.list_student()
        elif menu1 == "info" :
            _student.study()
        elif menu1 == "back":
            print("Geri dönme fonksiyonu henüz güncellenmedi(student)")      
        else:    
            print("şuan öğrenci bölümündeyiz")
            continue
    elif who == "t":
        menu2 = input("""
yapmak istediğiniz işlemi yazınız:
1.)add
2.)list
3.)info
4.)back           
""")
        if menu2 == "add":
            _teacher.add_teacher()     
        elif menu2 == "list":
            _teacher.list_teacher()
        elif menu2 == "info":
            _teacher.teach()
        elif menu2 == "back":
            print("Geri dönme fonksiyonu henüz güncellenmedi(teacher)") 
        else:
            print("şuan öğretmen bölümündeyiz")
    elif who == "c":
        print("Sayfa temizleme fonksiyonu henüz güncellenmedi...")                  
    else:
        print("Lütfen menüden bir seçim yapın!")