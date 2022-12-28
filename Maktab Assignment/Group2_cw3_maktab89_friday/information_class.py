from random import randint


class information:
    def __init__(self, address, shahr, ostan, codeposty, website):
        self.address = address
        self.shahr = shahr
        self.ostan = ostan
        self.codeposty = codeposty
        self.website = website

    def getawebsite(self):
        return self.website

    def getacodeposty(self):
        return self.codeposty

    def getaostan(self):
        return self.ostan

    def getashahr(self):
        return self.shahr

    def getaddress(self):
        return self.address


class personalinformation:
    def __init__(self, fname, lname, phonenumber, email):
        self.fname = fname
        self.lname = lname
        self.phonenumber = phonenumber
        self.email = email

    def getname(self):
        return (self.fname + self.lname)

    def getphonenumber(self):
        return self.phonenumber

    def getemail(self):
        return self.email


class Student:
    def __init__(self, personalinformation):
        self.personalinformation = personalinformation
        sid = str(randint(99, 999))
        while Check_sid(sid, 'Students') == True:
            sid = str(randint(99, 999))
        self.sid = sid

    def register(self):
        if f'{self.sid}:{self.personalinformation.getname()}:{self.personalinformation.getphonenumber()}:{self.personalinformation.getemail()}' in self.getobjects():
            print('This class already exist!!!')
        else:
            with open("Students.txt", mode="a+") as f:
               f.write(f'{self.sid}:{self.personalinformation.getname()}:{self.personalinformation.getphonenumber()}:{self.personalinformation.getemail()}\n')

    def getobjects(self):
        list1 = []
        with open('Students.txt', mode='a+') as f:
            line = f.readline()
            line = line.replace(" ", "")
            if not line:
                return list1
            list1.append(lines)
        return list1

    def getobject(self):
        with open('Classes.txt', mode='a+') as f:
            line = f.readline()
            line = line.replace(" ", "")
            if not line:
                lines = []
                return lines
            lines = line.split(":")
            if lines[1] == self.personalinformation.getname():
                return lines
        lines = []
        return lines


class Teacher:
    def __init__(self, personalinformation):
        self.personalinformation = personalinformation
        tid = str(randint(99, 999))
        while Check_id(tid, 'Teachers') == True:
            tid = str(randint(99, 999))
        self.tid = tid


    def register(self):
        if f'{self.tid}:{self.personalinformation.getname()}:{self.personalinformation.getphonenumber()}:{self.personalinformation.getemail()}' in self.getobjects():
            print('This class already exist!!!')
        else:
            with open("Teachers.txt", mode="a+") as f:
                f.write(f'{self.tid}:{self.personalinformation.getname()}:{self.personalinformation.getphonenumber()}:{self.personalinformation.getemail()}\n')


    def getobjects(self):
        list1 = []
        with open('Teachers.txt', mode='a+') as f:
            line = f.readline()
            line = line.replace(" ", "")
            if not line:
                return list1
            list1.append(lines)
        return list1

    def getobject(self):
        with open('Teachers.txt', mode='a+') as f:
            line = f.readline()
            line = line.replace(" ", "")
            if not line:
                lines = []
                return lines
            lines = line.split(":")
            if lines[1] == self.personalinformation.getname():
                return lines
        lines = []
        return lines


def Check_id(id, type):
    exist = False
    with open(f'{type}.txt', mode='a+') as f:
        line = f.readline()
        line = line.replace(" ", "")
        if not line:
            return exist
        lines = line.split(":")
        if lines[0] == id:
            exist = True
            return exist
    return exist


class university_class:
    def __init__(self, class_name, class_teacher, list_participent):
        self.list_participent = list_participent
        self.class_name = class_name
        self.class_teacher = class_teacher
        cid = str(randint(99, 999))
        while Check_id(cid, 'Classes') == True:
            cid = str(randint(99, 999))
        self.cid = cid

    def register(self):
        if f'{self.cid}:{self.class_name}:{self.class_teacher}:{self.list_participent}' in self.getobjects():
            print('This class already exist!!!')
        else:
            with open("Classes.txt", mode="a+") as f:
                f.write(f'{self.cid}:{self.class_name}:{self.class_teacher}:{self.list_participent}\n')


    def getobject(self):
        with open('Classes.txt', mode='a+') as f:
            line = f.readline()
            line = line.replace(" ", "")
            if not line:
                lines = []
                return lines
            lines = line.split(":")
            if lines[1] == self.class_name:
                return lines
        lines = []
        return lines


    def getobjects(self):
        list1 = []
        with open('Classes.txt', mode='a+') as f:
            line = f.readline()
            line = line.replace(" ", "")
            if not line:
                return list1
            lines = line.split(":")
            list1.append(lines)
        return list1


class university:
    def __init__(self, university_name, information):
        self.university_name = university_name
        self.information = information
        uid = randint(99, 999)
        while Check_id(uid, 'University') == True:
            uid = str(randint(99, 999))
        self.uid = uid

    def Registering(self, info):
        info.register()

    def getnumber(self, info):
        list1 = info.getobjects()
        return len(list1)

    def getmembers(self, info):
        return info.getobjects()

    def search(self, info):
        return info.getobject()

    def university_information(self):
        return (university_name + ':'+ self.information.getaddress() + ':'+ self.information.getshahr() + ':'+ self.information.getacodeposty() + ':'+ self.information.getaostan() + ':'+ self.information.getwebsite() + ':'+ len(Student.getobjects()) + ':'+ len(Teacher.getobjects()) + ':' + len(university_class.getobjects()))
