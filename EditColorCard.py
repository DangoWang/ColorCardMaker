# -*- coding: UTF-8 -*-
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from photoshop import Session
import photoshop.api as photoshop
import core

new_win = []

cwd = ''
if hasattr(sys, "_MEIPASS"):
    cwd = sys._MEIPASS
else:
    cwd = os.path.dirname(os.path.abspath(__file__))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(571, 112)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setMaximum(999)
        self.spinBox.setProperty("value", 50)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setMaximum(999)
        self.spinBox_2.setProperty("value", 50)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout.addWidget(self.spinBox_2)
        self.horizontalLayout.addWidget(QtWidgets.QLabel(u' 边框宽度：'))
        self.spinBox_3 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_3.setMaximum(999)
        self.spinBox_3.setProperty("value", 5)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout.addWidget(self.spinBox_3)

        self.horizontalLayout.addWidget(QtWidgets.QLabel(u' 字体颜色:'))
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItems([u'嘿', u'㿟'])
        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalLayout.addWidget(QtWidgets.QLabel(u' 字体大小:'))
        self.font_size = QtWidgets.QSpinBox(Dialog)
        self.font_size.setProperty("value", 23)
        self.horizontalLayout.addWidget(self.font_size)

        self.horizontalLayout.addWidget(QtWidgets.QLabel(u' 字和色卡间距:'))
        self.font_distance = QtWidgets.QDoubleSpinBox(Dialog)
        self.font_distance.setSingleStep(0.01)
        self.font_distance.setProperty("value", 0.3)
        self.horizontalLayout.addWidget(self.font_distance)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", u"Settings"))
        self.label.setText(_translate("Dialog", u"色卡单元尺寸："))
        self.label_2.setText(_translate("Dialog", u"×"))
        self.label_3.setText(_translate("Dialog", u"文件存储路径："))
        self.pushButton.setText(_translate("Dialog", u"OK"))


class SettingUI(Ui_Dialog, QtWidgets.QDialog):
    def __init__(self, parent):
        super(SettingUI, self).__init__(parent)
        self.setupUi(self)
        self.q_settings = QtCore.QSettings(u'ColorCardTool', 'win_cfg')
        self.pushButton.clicked.connect(self.close)
        self.readSettings()

    def readSettings(self):
        font_index = {'嘿': 0, '㿟': 1}
        cw = self.q_settings.value("cw") or 50
        ch = self.q_settings.value("ch") or 50
        lw = self.q_settings.value("lw") or 5
        path = self.q_settings.value("path")
        font_color = self.q_settings.value("font_color")
        font_size = self.q_settings.value('font_size') or 23
        font_distance = float(self.q_settings.value('font_distance') or 0.3)
        # print(path)
        if not path or not font_color:
            return
        self.spinBox.setValue(cw)
        self.spinBox_2.setValue(ch)
        self.spinBox_3.setValue(lw)
        self.lineEdit.setText(path)
        self.comboBox.setCurrentIndex(font_index[font_color])
        self.font_size.setValue(font_size)
        self.font_distance.setValue(font_distance)

    def writeSettings(self):
        self.q_settings.setValue("cw", self.spinBox.value())
        self.q_settings.setValue("ch", self.spinBox_2.value())
        self.q_settings.setValue("lw", self.spinBox_3.value())
        self.q_settings.setValue("path", self.lineEdit.text())
        self.q_settings.setValue(u'font_color', self.comboBox.currentText())
        self.q_settings.setValue("font_size", self.font_size.value())
        self.q_settings.setValue(u'font_distance', float(self.font_distance.value()))

    def closeEvent(self, QCloseEvent):
        if not self.lineEdit.text() or not os.path.isdir(self.lineEdit.text()):
            QtWidgets.QMessageBox.critical(self, u"警告", u"必须填入有效路径！", QtWidgets.QMessageBox.Yes)
            QCloseEvent.ignore()
        else:
            self.writeSettings()
            print(u'成功写入设置')
            QCloseEvent.accept()


