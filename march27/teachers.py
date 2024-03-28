
class Teacher:
    teacher_list = [{"teacher_number":1001,"name":"Ercan","surname":"Deniz","field":"Math"}]
    def teach(self):
        t_number = int(input("Öğretmen numaranızı giriniz: "))
        for teacher in self.teacher_list:
            if teacher['teacher_number'] == t_number:
                print(f"{teacher['name']} {teacher['field']} dersini veriyor.")
                print("------------------------")
                return

    def add_teacher(self):
        teacher_number = int(input("Öğretmen numaranızı giriniz: "))
        for teacher in self.teacher_list:
            if teacher_number == teacher['teacher_number']:
                print(f"{teacher_number} numaralı kayıt zaten var.")
                return
        name = input("Öğretmen adını giriniz: ")
        surname = input("Öğretmen soyadını giriniz: ")
        field = input("Öğretmen branşınızı giriniz: ")
        new_teacher = {"teacher_number":teacher_number,"name":name,"surname":surname,"field":field}
        self.teacher_list.append(new_teacher)

    def list_teacher(self):
        if not self.teacher_list:
            print("henüz kayıt oluşturulmadı!")
            return
        for teacher in self.teacher_list:
            print(f"""
Teacher Number: {teacher['teacher_number']}
Name: {teacher['name']} 
Surname: {teacher['surname']} 
Subject: {teacher['field']}
------------------------""")             