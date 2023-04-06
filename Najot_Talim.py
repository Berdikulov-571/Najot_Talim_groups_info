import os

os.system('cls')

import sys

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout,QLineEdit,QLabel,QListWidget

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'najot_talim_guruh',
    user = 'root',
    password = 'sanjarbek2006'
)

mycursor = mydb.cursor()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500,600)

        self.setGeometry(600, 270, 600, 600)

        # self.acceptDrops()

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("Najot Ta'lim")

        self.initUi()

    def initUi(self):

        self.najot_talim_label = QLabel('NAJOT',self)
        self.najot_talim_label.setStyleSheet(
            'color: blue;'
            'font-size: 70px;'
            'font-weight: bold;'
        )

        self.najot_talim_label2 = QLabel('TA\'LIM',self)
        self.najot_talim_label2.setStyleSheet(
            'color: red;'
            'font-size: 70px;'
            'font-weight: bold;'   
            
        )

        self.login_edit = QLineEdit(self)
        self.login_edit.setFixedSize(200,40)
        self.login_edit.setPlaceholderText('TEACHER LOGIN')
        self.login_edit.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 20px'
            )
        
        self.footer_label = QLabel('© 2023 Najot Ta\'lim IT centre',self)
      
        self.password_edit = QLineEdit(self)
        self.password_edit.setFixedSize(200,40)
        self.password_edit.setPlaceholderText('PASSWORD')
        self.password_edit.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 20px'
            )

        self.footer_label.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 15px'
        )

        self.login_btn = QPushButton('LOGIN',self)
        self.login_btn.setFixedSize(200,40)
        self.login_btn.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )

        self.login_edit.move(135, 230)
        self.password_edit.move(135, 280)

        self.najot_talim_label.move(70, 20)
        self.najot_talim_label2.move(150, 100)

        self.login_btn.move(135, 330)

        self.footer_label.move(135,570)

        self.show()

        self.login_btn.clicked.connect(self.pressLogin)


    def isEmpty(self, username, password):
        if '' in [username, password]:
            return True
        return False

    
    def pressLogin(self):
        username, password = self.login_edit.text(), self.password_edit.text()
        self.displayClear()
        if username == 'Aziz'  and password == '12345':
            self.close()
            self.SecondPage = SecondPage()
            self.SecondPage.show()

        elif username != 'Aziz'  and password != '12345' and self.isEmpty(username, password) :
            self.login_edit.setPlaceholderText('Error login')
            self.password_edit.setPlaceholderText('Error password')                

    
    def displayClear(self):
        self.login_edit.clear()
        self.password_edit.clear()


class SecondPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("Groups Teacher Aziz")

        self.footer_label = QLabel('© 2023 Najot Ta\'lim IT centre',self)

        self.bfn2 = QPushButton(self)
        self.bfn2.setText('Bootcamp Foundation N2')

        self.bfn3 = QPushButton(self)
        self.bfn3.setText('Bootcamp Foundation N3')

        self.bfn32 = QPushButton(self)
        self.bfn32.setText('Bootcamp Foundation N32')

        self.exit = QPushButton(self)
        self.exit.setText('EXIT')

        self.initUi()
    
    def initUi(self):

        self.select = QLabel('SELECT',self)

        self.select.setStyleSheet(
            'color: blue;'
            'font-size: 70px;'
            'font-weight: bold;'
        )

        self.footer_label.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 15px'
        )

        self.bfn2.setStyleSheet(
            'background-color: lightblue; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.bfn2.setFixedSize(300,80)

        self.bfn3.setStyleSheet(
            'background-color: lightblue; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.bfn3.setFixedSize(300,80)

        self.bfn32.setStyleSheet(
            'background-color: lightblue; '
            'font: 18px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.bfn32.setFixedSize(300,80)

        self.exit.setStyleSheet(
            'background-color: lightblue; '
            'font: 18px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.exit.setFixedSize(300,80)

        self.footer_label.move(135,570)
        
        self.bfn2.move(90,120)
        self.bfn3.move(90,220)
        self.bfn32.move(90,320)
        self.exit.move(90,420)

        self.select.move(115, 20)

        self.show()

        self.exit.clicked.connect(self.press_btn_exit)
        self.bfn2.clicked.connect(self.press_btn_third1)
        self.bfn3.clicked.connect(self.press_btn_third2)
        self.bfn32.clicked.connect(self.press_btn_third3)

    
    def press_btn_exit(self):
        self.close()

    def press_btn_third1(self):
        self.close()
        self.thirdPage1 = thirdPage1()
        self.thirdPage1.show()    
    
    def press_btn_third2(self):
        self.close()
        self.thirdPage2 = thirdPage2()
        self.thirdPage2.show() 
    
    def press_btn_third3(self):
        self.close()
        self.thirdPage3 = thirdPage3()
        self.thirdPage3.show() 



class thirdPage1(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(500,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("Group Bootcamp Foundation N 2")

        self.footer_label = QLabel('© 2023 Najot Ta\'lim Group Foundation N 2',self)


        self.table_pupils = QPushButton(self)
        self.table_pupils.setText('List of all students')

        self.add_student = QPushButton(self)
        self.add_student.setText('Add student')

        self.delete_student = QPushButton(self)
        self.delete_student.setText('Delete student')

        self.info = QPushButton(self)
        self.info.setText('Group information')

        self.back = QPushButton(self)
        self.back.setText('BACK')

        self.initUi()
    
    def initUi(self):

        self.bootcamp = QLabel('BOOTCAMP N2',self)

        self.foundation = QLabel('FOUNDATION',self)
        

        self.bootcamp.setStyleSheet(
            'color: blue;'
            'font-size: 60px;'
            'font-weight: bold;'
        )

        self.foundation.setStyleSheet(
            'color: blue;'
            'font-size: 60px;'
            'font-weight: bold;'
        )
        
        self.footer_label.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 15px'
        )

        self.table_pupils.setStyleSheet(
            'background-color: lightblue; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.table_pupils.setFixedSize(300,80)

        self.add_student.setStyleSheet(
            'background-color: lightblue; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.add_student.setFixedSize(300,80)

        self.delete_student.setStyleSheet(
            'background-color: lightblue; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.delete_student.setFixedSize(300,80)

        self.info.setStyleSheet(
            'background-color: lightblue; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )

        self.back.setStyleSheet(
            'background-color: lightgreen; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.back.setFixedSize(90,50)



        self.info.setFixedSize(300,80)

        self.foundation.move(10, 10)
        self.bootcamp.move(10, 70)

        self.table_pupils.move(100, 150)
        self.add_student.move(100,250)
        self.delete_student.move(100, 350)
        self.info.move(100, 450)
        self.back.move(10, 545)

        self.footer_label.move(115, 570)

        self.back.clicked.connect(self.press_btn_back)

        self.table_pupils.clicked.connect(self.press_btn_table)

        self.add_student.clicked.connect(self.press_btn_add_student)

        self.delete_student.clicked.connect(self.press_btn_delete)

        self.info.clicked.connect(self.press_btn_get_info)

        self.show()
    
    def press_btn_back(self):
        self.close()
        self.secondPage = SecondPage()
        self.secondPage.show()
    
    def press_btn_table(self):
        self.close()
        self.bfn2Page = bfn2Page()
        self.bfn2Page.show()
    
    def press_btn_add_student(self):
        self.close()
        self.bfn2_add_student = bfn2_add_student()
        self.bfn2_add_student.show()
    
    def press_btn_delete(self):
        self.close()
        self.bfn2_delete_student = delete_student_bfn2()
        self.bfn2_delete_student.show()
    
    def press_btn_get_info(self):
        self.close()
        self.bfn2_get_info = get_info_bfn2()
        self.bfn2_get_info.show()


class thirdPage2(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(500,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("Group Bootcamp Foundation N 3")

        self.footer_label = QLabel('© 2023 Najot Ta\'lim Group Foundation N 3',self)


        self.table_pupils = QPushButton(self)
        self.table_pupils.setText('List of all students')

        self.add_student = QPushButton(self)
        self.add_student.setText('Add student')

        self.delete_student = QPushButton(self)
        self.delete_student.setText('Delete student')

        self.info = QPushButton(self)
        self.info.setText('Group information')

        self.back = QPushButton(self)
        self.back.setText('BACK')

        self.initUi()
    
    def initUi(self):

        self.bootcamp = QLabel('BOOTCAMP N3',self)

        self.foundation = QLabel('FOUNDATION',self)

        self.bootcamp.setStyleSheet(
            'color: blue;'
            'font-size: 60px;'
            'font-weight: bold;'
        )

        self.foundation.setStyleSheet(
            'color: blue;'
            'font-size: 60px;'
            'font-weight: bold;'
        )
        
        self.footer_label.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 15px'
        )

        self.table_pupils.setStyleSheet(
            'background-color: lightblue; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.table_pupils.setFixedSize(300,80)

        self.add_student.setStyleSheet(
            'background-color: lightblue; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.add_student.setFixedSize(300,80)

        self.delete_student.setStyleSheet(
            'background-color: lightblue; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.delete_student.setFixedSize(300,80)

        self.info.setStyleSheet(
            'background-color: lightblue; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )

        self.back.setStyleSheet(
            'background-color: lightgreen; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.back.setFixedSize(90,50)



        self.info.setFixedSize(300,80)

        self.foundation.move(10, 10)
        self.bootcamp.move(10, 70)

        self.table_pupils.move(100, 150)
        self.add_student.move(100,250)
        self.delete_student.move(100, 350)
        self.info.move(100, 450)
        self.back.move(10, 545)

        self.footer_label.move(115, 570)

        self.back.clicked.connect(self.press_btn_back)

        self.table_pupils.clicked.connect(self.table_students)

        self.add_student.clicked.connect(self.press_btn_add_student)

        self.delete_student.clicked.connect(self.press_btn_delete_student)

        self.info.clicked.connect(self.press_btn_info)

        # self.show()
    
    def press_btn_back(self):
        self.close()
        self.secondPage = SecondPage()
        self.secondPage.show()
    
    def table_students(self):
        self.close()
        self.bfn3Page = bfn3Page()
        self.bfn3Page.show()

    def press_btn_add_student(self):
        self.bfn3_add_student = bfn3_add_student()
        self.close()
        self.bfn3_add_student.show()
    
    def press_btn_delete_student(self):
        self.delete_student_bfn3 = delete_student_bfn3()
        self.close()
        self.delete_student.show()
    
    def press_btn_info(self):
        self.get_info_bfn3 = get_info_bfn3()
        self.close()
        self.get_info_bfn3.show()
    



class thirdPage3(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(500,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("Group Bootcamp Foundation N 32")

        self.footer_label = QLabel('© 2023 Najot Ta\'lim Group Foundation N 32',self)


        self.table_pupils = QPushButton(self)
        self.table_pupils.setText('List of all students')

        self.add_student = QPushButton(self)
        self.add_student.setText('Add student')

        self.delete_student = QPushButton(self)
        self.delete_student.setText('Delete student')

        self.info = QPushButton(self)
        self.info.setText('Group information')

        self.back = QPushButton(self)
        self.back.setText('BACK')

        self.initUi()
    
    def initUi(self):

        self.bootcamp = QLabel('BOOTCAMP N32',self)

        self.foundation = QLabel('FOUNDATION',self)

        self.bootcamp.setStyleSheet(
            'color: blue;'
            'font-size: 60px;'
            'font-weight: bold;'
        )

        self.foundation.setStyleSheet(
            'color: blue;'
            'font-size: 60px;'
            'font-weight: bold;'
        )
        
        self.footer_label.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 15px'
        )

        self.table_pupils.setStyleSheet(
            'background-color: lightblue; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.table_pupils.setFixedSize(300,80)

        self.add_student.setStyleSheet(
            'background-color: lightblue; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.add_student.setFixedSize(300,80)

        self.delete_student.setStyleSheet(
            'background-color: lightblue; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.delete_student.setFixedSize(300,80)

        self.info.setStyleSheet(
            'background-color: lightblue; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )

        self.back.setStyleSheet(
            'background-color: lightgreen; '
            'font: 20px;'
            'font-weight: bold;'
            'color : #fff;'
            'border: 2px solid #4169E1;'
            'padding: 5px 15px;'
            'margin-top: 10px;'
            'outline: 0px;'
            'border-radius : 30'
        )
        self.back.setFixedSize(90,50)



        self.info.setFixedSize(300,80)

        self.foundation.move(10, 10)
        self.bootcamp.move(10, 70)

        self.table_pupils.move(100, 150)
        self.add_student.move(100,250)
        self.delete_student.move(100, 350)
        self.info.move(100, 450)
        self.back.move(10, 545)

        self.footer_label.move(115, 570)

        self.back.clicked.connect(self.press_btn_back)

        self.table_pupils.clicked.connect(self.press_btn_show_table)

        self.add_student.clicked.connect(self.press_btn_add_student)

        self.delete_student.clicked.connect(self.press_btn_delete_student)

        self.info.clicked.connect(self.press_btn_info)

        self.show()
    
    def press_btn_back(self):
        self.close()
        self.secondPage = SecondPage()
        self.secondPage.show()
    
    def press_btn_show_table(self):
        self.bfn32page = bfn32Page()
        self.close()
        self.bfn32page.show()
    
    def press_btn_add_student(self):
        self.close()
        self.btn32_add_student = bfn32_add_student()
        self.btn32_add_student.show()
    
    def press_btn_delete_student(self):
        self.close()
        self.bfn32_del_student = delete_student_bfn32()
        self.bfn32_del_student.show()
    
    def press_btn_info(self):
        self.close()
        self.get_info_bfn32 = get_info_bfn32()
        self.get_info_bfn32.show()


class bfn3Page(QWidget):
    def __init__(self):
        super().__init__()

        self.btn_exit = QPushButton(self)
        self.btn_exit.setText("BACK")
        self.btn_exit.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )
        
        self.v_box = QVBoxLayout()
        
        self.qlw = QListWidget()

        self.v_box.addWidget(self.qlw)
        self.v_box.addWidget(self.btn_exit)

        self.setLayout(self.v_box)

        self.setFixedSize(500,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("Group Bootcamp Foundation N 3")

        # self.footer_label = QLabel('© 2023 Najot Ta\'lim Group Foundation N 32',self)

        self.show_data()

        self.btn_exit.clicked.connect(self.press_exit)


    def show_data(self):
        try:
            with mydb.cursor() as cursor:
                sql = f"""
                select * from bfn3           
                """
                cursor.execute(sql)
                result = cursor.fetchall()

                for i in result:
                    self.i = self
                    self.i.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )
                    self.i = str(i)
                    self.qlw.addItem(self.i[2:-3])
        except Exception as err:
            print(err)


    def press_exit(self):
        self.two = thirdPage2()
        self.close()
        self.two.show()
    

class bfn3_add_student(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("Group Bootcamp Foundation N 3")

        self.footer_label = QLabel('© 2023 Najot Ta\'lim Group Foundation N 3',self)

        self.initUi()

    def initUi(self):

        self.add_student = QLabel('ADD A',self)
        self.add_student.setStyleSheet(
            'color: blue;'
            'font-size: 70px;'
            'font-weight: bold;'
        )

        self.add_student2 = QLabel('STUDENT',self)
        self.add_student2.setStyleSheet(
            'color: red;'
            'font-size: 70px;'
            'font-weight: bold;'   
        )

        self.full_name = QLineEdit(self)
        self.full_name.setFixedSize(200,40)
        self.full_name.setPlaceholderText('FULL NAME')
        self.full_name.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 20px'
            )

        self.footer_label.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 15px'
        )

        self.btn_add = QPushButton('ADD STUDENT',self)
        self.btn_add.setFixedSize(200,40)
        self.btn_add.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )

        self.back = QPushButton('BACK',self)
        self.back.setFixedSize(200,40)
        self.back.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )
        
        self.full_name.move(135, 230)
        self.btn_add.move(135, 280)
        self.back.move(135,330)

        self.add_student.move(70, 20)
        self.add_student2.move(150, 100)

        self.footer_label.move(110, 570)

        self.show()

        self.btn_add.clicked.connect(self.press_btn_add)

        self.back.clicked.connect(self.press_btn_back)
    
    def press_btn_back(self):
        self.thirdPage2 = thirdPage2()
        self.close()
        self.thirdPage2.show()
    
    def press_btn_add(self):
        try:         
            name = self.full_name.text()     

            sql = "insert into bfn3 (full_name) values (%s)"
            val = ([f'{name}'])
            mycursor.execute(sql,val)

        except Exception as err:
            print(err)
        else:
            print('norm')
            self.full_name.clear()
            self.full_name.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 20px;'
            'border: 2px solid green;'
            )

class delete_student_bfn3(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("Group Bootcamp Foundation N 3")

        self.footer_label = QLabel('© 2023 Najot Ta\'lim Group Foundation N 3',self)

        self.initUi()

    def initUi(self):

        self.add_student = QLabel('DELETE A',self)
        self.add_student.setStyleSheet(
            'color: blue;'
            'font-size: 70px;'
            'font-weight: bold;'
        )

        self.add_student2 = QLabel('STUDENT',self)
        self.add_student2.setStyleSheet(
            'color: red;'
            'font-size: 70px;'
            'font-weight: bold;'   
        )

        self.full_name = QLineEdit(self)
        self.full_name.setFixedSize(200,40)
        self.full_name.setPlaceholderText('FULL NAME')
        self.full_name.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 20px'
            )

        self.footer_label.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 15px'
        )

        self.btn_add = QPushButton('DELETE STUDENT',self)
        self.btn_add.setFixedSize(200,40)
        self.btn_add.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )
        
        self.back = QPushButton('BACK',self)
        self.back.setFixedSize(200,40)
        self.back.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )
        
        self.full_name.move(135, 230)
        self.btn_add.move(135, 280)
        self.back.move(135,330)

        self.add_student.move(70, 20)
        self.add_student2.move(150, 100)

        self.footer_label.move(110, 570)

        self.show()

        self.btn_add.clicked.connect(self.press_btn_add)

        self.back.clicked.connect(self.press_btn_back)
    
    def press_btn_back(self):
        self.thirdPage2 = thirdPage2()
        self.close()
        self.thirdPage2.show()

    
    def press_btn_add(self):
        try:         
            name = self.full_name.text()     

            sql = "delete from bfn3 where full_name = (%s)"
            val = ([f'{name}'])
            mycursor.execute(sql,val)

            mydb.commit()

        except Exception as err:
            print(err)
        else:
            print('norm')
            self.full_name.clear()
            self.full_name.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 20px;'
            'border: 2px solid green;'
            )

class get_info_bfn3(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(580,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("INFO BOOTCAMO FOUNDATION N3")

        self.initUi()

        self.show()

    def initUi(self):

        self.head_teacher = QLabel('HEAD TEACHER',self)
        self.head_teacher.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_head_teacher = QLabel('SHAKIROV AZIZ',self)
        self.name_head_teacher.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.assistant_teacher = QLabel('ASSISTANT TEACHER',self)
        self.assistant_teacher.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_assistant_teacher = QLabel('ABDURAHMONOV ISLOM',self)
        self.name_assistant_teacher.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )
        
        self.romm = QLabel('ROOM',self)
        self.romm.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_room = QLabel('MICROSOFT',self)
        self.name_room.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.floor = QLabel('FLOOR',self)
        self.floor.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_floor = QLabel('3RD FLOOR',self)
        self.name_floor.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.academic_moths = QLabel('ACADEMIC MONTH',self)
        self.academic_moths.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_academic_months = QLabel('5TH MONTH',self)
        self.name_academic_months.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.branch = QLabel('BRANCH',self)
        self.branch.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_branch = QLabel('CHILONZOR',self)
        self.name_branch.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.class_time = QLabel('CLASS TIME',self)
        self.class_time.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_class_time = QLabel('13:30',self)
        self.name_class_time.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.lesson_duration = QLabel('LESSON DURATION',self)
        self.lesson_duration.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_lesson_duration = QLabel('3 HOURS',self)
        self.name_lesson_duration.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.direction = QLabel('DIRECTION',self)
        self.direction.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_direction = QLabel('PROGRAMMING',self)
        self.name_direction.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )
        
        self.school_days = QLabel('SCHOOL DAYS',self)
        self.school_days.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_school_days = QLabel('5 DAYS',self)
        self.name_school_days.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.head_teacher.move(10, 20)
        self.name_head_teacher.move(280,20)

        self.assistant_teacher.move(10, 60)
        self.name_assistant_teacher.move(280,60)

        self.romm.move(10,100)
        self.name_room.move(280,100)

        self.floor.move(10,140)
        self.name_floor.move(280,140)

        self.academic_moths.move(10,180)
        self.name_academic_months.move(280,180)

        self.branch.move(10, 220)
        self.name_branch.move(280,220)

        self.class_time.move(10, 260)
        self.name_class_time.move(280, 260)

        self.lesson_duration.move(10, 300)
        self.name_lesson_duration.move(280,300)

        self.direction.move(10, 340)
        self.name_direction.move(280,340)

        self.school_days.move(10,380)
        self.name_school_days.move(280, 380)

        self.back = QPushButton('BACK',self)
        self.back.setFixedSize(200,40)
        self.back.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )
        
        self.back.move(170, 450)

        self.back.clicked.connect(self.press_btn_back)
    
    def press_btn_back(self):
        self.thirdPage2 = thirdPage2()
        self.close()
        self.thirdPage2.show()


class bfn2Page(QWidget):
    def __init__(self):
        super().__init__()

        self.btn_exit = QPushButton(self)
        self.btn_exit.setText("BACK")
        self.btn_exit.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )
        
        self.v_box = QVBoxLayout()
        
        self.qlw = QListWidget()

        self.v_box.addWidget(self.qlw)
        self.v_box.addWidget(self.btn_exit)

        self.setLayout(self.v_box)

        self.setFixedSize(500,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("Group Bootcamp Foundation N 2")

        # self.footer_label = QLabel('© 2023 Najot Ta\'lim Group Foundation N 32',self)

        self.show_data()

        self.btn_exit.clicked.connect(self.press_exit)


    def show_data(self):
        try:
            with mydb.cursor() as cursor:
                sql = f"""
                select * from bfn2           
                """
                cursor.execute(sql)
                result = cursor.fetchall()

                for i in result:
                    self.i = self
                    self.i.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )
                    self.i = str(i)
                    self.qlw.addItem(self.i[2:-3])
        except Exception as err:
            print(err)


    def press_exit(self):
        self.two = thirdPage1()
        self.close()
        self.two.show()



class bfn2_add_student(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("Group Bootcamp Foundation N 2")

        self.footer_label = QLabel('© 2023 Najot Ta\'lim Group Foundation N 2',self)

        self.initUi()

    def initUi(self):

        self.add_student = QLabel('ADD A',self)
        self.add_student.setStyleSheet(
            'color: blue;'
            'font-size: 70px;'
            'font-weight: bold;'
        )

        self.add_student2 = QLabel('STUDENT',self)
        self.add_student2.setStyleSheet(
            'color: red;'
            'font-size: 70px;'
            'font-weight: bold;'   
        )

        self.full_name = QLineEdit(self)
        self.full_name.setFixedSize(200,40)
        self.full_name.setPlaceholderText('FULL NAME')
        self.full_name.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 20px'
            )

        self.footer_label.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 15px'
        )

        self.btn_add = QPushButton('ADD STUDENT',self)
        self.btn_add.setFixedSize(200,40)
        self.btn_add.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )

        self.back = QPushButton('BACK',self)
        self.back.setFixedSize(200,40)
        self.back.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )
        
        self.full_name.move(135, 230)
        self.btn_add.move(135, 280)
        self.back.move(135,330)

        self.add_student.move(70, 20)
        self.add_student2.move(150, 100)

        self.footer_label.move(110, 570)

        self.show()

        self.btn_add.clicked.connect(self.press_btn_add)

        self.back.clicked.connect(self.press_btn_back)
    
    def press_btn_back(self):
        self.thirdPage1 = thirdPage1()
        self.close()
        self.thirdPage1.show()
    
    def press_btn_add(self):
        try:         
            name = self.full_name.text()     

            sql = "insert into bfn2 (full_name) values (%s)"
            val = ([f'{name}'])
            mycursor.execute(sql,val)

            mydb.commit()

        except Exception as err:
            print(err)
        else:
            print('norm')
            self.full_name.clear()
            self.full_name.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 20px;'
            'border: 2px solid green;'
            )



class delete_student_bfn2(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("Group Bootcamp Foundation N 2")

        self.footer_label = QLabel('© 2023 Najot Ta\'lim Group Foundation N 2',self)

        self.initUi()

    def initUi(self):

        self.add_student = QLabel('DELETE A',self)
        self.add_student.setStyleSheet(
            'color: blue;'
            'font-size: 70px;'
            'font-weight: bold;'
        )

        self.add_student2 = QLabel('STUDENT',self)
        self.add_student2.setStyleSheet(
            'color: red;'
            'font-size: 70px;'
            'font-weight: bold;'   
        )

        self.full_name = QLineEdit(self)
        self.full_name.setFixedSize(200,40)
        self.full_name.setPlaceholderText('FULL NAME')
        self.full_name.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 20px'
            )

        self.footer_label.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 15px'
        )

        self.btn_add = QPushButton('DELETE STUDENT',self)
        self.btn_add.setFixedSize(200,40)
        self.btn_add.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )
        
        self.back = QPushButton('BACK',self)
        self.back.setFixedSize(200,40)
        self.back.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )
        
        self.full_name.move(135, 230)
        self.btn_add.move(135, 280)
        self.back.move(135,330)

        self.add_student.move(70, 20)
        self.add_student2.move(150, 100)

        self.footer_label.move(110, 570)

        self.show()

        self.btn_add.clicked.connect(self.press_btn_add)

        self.back.clicked.connect(self.press_btn_back)
    
    def press_btn_back(self):
        self.thirdPage1 = thirdPage1()
        self.close()
        self.thirdPage1.show()

    
    def press_btn_add(self):
        try:         
            name = self.full_name.text()     

            sql = "delete from bfn2 where full_name = (%s)"
            val = ([f'{name}'])
            mycursor.execute(sql,val)

            mydb.commit()

        except Exception as err:
            print(err)
        else:
            print('norm')
            self.full_name.clear()
            self.full_name.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 20px;'
            'border: 2px solid green;'
            )



class get_info_bfn2(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(580,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("INFO BOOTCAMO FOUNDATION N2")

        self.initUi()

        self.show()

    def initUi(self):

        self.head_teacher = QLabel('HEAD TEACHER',self)
        self.head_teacher.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_head_teacher = QLabel('SHAKIROV AZIZ',self)
        self.name_head_teacher.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.assistant_teacher = QLabel('ASSISTANT TEACHER',self)
        self.assistant_teacher.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_assistant_teacher = QLabel('ESHMATOV TOSHMAT',self)
        self.name_assistant_teacher.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )
        
        self.romm = QLabel('ROOM',self)
        self.romm.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_room = QLabel('FACEBOOK',self)
        self.name_room.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.floor = QLabel('FLOOR',self)
        self.floor.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_floor = QLabel('2ND FLOOR',self)
        self.name_floor.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.academic_moths = QLabel('ACADEMIC MONTH',self)
        self.academic_moths.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_academic_months = QLabel('5TH MONTH',self)
        self.name_academic_months.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.branch = QLabel('BRANCH',self)
        self.branch.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_branch = QLabel('CHILONZOR',self)
        self.name_branch.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.class_time = QLabel('CLASS TIME',self)
        self.class_time.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_class_time = QLabel('09:00',self)
        self.name_class_time.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.lesson_duration = QLabel('LESSON DURATION',self)
        self.lesson_duration.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_lesson_duration = QLabel('3 HOURS',self)
        self.name_lesson_duration.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.direction = QLabel('DIRECTION',self)
        self.direction.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_direction = QLabel('PROGRAMMING',self)
        self.name_direction.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )
        
        self.school_days = QLabel('SCHOOL DAYS',self)
        self.school_days.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_school_days = QLabel('5 DAYS',self)
        self.name_school_days.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.head_teacher.move(10, 20)
        self.name_head_teacher.move(280,20)

        self.assistant_teacher.move(10, 60)
        self.name_assistant_teacher.move(280,60)

        self.romm.move(10,100)
        self.name_room.move(280,100)

        self.floor.move(10,140)
        self.name_floor.move(280,140)

        self.academic_moths.move(10,180)
        self.name_academic_months.move(280,180)

        self.branch.move(10, 220)
        self.name_branch.move(280,220)

        self.class_time.move(10, 260)
        self.name_class_time.move(280, 260)

        self.lesson_duration.move(10, 300)
        self.name_lesson_duration.move(280,300)

        self.direction.move(10, 340)
        self.name_direction.move(280,340)

        self.school_days.move(10,380)
        self.name_school_days.move(280, 380)

        self.back = QPushButton('BACK',self)
        self.back.setFixedSize(200,40)
        self.back.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )
        
        self.back.move(170, 450)

        self.back.clicked.connect(self.press_btn_back)
    
    def press_btn_back(self):
        self.thirdPage1 = thirdPage1()
        self.close()
        self.thirdPage1.show()



class bfn32Page(QWidget):
    def __init__(self):
        super().__init__()

        self.btn_exit = QPushButton(self)
        self.btn_exit.setText("BACK")
        self.btn_exit.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )
        
        self.v_box = QVBoxLayout()
        
        self.qlw = QListWidget()

        self.v_box.addWidget(self.qlw)
        self.v_box.addWidget(self.btn_exit)

        self.setLayout(self.v_box)

        self.setFixedSize(500,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("Group Bootcamp Foundation N 32")

        # self.footer_label = QLabel('© 2023 Najot Ta\'lim Group Foundation N 32',self)

        self.show_data()

        self.btn_exit.clicked.connect(self.press_exit)


    def show_data(self):
        try:
            with mydb.cursor() as cursor:
                sql = f"""
                select * from bfn32           
                """
                cursor.execute(sql)
                result = cursor.fetchall()

                for i in result:
                    self.i = self
                    self.i.setStyleSheet(
                    'color: black;'
                    'font-size: 20px;'
                    'font-weight: bold;'   
                    )
                    self.i = str(i)
                    self.qlw.addItem(self.i[2:-3])
        except Exception as err:
            print(err)


    def press_exit(self):
        self.two = thirdPage3()
        self.close()
        self.two.show()



class bfn32_add_student(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("Group Bootcamp Foundation N 32")

        self.footer_label = QLabel('© 2023 Najot Ta\'lim Group Foundation N 32',self)

        self.initUi()

    def initUi(self):

        self.add_student = QLabel('ADD A',self)
        self.add_student.setStyleSheet(
            'color: blue;'
            'font-size: 70px;'
            'font-weight: bold;'
        )

        self.add_student2 = QLabel('STUDENT',self)
        self.add_student2.setStyleSheet(
            'color: red;'
            'font-size: 70px;'
            'font-weight: bold;'   
        )

        self.full_name = QLineEdit(self)
        self.full_name.setFixedSize(200,40)
        self.full_name.setPlaceholderText('FULL NAME')
        self.full_name.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 20px'
            )

        self.footer_label.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 15px'
        )

        self.btn_add = QPushButton('ADD STUDENT',self)
        self.btn_add.setFixedSize(200,40)
        self.btn_add.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )

        self.back = QPushButton('BACK',self)
        self.back.setFixedSize(200,40)
        self.back.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )
        
        self.full_name.move(135, 230)
        self.btn_add.move(135, 280)
        self.back.move(135,330)

        self.add_student.move(70, 20)
        self.add_student2.move(150, 100)

        self.footer_label.move(110, 570)

        self.show()

        self.btn_add.clicked.connect(self.press_btn_add)

        self.back.clicked.connect(self.press_btn_back)
    
    def press_btn_back(self):
        self.thirdPage3 = thirdPage3()
        self.close()
        self.thirdPage3.show()
    
    def press_btn_add(self):
        try:         
            name = self.full_name.text()     

            sql = "insert into bfn32 (full_name) values (%s)"
            val = ([f'{name}'])
            mycursor.execute(sql,val)

            mydb.commit()

        except Exception as err:
            print(err)
        else:
            print('norm')
            self.full_name.clear()
            self.full_name.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 20px;'
            'border: 2px solid green;'
            )