class SingleColorCard(QtWidgets.QWidget):
    def __init__(self, parent):
        super(SingleColorCard, self).__init__(parent)
        self.check_box = QtWidgets.QToolButton()
        self.check_box.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.check_box.setAutoExclusive(False)
        self.check_box.setAutoRaise(True)
        self.check_box.setIcon(QtGui.QIcon(cwd + u'/icons/brush.svg'))
        self.tool_button = QtWidgets.QToolButton()
        self.tool_button.setIcon(QtGui.QIcon(cwd + u'/icons/cross.svg'))
        self.tool_button.setFixedSize(40, 40)
        self.main_layout = QtWidgets.QHBoxLayout()
        # self.main_layout.addItem(QtWidgets.QSpacerItem(0, 0,
        #                                               QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.main_layout.addWidget(self.check_box)
        self.main_layout.addWidget(self.tool_button)
        self.setLayout(self.main_layout)

        # signal click
        self.check_box.clicked.connect(self.clear_color)
        self.tool_button.clicked.connect(self.on_label_color_pushButton_clicked)

        # public param
        self.is_valid = False
        self.card_color = ''

    def small(self):
        self.tool_button.setFixedSize(20, 20)
        return self

    def large(self):
        self.tool_button.setFixedSize(40, 40)
        return self

    def clear_color(self):
        self.tool_button.setStyleSheet(u'')
        self.tool_button.setAutoExclusive(True)
        self.tool_button.setAutoRaise(False)
        self.tool_button.setIcon(QtGui.QIcon(cwd + u'/icons/cross.svg'))
        self.is_valid = False

    @staticmethod
    def RGB_to_Hex(rgb):
        tmp = '#'
        for c in rgb:
            # 将R、G、B分别转化为16进制拼接转换并大写
            tmp += str(hex(c))[-2:].replace('x', '0')
        return tmp

    def on_label_color_pushButton_clicked(self):
        try:
            app = photoshop.Application()
            colors = []
            with Session() as ps:
                color_window = app.showColorPicker()
                if color_window:
                    red = ps.app.foregroundColor.rgb.red
                    green = ps.app.foregroundColor.rgb.green
                    blue = ps.app.foregroundColor.rgb.blue
                    colors = [red, green, blue]
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, u"警告", u"无法连接photoshop！！", QtWidgets.QMessageBox.Yes)
            raise RuntimeError(e)
        # add color panel for users to select color
        # label_color = QtWidgets.QColorDialog.getColor()
        # if label_color.isValid():
        #     self.card_color = label_color.name()
        #     style_sheet = 'background-color: rgb({}, {}, {});'.format(label_color.getRgb()[0],
        #                                                              label_color.getRgb()[1], label_color.getRgb()[2])
        if colors:
            style_sheet = 'background-color: rgb({}, {}, {});'.format(*colors)
            self.card_color = self.RGB_to_Hex(colors)
            print(style_sheet)
            self.tool_button.setStyleSheet(style_sheet)
            self.tool_button.setAutoExclusive(False)
            self.tool_button.setAutoRaise(True)
            self.tool_button.setIcon(QtGui.QIcon(u''))
            self.is_valid = True
            return True
        self.tool_button.setAutoExclusive(True)
        self.tool_button.setAutoRaise(False)
        return False


