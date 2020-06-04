# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_source_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditSource(object):
    def setupUi(self, EditSource):
        EditSource.setObjectName("EditSource")
        EditSource.resize(567, 320)
        self.centralwidget = QtWidgets.QWidget(EditSource)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_rebuild = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_rebuild.setFont(font)
        self.btn_rebuild.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/rebuild"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_rebuild.setIcon(icon)
        self.btn_rebuild.setIconSize(QtCore.QSize(20, 20))
        self.btn_rebuild.setObjectName("btn_rebuild")
        self.horizontalLayout.addWidget(self.btn_rebuild)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/save"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon1)
        self.btn_save.setIconSize(QtCore.QSize(20, 20))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_reload = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/refresh"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reload.setIcon(icon2)
        self.btn_reload.setIconSize(QtCore.QSize(20, 20))
        self.btn_reload.setObjectName("btn_reload")
        self.horizontalLayout.addWidget(self.btn_reload)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.src_editor = MetalSourceEditor(self.centralwidget)
        self.src_editor.setObjectName("src_editor")
        self.verticalLayout.addWidget(self.src_editor)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.undo = QtWidgets.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/delete"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undo.setIcon(icon3)
        self.undo.setObjectName("undo")
        self.horizontalLayout_3.addWidget(self.undo)
        self.zoomin = QtWidgets.QPushButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/plot/zoom"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoomin.setIcon(icon4)
        self.zoomin.setObjectName("zoomin")
        self.horizontalLayout_3.addWidget(self.zoomin)
        self.zoomout = QtWidgets.QPushButton(self.centralwidget)
        self.zoomout.setIcon(icon4)
        self.zoomout.setObjectName("zoomout")
        self.horizontalLayout_3.addWidget(self.zoomout)
        self.center = QtWidgets.QPushButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/options"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.center.setIcon(icon5)
        self.center.setObjectName("center")
        self.horizontalLayout_3.addWidget(self.center)
        self.full_screen = QtWidgets.QPushButton(self.centralwidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/plot/autozoom"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.full_screen.setIcon(icon6)
        self.full_screen.setObjectName("full_screen")
        self.horizontalLayout_3.addWidget(self.full_screen)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.lineSrcPath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSrcPath.setReadOnly(True)
        self.lineSrcPath.setObjectName("lineSrcPath")
        self.verticalLayout.addWidget(self.lineSrcPath)
        EditSource.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EditSource)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 22))
        self.menubar.setObjectName("menubar")
        EditSource.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(EditSource)
        self.statusBar.setObjectName("statusBar")
        EditSource.setStatusBar(self.statusBar)

        self.retranslateUi(EditSource)
        self.btn_save.clicked.connect(self.src_editor.save_file)
        self.btn_reload.clicked.connect(self.src_editor.reload_file)
        self.undo.clicked.connect(self.src_editor.undo)
        self.zoomin.clicked.connect(self.src_editor.zoomIn)
        self.zoomout.clicked.connect(self.src_editor.zoomOut)
        self.center.clicked.connect(self.src_editor.centerCursor)
        self.full_screen.clicked.connect(EditSource.showFullScreen)
        QtCore.QMetaObject.connectSlotsByName(EditSource)

    def retranslateUi(self, EditSource):
        _translate = QtCore.QCoreApplication.translate
        EditSource.setWindowTitle(_translate("EditSource", "Edit source code"))
        self.btn_rebuild.setText(_translate("EditSource", "Rebuild Component"))
        self.btn_rebuild.setShortcut(_translate("EditSource", "Ctrl+R, Meta+R"))
        self.btn_save.setText(_translate("EditSource", "Save File"))
        self.btn_save.setShortcut(_translate("EditSource", "Ctrl+S, Meta+S"))
        self.btn_reload.setText(_translate("EditSource", "Reload File"))
        self.src_editor.setPlainText(_translate("EditSource", "Source comes here"))
        self.undo.setText(_translate("EditSource", "Undo"))
        self.zoomin.setText(_translate("EditSource", "Zoom in"))
        self.zoomout.setText(_translate("EditSource", "Zoom out"))
        self.center.setText(_translate("EditSource", "Center"))
        self.full_screen.setText(_translate("EditSource", "Full screen"))
        self.lineSrcPath.setText(_translate("EditSource", "Source code file path here"))
from .widgets.edit_component.source_editor import MetalSourceEditor
from . import main_window_rc_rc
