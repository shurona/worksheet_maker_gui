from basic_gui import *
from PyQt5.QtWidgets import (QRadioButton, QGroupBox, QCheckBox)
from PyQt5.QtGui import QIcon
import wordsearch_generater

class Communication(Communication):
    super(Communication)
    # signal for puzzle settings
    puzzle_setting = pyqtSignal(list)
    # emits if entered words are korean
    korean = pyqtSignal(bool)
    # siganl to notify that making wordsearch puzzle is complete and to proceed the following
    puzzle_complete = pyqtSignal()
    recursionerrormsg = pyqtSignal()


class Settings(QWidget):
    def __init__(self, c):
        super().__init__()
        self.c = c
        self.puzzle_width = 15
        self.puzzle_height = 15
        self.diff = '가로세로'
        self.diff_val = 1
        self.option = '겹치지 않도록'
        self.option_val = 0
        self.init_UI()

    def init_UI(self):
        title_label = QLabel("1. 퍼즐 옵션을 선택하세요.")

        grp_size = QGroupBox("크기 조정")
        self.label_puzzle_width = QLabel('가로 길이: ')
        self.width_spin = QSpinBox()
        self.width_spin.setToolTip('마우스 스크롤 가능합니다.')
        self.width_spin.setValue(15)

        self.label_puzzle_height = QLabel('세로 길이: ')
        self.height_spin = QSpinBox()
        self.height_spin.setToolTip('마우스 스크롤 가능합니다.')
        self.height_spin.setValue(15)
        self.height_spin.valueChanged.connect(self.puzzle_height_change)

        # layout width
        hbox_width = QHBoxLayout()
        hbox_width_label = QHBoxLayout()
        hbox_width_label.setAlignment(Qt.AlignRight)
        hbox_width_label.addWidget(self.label_puzzle_width)
        hbox_width.addLayout(hbox_width_label)
        hbox_width_spin = QHBoxLayout()
        hbox_width_spin.setAlignment(Qt.AlignLeft)
        hbox_width_spin.addWidget(self.width_spin)
        hbox_width.addLayout(hbox_width_spin)
        self.width_spin.valueChanged.connect(self.puzzle_width_change)

        # layout height
        hbox_height = QHBoxLayout()
        hbox_height_label = QHBoxLayout()
        hbox_height_label.setAlignment(Qt.AlignRight)
        hbox_height_label.addWidget(self.label_puzzle_height)
        hbox_height_spin = QHBoxLayout()
        hbox_height_spin.setAlignment(Qt.AlignLeft)
        hbox_height_spin.addWidget(self.height_spin)
        hbox_height.addLayout(hbox_height_label)
        hbox_height.addLayout(hbox_height_spin)

        # layout for width, height
        vbox_size = QVBoxLayout()
        vbox_size.addLayout(hbox_width)
        vbox_size.addLayout(hbox_height)

        grp_size.setLayout(vbox_size)

        self.label_explain = QLabel("난이도 : 글자 방향은 <font color='yellow'>가로세로</font>, 채워지는 글자는 되도록  <font color='yellow'>겹치지 않도록</font> 설정합니다.")

        grp_difficulty = QGroupBox("난이도")
        diff_1 = QRadioButton("난이도 1")
        diff_1.setToolTip("<p style='white-space:pre'>글자 방향은 <font color='yellow'>가로세로로</font> 설정합니다.")
        diff_1.setChecked(True)
        diff_2 = QRadioButton("난이도 2")
        diff_2.setToolTip("<p style='white-space:pre'>글자 방향은 <font color='yellow'>가로세로, 가로세로 거꾸로</font> 설정합니다.")
        diff_3 = QRadioButton("난이도 3")
        diff_3.setToolTip("<p style='white-space:pre'>글자 방향은 <font color='yellow'>가로세로 그리고 대각선으로</font> 설정합니다.")
        diff_4 = QRadioButton("난이도 4")
        diff_4.setToolTip("<p style='white-space:pre'>글자 방향은 <font color='yellow'>가로세로, 가로세로 거꾸로 그리고 대각선으로</font> 설정합니다.")
        diff_5 = QRadioButton("난이도 5")
        diff_5.setToolTip("<p style='white-space:pre'>글자 방향은 <font color='yellow'>가로세로, 가로세로 거꾸로 그리고 대각선, 대각선 거꾸로</font> 설정합니다.")
        diff_1.clicked.connect(lambda: self.diff_checked(diff_1))
        diff_2.clicked.connect(lambda: self.diff_checked(diff_2))
        diff_3.clicked.connect(lambda: self.diff_checked(diff_3))
        diff_4.clicked.connect(lambda: self.diff_checked(diff_4))
        diff_5.clicked.connect(lambda: self.diff_checked(diff_5))
        placeholder = QLabel('')
        # layout difficulty
        grp_difficulty_layout = QVBoxLayout()
        """
        hbox_diff = QHBoxLayout()
        
        vbox_diff123 = QVBoxLayout()
        vbox_diff45 = QVBoxLayout()
        vbox_diff123.addWidget(diff_1)
        vbox_diff123.addWidget(diff_2)
        vbox_diff123.addWidget(diff_3)
        vbox_diff45.addWidget(diff_4)
        vbox_diff45.addWidget(diff_5)
        vbox_diff45.addWidget(placeholder)
        hbox_diff.addLayout(vbox_diff123)

        hbox_diff.addLayout((vbox_diff45))"""
        hbox_diff = QHBoxLayout()
        hbox_diff.addWidget(diff_1)
        hbox_diff.addWidget(diff_2)
        hbox_diff.addWidget(diff_3)
        hbox_diff.addWidget(diff_4)
        hbox_diff.addWidget(diff_5)
        grp_difficulty_layout.addLayout(hbox_diff)
        self.line_explain = QLineEdit("글자 방향은 가로세로로 설정합니다.")
        self.line_explain.setReadOnly(True)
        self.line_explain.setAlignment(Qt.AlignHCenter)
        grp_difficulty_layout.addWidget(self.line_explain)
        grp_difficulty.setLayout(grp_difficulty_layout)

        grp_option = QGroupBox("옵션")
        option_1 = QRadioButton("글자 겹치지 않게")
        option_1.setToolTip("퍼즐이 쉬워집니다. <p style='white-space:pre'>채워지는 글자는 되도록 <font color='yellow'>겹치지 않도록</font> 설정합니다.")
        option_1.setChecked(True)
        option_2 = QRadioButton("글자 무작위로")
        option_2.setToolTip("퍼즐 난이도는 보통입니다. <p style='white-space:pre'>채워지는 글자는 되도록 <font color='yellow'>무작위로</font> 설정합니다.")
        option_3 = QRadioButton("글자 겹치게")
        option_3.setToolTip("<p style='white-space:pre'>퍼즐이 어려워집니다. <p style='white-space:pre'>채워지는 글자는 되도록 <font color='yellow'>겹치도록</font> 설정합니다.")
        option_1.clicked.connect(lambda: self.option_checked(option_1))
        option_2.clicked.connect(lambda: self.option_checked(option_2))
        option_3.clicked.connect(lambda: self.option_checked(option_3))
        # layout option
        grp_option_layout = QVBoxLayout()
        grp_option_layout.addWidget(option_1)
        grp_option_layout.addWidget(option_2)
        grp_option_layout.addWidget(option_3)

        grp_option.setLayout(grp_option_layout)

        # layout for diplay
        vbox_display = QVBoxLayout()

        hbox_setting = QHBoxLayout()
        hbox_setting.addWidget(grp_size)
        hbox_setting.addWidget(grp_difficulty)
        hbox_setting.addWidget(grp_option)
        hbox_setting.setStretch(0, 1)
        hbox_setting.setStretch(1, 3)
        hbox_setting.setStretch(3, 1)

        vbox_display.addWidget(title_label)
        vbox_display.addLayout(hbox_setting)

        self.setLayout(vbox_display)
        self.show()

    def puzzle_width_change(self, value):
        self.puzzle_width = value
        self.c.puzzle_setting.emit([self.puzzle_width, self.puzzle_height, self.diff_val, self.option_val])

    def puzzle_height_change(self, value):
        self.puzzle_height = value
        self.c.puzzle_setting.emit([self.puzzle_width, self.puzzle_height, self.diff_val, self.option_val])

    def diff_checked(self, diff):
        text = diff.text()
        if text == '난이도 1':
            self.diff = "가로세로로"
            self.diff_val = 1
        elif text == '난이도 2':
            self.diff = "가로세로, 가로세로 거꾸로"
            self.diff_val = 2
        elif text == '난이도 3':
            self.diff = "가로세로, 대각선으로"
            self.diff_val = 3
        elif text == '난이도 4':
            self.diff = "가로세로, 가로세로 거꾸로, 대각선으로"
            self.diff_val = 4
        elif text == '난이도 5':
            self.diff = "가로세로, 가로세로 거꾸로, 대각선, 대각선 거꾸로"
            self.diff_val = 5
        self.set_line_explain()

    def option_checked(self, option):
        text = option.text()
        if text == '글자 겹치지 않게':
            self.option_val = 0
        elif text == '글자 무작위로':
            self.option_val = 1
        elif text == '글자 겹치게':
            self.option_val = 2
    def set_line_explain(self):
        self.line_explain.setText("방향을 {} 설정합니다.".format(self.diff))
        # self.line_explain.resize(self.line_explain.sizeHint())
        self.c.puzzle_setting.emit([self.puzzle_width, self.puzzle_height, self.diff_val, self.option_val])