class delete_student_bfn32(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("Group Bootcamp Foundation N 32")

        self.footer_label = QLabel('© 2023 Najot Ta\'lim Group Foundation N 32',self)

        self.initUi()

    def initUi(self):

        self.add_student = QLabel('DELETE A',self)
        self.add_student.setStyleSheet(
            'color: blue;'
            'font-size: 70px;'
            'font-weight: bold;'
        )

        self.add_student2 = QLabel('STUDENT',self)
        self.add_student2.setStyleSheet(
            'color: red;'
            'font-size: 70px;'
            'font-weight: bold;'   
        )

        self.full_name = QLineEdit(self)
        self.full_name.setFixedSize(200,40)
        self.full_name.setPlaceholderText('FULL NAME')
        self.full_name.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 20px'
            )

        self.footer_label.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 15px'
        )

        self.btn_add = QPushButton('DELETE STUDENT',self)
        self.btn_add.setFixedSize(200,40)
        self.btn_add.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )
        
        self.back = QPushButton('BACK',self)
        self.back.setFixedSize(200,40)
        self.back.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )
        
        self.full_name.move(135, 230)
        self.btn_add.move(135, 280)
        self.back.move(135,330)

        self.add_student.move(70, 20)
        self.add_student2.move(150, 100)

        self.footer_label.move(110, 570)

        self.show()

        self.btn_add.clicked.connect(self.press_btn_add)

        self.back.clicked.connect(self.press_btn_back)
    
    def press_btn_back(self):
        self.thirdPage3 = thirdPage3()
        self.close()
        self.thirdPage3.show()

    
    def press_btn_add(self):
        try:         
            name = self.full_name.text()     

            sql = "delete from bfn32 where full_name = (%s)"
            val = ([f'{name}'])
            mycursor.execute(sql,val)

            mydb.commit()

        except Exception as err:
            print(err)
        else:
            print('norm')
            self.full_name.clear()
            self.full_name.setStyleSheet(
            'border-width: 2px;'
            'border-radius: 8px;'
            'border-style: solid;'
            'background-color: #f4f4f4;'
            'color: #3d3d3d;'
            'font-weight: bold;'
            'font: 20px;'
            'border: 2px solid green;'
            )

