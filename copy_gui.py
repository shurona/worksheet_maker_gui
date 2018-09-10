import exercise

import sys

from PyQt5.QtWidgets import *

from PyQt5.QtCore import  *

from PyQt5.QtGui import *


class Labels(QMainWindow) :


    def __init__(self):

        super().__init__()

        self.initUi()



    def initUi(self) :



        self.setWindowTitle("라벨지 선택")

        self.new_screen = new_Window()

        #라벨지 생성 button
        make_window_btn = QPushButton("원하는 라벨지 선택",self)

        make_window_btn.move(70,40)

        make_window_btn.resize(150,50)

        make_window_btn.clicked.connect(self.buttonClicked_2)

        self.setGeometry(300,300,400,300)

        self.show()


    def buttonClicked_2(self):

        self.new_screen.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


class new_Window(QWidget):


    def __init__(self):

        super().__init__()

        self.window_screen()



    def window_screen(self):

        self.setWindowTitle("Test")
        self.setGeometry(300,300,400,450)

        grid = QGridLayout()
        grid.setSpacing(10)

        show_label = QLabel('원하시는 사진을 선택하세요')
        grid.addWidget(show_label,0,0)


        # 그림 넣을 레이블 생성

        self.left_lb = QLabel(self)
        self.right_lb = QLabel(self)

        self.picture_set()

        grid.addWidget(self.left_lb,1,0,3,2)
        grid.addWidget(self.right_lb,1,3,3,2)


        #radio 버튼
        self.radiobutton_left = QRadioButton('Picture select')
        self.radiobutton_left.setChecked(0)

        self.radiobutton_right = QRadioButton('Picture select')
        self.radiobutton_right.setChecked(0)

        grid.addWidget(self.radiobutton_left,6,0)
        grid.addWidget(self.radiobutton_right,6,3)

        #하단 버튼
        self.check_number = 0

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        okButton.clicked.connect(self.okbutton_cliecked)
        okButton.clicked.connect(self.close)
        cancelButton.clicked.connect(self.cancelButton_clicked)
        cancelButton.clicked.connect(self.close)

        hbox  = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        grid.addLayout(hbox,7,3)

        grid.setColumnStretch(0,8)

        self.setLayout(grid)

    def okbutton_cliecked(self):

        # OK 버튼 눌렀을 시 상황
        if self.radiobutton_left.isChecked() == True :

            print_label = exercise.CopyPic()

            print_label.rec_size(24)
            print_label.rec_filepath('D:\Pic/')
            print_label.excute_copy()

            for i in print_label.makedfile_list :
                print(i)

            print(len(print_label.makedfile_list))

            print("복사완료")

        elif self.radiobutton_right.isChecked() == True :

            print_label = exercise.CopyPic()

            print_label.rec_size(21)
            print_label.rec_filepath('D:\Pic/')
            print_label.excute_copy()

            print("복사완료")

        else :
            pass

    def cancelButton_clicked(self):
        self.choosed_picture = 0

    def picture_set(self):
        #그림 정하기
        fname_left = 'D:/Pic/a.PNG'
        fname_right = 'D:/Pic/b.PNG'

        pixmap_left = QPixmap(fname_left)
        pixmap_right = QPixmap(fname_right)

        #라벨에 이미지 넣기
        height_label = 300
        width_label = 200

        self.left_lb.resize(width_label, height_label)
        self.left_lb.setPixmap(pixmap_left.scaled(self.left_lb.size()))

        self.right_lb.resize(width_label, height_label)
        self.right_lb.setPixmap(pixmap_right.scaled(self.right_lb.size()))


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__" :

    app = QApplication(sys.argv)

    lable = Labels()

    sys.exit(app.exec_())