class EnterWords(EnterWords):
    def set_words(self):
        search_target = self.input_words.toPlainText()
        regex = r'[a-zA-Z]+'
        self.words = list({word.lower() if word.isalpha() else word for word in re.findall(regex, search_target)})
        if not self.words:
            regex = r'[가-힣]+'
            self.words = list({word.lower() if word.isalpha() else word for word in re.findall(regex, search_target)})
            self.c.korean.emit(True)
        else:
            self.c.korean.emit(False)

class DownloadImage(DownloadImage):
    def __init__(self, c):
        super(DownloadImage, self).__init__(c)
        # initial puzzle settings
        self.width, self.height, self.diff, self.option = 15, 15, 1, 0
        # initialize download numbers
        self.picture_on = False
        # initialize language mode
        self.korean = False
        # initialize language mode
        self.chosung = False

    def init_UI(self):
        super(DownloadImage, self).init_UI()
        # get data of puzzle settings
        self.c.puzzle_setting.connect(self.puzzle_setting)
        # see if its korean or english/ default is english
        self.c.korean.connect(self.korean_on)


        self.chosung_checkBox = QCheckBox("초성", self)
        self.chosung_checkBox.setToolTip("단어가 초성으로 제시됩니다.")
        self.chosung_checkBox.close()
        self.chosung_checkBox.stateChanged.connect(self.chosung_on)

        self.make_puzzle_bt = QPushButton("Word Search 퍼즐 만들기")
        self.make_puzzle_bt.clicked.connect(self.make_puzzle)
        self.make_puzzle_bt.setToolTip("단축키 : Ctrl + D")
        self.make_puzzle_bt.setShortcut('Ctrl+D')

        hbox_puzzle_bt = QHBoxLayout()
        hbox_puzzle_bt.addStretch(1)
        hbox_puzzle_bt.addWidget(self.chosung_checkBox)
        hbox_puzzle_bt.addWidget(self.make_puzzle_bt)
        self.grid.addLayout(hbox_puzzle_bt, 3, 0, 1, 2)

    # define puzzle settings
    def puzzle_setting(self, puzzle_setting):
        self.width, self.height, self.diff, self.option = puzzle_setting[0], puzzle_setting[1], puzzle_setting[2], puzzle_setting[3]

    def korean_on(self, bool):
        self.korean = bool
        if bool == True:
            self.chosung_checkBox.show()
            self.make_puzzle_bt.setText('낱말 찾기 퍼즐 만들기')
        else:
            self.chosung_checkBox.close()
            self.make_puzzle_bt.setText('Word Search 퍼즐 만들기')
        self.make_puzzle_bt.setToolTip("단축키 : Ctrl + D")
        self.make_puzzle_bt.setShortcut('Ctrl+D')

    def chosung_on(self):
        if self.chosung_checkBox.isChecked() == True:
            self.chosung = True
        else:
            self.chosung = False

    def enable_buttons(self):
        self.download_bt.setEnabled(True)
        self.make_puzzle_bt.setEnabled(True)
        self.c.enable_set_keyword_bt.emit()

    def disable_buttons(self):
        self.download_bt.setEnabled(False)
        self.make_puzzle_bt.setEnabled(False)
        self.c.disable_set_keyword_bt.emit()

    def make_puzzle(self):
        word_image = []
        if self.tree.topLevelItemCount() == 0:
            self.start_download()
            return

        self.disable_buttons()

        if self.picture_on:
            iterator = QTreeWidgetItemIterator(self.tree, QTreeWidgetItemIterator.HasChildren)
        else:
            iterator = QTreeWidgetItemIterator(self.tree, QTreeWidgetItemIterator.All)
        while iterator.value():
            item = iterator.value()
            word = item.data(0, 0)
            pic = ''
            if self.picture_on:
                pic = item.path
                if not os.path.exists(pic):
                    self.c.press_set_keyword_bt.emit()
                    self.enable_buttons()
                    q = QMessageBox(self)
                    q.information(self, 'information', '선택하신 이미지가 존재하지 않습니다. 다시 다운로드 눌러주세요.', QMessageBox.Ok)
                    return
            word_image.append([word, pic])
            iterator += 1
        puzzle_worker = PuzzleWorker(wordsearch_generater.MakeWordSearch, word_image, self.width, self.height, self.diff,
                                                         self.option, self.picture_on, self.korean, self.chosung)
        puzzle_worker.signal.puzzle_complete.connect(self.puzzle_finish)
        puzzle_worker.signal.recursionerrormsg.connect(self.errormsg)
        self.threadpool.start(puzzle_worker)

    def puzzle_finish(self):
        q = QMessageBox(self)
        q.information(self, 'information', '바탕화면에 퍼즐 파일이 저장되었습니다.', QMessageBox.Ok)
        # TODO button, whether to open the file or not --> i should get the file's path and create a thread to open it
        self.enable_buttons()

    def errormsg(self):
        q = QMessageBox(self)
        q.information(self, 'information', '단어의 개수에 비해서 퍼즐의 크기가 너무 작습니다.', QMessageBox.Ok)
        self.enable_buttons()

# thread to download pictures while not stopping the Gui
class PuzzleWorker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(PuzzleWorker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signal = Communication()

    @pyqtSlot()
    def run(self):
        try:
            self.fn(*self.args, **self.kwargs).make_puzzle()
            self.signal.puzzle_complete.emit()
        except RecursionError:
            self.signal.recursionerrormsg.emit()

class MainWindow(MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

    def init_UI(self):
        super(MainWindow, self).init_UI()
        self.setWindowTitle('Word Puzzle generator')
        self.setWindowIcon(QIcon('wordsearch.ico'))
        c = Communication()
        self.vbox.addWidget(Settings(c))
        self.vbox.addWidget(EnterWords(c))
        self.vbox.addWidget(DownloadImage(c))
        self.vbox.setStretch(0, 1)
        self.vbox.setStretch(1, 1)
        self.vbox.setStretch(2, 7)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    sys.exit(app.exec_())