class ColorCard(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(ColorCard, self).__init__(parent)
        self.color_card_size_info = [50, 50, 5]
        self.color_card_path_info = ''
        self.font_color_info = ''
        self.font_size_info = ''
        self.font_distance_info = ''
        self.common_card_widgets = []
        self.card_color_info = None
        self._init_ui()
        self._init_cfg()

    def _init_ui(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        main_widget = QtWidgets.QWidget()
        self.setCentralWidget(main_widget)
        self.setWindowTitle(u'色卡')
        self.setFixedWidth(150)

        self.main_layout = QtWidgets.QVBoxLayout()
        main_widget.setLayout(self.main_layout)

        toolbar_layout = QtWidgets.QHBoxLayout()
        self.setting_btn = QtWidgets.QToolButton()
        self.setting_btn.setAutoRaise(True)
        self.setting_btn.setIcon(QtGui.QIcon(cwd + u'/icons/setting.svg'))
        self.setting_btn.clicked.connect(self.set_setting_ui)
        toolbar_layout.addWidget(self.setting_btn)
        self.setting_ui = SettingUI(self)
        self.setting_ui.pushButton.clicked.connect(self.set_settings)

        self.new_btn = QtWidgets.QToolButton()
        self.new_btn.setAutoRaise(True)
        self.new_btn.setIcon(QtGui.QIcon(cwd + u'/icons/new.svg'))
        self.new_btn.clicked.connect(self.new_one)
        toolbar_layout.addWidget(self.new_btn)

        toolbar_layout.addItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.toolButton_close = QtWidgets.QToolButton()
        self.toolButton_close.setIcon(QtGui.QIcon(cwd + u'/icons/close.svg'))
        self.toolButton_close.setAutoExclusive(False)
        self.toolButton_close.setAutoRaise(True)
        toolbar_layout.addWidget(self.toolButton_close)
        self.toolButton_close.clicked.connect(self.close)
        self.main_layout.addLayout(toolbar_layout)

        self.line_edit = QtWidgets.QLineEdit()
        # self.line_edit.setText(u'1')
        self.line_edit.setPlaceholderText(u'输入名称...')
        self.main_layout.addWidget(self.line_edit)

        self.main_group_box = QtWidgets.QGroupBox()
        self.main_group_box_layout = QtWidgets.QVBoxLayout()
        self.main_group_box.setLayout(self.main_group_box_layout)
        self.main_layout.addWidget(self.main_group_box)

        Hbox_layout = QtWidgets.QHBoxLayout()
        self.upper_card = SingleColorCard(self).small()
        Hbox_layout.addItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        Hbox_layout.addWidget(self.upper_card)
        self.main_group_box_layout.addLayout(Hbox_layout)

        for _ in range(7):
            ly = QtWidgets.QHBoxLayout()
            card = SingleColorCard(self).large()
            ly.addWidget(card)
            self.common_card_widgets.append(card)
            ly.addItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
            self.main_group_box_layout.addLayout(ly)

        Hbox_layout1 = QtWidgets.QHBoxLayout()
        self.down_card = SingleColorCard(self).small()
        Hbox_layout1.addItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        Hbox_layout1.addWidget(self.down_card)
        self.main_group_box_layout.addLayout(Hbox_layout1)

        #  outline check
        self.outline_cb = QtWidgets.QCheckBox(u'OutLine')
        # self.outline_cb.setStyleSheet('* {background: green; border: 0px;}')
        self.outline_cb.setChecked(True)
        outline_layout = QtWidgets.QHBoxLayout()
        outline_layout.addItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        outline_layout.addWidget(self.outline_cb)
        outline_layout.addItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.main_layout.addLayout(outline_layout)

        # save
        self.save_pb = QtWidgets.QToolButton()
        self.save_pb.setText(u'Save')
        self.save_pb.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        save_pb_layout = QtWidgets.QHBoxLayout()
        save_pb_layout.addItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.save_pb.setAutoExclusive(False)
        self.save_pb.setAutoRaise(True)
        self.save_pb.setFixedSize(50, 30)
        # self.main_layout.addWidget(self.save_pb)
        self.save_pb.setIcon(QtGui.QIcon(cwd + u'/icons/save.svg'))
        save_pb_layout.addWidget(self.save_pb)
        save_pb_layout.addItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.main_layout.addLayout(save_pb_layout)

        # signal
        self.save_pb.clicked.connect(self.save)
        pass

    def dragPosition(self):
        pass

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            try:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()
            except:
                pass

    def set_setting_ui(self):
        # self.setting_ui.lineEdit.setText(self.color_card_path_info)
        # self.setting_ui.spinBox.setValue(self.color_card_size_info[0])
        # self.setting_ui.spinBox_2.setValue(self.color_card_size_info[1])
        # self.setting_ui.spinBox_3.setValue(self.color_card_size_info[2])
        self.setting_ui.show()

    def set_settings(self):
        line_edit_text = self.setting_ui.lineEdit.text()
        if line_edit_text:
            self.color_card_path_info = line_edit_text
        self.color_card_size_info = (self.setting_ui.spinBox.value(),
                                     self.setting_ui.spinBox_2.value(), self.setting_ui.spinBox_3.value())
        self.font_color_info = self.setting_ui.comboBox.currentText()
        self.font_size_info = self.setting_ui.font_size.value()
        self.font_distance_info = self.setting_ui.font_distance.value()

    def new_one(self):
        global new_win
        nw = ColorCard(None)
        # nw.line_edit.setText(str(len(new_win)+2))
        nw.color_card_path_info = self.color_card_path_info
        nw.color_card_size_info = self.color_card_size_info
        new_win.append(nw)
        num = len(new_win) if len(new_win) < 3 else 3
        new_win[-1].move(self.pos().x()+self.size().width() + num*10, self.pos().y()+ num*10)
        new_win[-1].show()

    def _init_cfg(self):
        self.card_color_info = {'upper': '', 'common': [], 'down': '', 'size': None, 'path': None, 'outline': True}

    def load_cfg(self):
        self._init_cfg()
        if self.upper_card.is_valid:
            self.card_color_info['upper'] = self.upper_card.card_color
        if self.down_card.is_valid:
            self.card_color_info['down'] = self.down_card.card_color
        for card in self.common_card_widgets:
            if card.is_valid:
                self.card_color_info['common'].append(card.card_color)
        self.card_color_info['size'] = self.color_card_size_info
        self.card_color_info['path'] = self.color_card_path_info
        self.card_color_info['font_color'] = self.font_color_info
        self.card_color_info['font_size'] = self.font_size_info
        self.card_color_info['font_distance'] = self.font_distance_info
        if not self.outline_cb.isChecked():
            self.card_color_info['outline'] = False
        return self.card_color_info

    def save(self):
        if not self.line_edit.text():
            QtWidgets.QMessageBox.critical(self, u"警告", u"请填入图片名称！", QtWidgets.QMessageBox.Yes)
            return
        cfg = self.load_cfg()
        pic_path = os.path.join(cfg.get(u'path') + '/', self.line_edit.text()) + '.png'
        if cfg:
            img = core.combine_color_card(cfg)
            # w, h = img.size
            # img = img.resize((int(w), int(h)))
            img.save(pic_path)
            print(u'success!')
            QtWidgets.QMessageBox.information(self, u"提示", u"输出成功！", QtWidgets.QMessageBox.Yes)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = ColorCard(None)
    win.show()
    win.set_setting_ui()
    app.exec_()