class get_info_bfn32(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(580,600)

        self.setStyleSheet('background-color: #F0FFFF;')

        self.setWindowTitle("INFO BOOTCAMO FOUNDATION N32")

        self.initUi()

        self.show()

    def initUi(self):

        self.head_teacher = QLabel('HEAD TEACHER',self)
        self.head_teacher.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_head_teacher = QLabel('SHAKIROV AZIZ',self)
        self.name_head_teacher.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.assistant_teacher = QLabel('ASSISTANT TEACHER',self)
        self.assistant_teacher.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_assistant_teacher = QLabel('TOSHMATOV QULMAMAT',self)
        self.name_assistant_teacher.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )
        
        self.romm = QLabel('ROOM',self)
        self.romm.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_room = QLabel('AMAZON',self)
        self.name_room.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.floor = QLabel('FLOOR',self)
        self.floor.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_floor = QLabel('2ND FLOOR',self)
        self.name_floor.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.academic_moths = QLabel('ACADEMIC MONTH',self)
        self.academic_moths.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_academic_months = QLabel('5TH MONTH',self)
        self.name_academic_months.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.branch = QLabel('BRANCH',self)
        self.branch.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_branch = QLabel('CHILONZOR',self)
        self.name_branch.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.class_time = QLabel('CLASS TIME',self)
        self.class_time.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_class_time = QLabel('18:00',self)
        self.name_class_time.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.lesson_duration = QLabel('LESSON DURATION',self)
        self.lesson_duration.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_lesson_duration = QLabel('3 HOURS',self)
        self.name_lesson_duration.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.direction = QLabel('DIRECTION',self)
        self.direction.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_direction = QLabel('PROGRAMMING',self)
        self.name_direction.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )
        
        self.school_days = QLabel('SCHOOL DAYS',self)
        self.school_days.setStyleSheet(
            'color: blue;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.name_school_days = QLabel('5 DAYS',self)
        self.name_school_days.setStyleSheet(
            'color: black;'
            'font-size: 20px;'
            'font-weight: bold;'
        )

        self.head_teacher.move(10, 20)
        self.name_head_teacher.move(280,20)

        self.assistant_teacher.move(10, 60)
        self.name_assistant_teacher.move(280,60)

        self.romm.move(10,100)
        self.name_room.move(280,100)

        self.floor.move(10,140)
        self.name_floor.move(280,140)

        self.academic_moths.move(10,180)
        self.name_academic_months.move(280,180)

        self.branch.move(10, 220)
        self.name_branch.move(280,220)

        self.class_time.move(10, 260)
        self.name_class_time.move(280, 260)

        self.lesson_duration.move(10, 300)
        self.name_lesson_duration.move(280,300)

        self.direction.move(10, 340)
        self.name_direction.move(280,340)

        self.school_days.move(10,380)
        self.name_school_days.move(280, 380)

        self.back = QPushButton('BACK',self)
        self.back.setFixedSize(200,40)
        self.back.setStyleSheet(
            'background-color: #0d6efd;'
            'color: #fff;'
            'font-weight: 600;'
            'border-radius: 8px;'
            'border: 2px solid black;'
            )
        
        self.back.move(170, 450)

        self.back.clicked.connect(self.press_btn_back)
    
    def press_btn_back(self):
        self.thirdPage3 = thirdPage3()
        self.close()
        self.thirdPage3.show()


app = QApplication(sys.argv)

win = MainWindow()

sys.exit(app.exec_())

#  Python program to create a simple Flames game using PyQt5   
# import all required libraries  









