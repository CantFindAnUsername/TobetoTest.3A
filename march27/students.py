
class Student:
    student_list = [{"student_number":1,"name":"Talha","surname":"Özçam","subject":"mat"}]
    def study(self):
        s_number = int(input("Öğrenci numaranızı giriniz: "))
        for student in self.student_list:
            if student['student_number'] == s_number:
                print(f"{student['name']} {student['subject']} dersini alıyor.")
                print("------------------------")
                return

    def add_student(self):
        student_number = int(input("Öğrenci numaranızı giriniz: "))
        for student in self.student_list:
            if student_number == student['student_number']:
                print(f"{student_number} numaralı kayıt zaten var.")
                return
        name = input("Öğrenci adını giriniz: ")
        surname = input("Öğrenci soyadını giriniz: ")
        subject = input("Aldığınız dersi giriniz: ")
        new_student = {"name":name,"surname":surname,"student_number":student_number,"subject":subject}
        self.student_list.append(new_student)

    def list_student(self):
        if not self.student_list:
            print("henüz kayıt oluşturulmadı!")
            return
        for student in self.student_list:
            print(f"""
Student Number: {student['student_number']}
Name: {student['name']} 
Surname: {student['surname']} 
Subject: {student['subject']}
------------------------""") 