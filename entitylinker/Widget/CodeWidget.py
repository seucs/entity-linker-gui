#coding=utf8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from Item.MainList import MainList
from Function.LexerManager import LexerManager

class CodeList(MainList):
    def __init__(self):
        MainList.__init__(self)
        self.clicked.connect(self.changeViewer)

    def connectViewer(self, viewer):
        self.viewer = viewer

    def changeViewer(self, item):
        filename = str(item.data().toString())
        self.viewer.setCode(filename)

    def feedTitle(self, title):
        item = QListWidgetItem(QIcon('../icon/list.png'),title)
        item.setSizeHint(QSize(140,40))
        self.addItem(item)

class CodeViewer(QWebView):
    def __init__(self, *args):
        QWebView.__init__(self)
        self.pythonLex = LexerManager('python',True)
        #self.CppLex = LexerManager('c++',True)
        #JavaLex = LexerManager('java',True)

    def getCodelist(self):
        return self.pythonLex.codeDict.keys()
    
    def setCode(self, filename):
        self.setHtml(self.pythonLex.getCode(filename))

class CodeWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QHBoxLayout()
        self.list = CodeList()
        self.codeView = CodeViewer()
        self.list.connectViewer(self.codeView)

        for filename in self.codeView.getCodelist():
            self.list.feedTitle(filename)
        
        layout.addWidget(self.list)
        layout.addWidget(self.codeView)

        self.setLayout(layout)
        self.setMinimumWidth(840)



