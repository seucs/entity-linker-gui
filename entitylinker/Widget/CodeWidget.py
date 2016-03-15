#coding=utf8
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.Qsci import *
from PyQt4.QtWebKit import *
from Item.MainList import MainList

class SimplePythonEditor(QsciScintilla):
    ARROW_MARKER_NUM = 8

    def __init__(self, parent=None):
        super(SimplePythonEditor, self).__init__(parent)

        # Set the default font
        font = QFont(u'Consolas')
        #font.setFixedPitch(True)
        font.setPointSize(10)
        self.setFont(font)
        self.setMarginsFont(font)
        self.setUtf8(True)

        
        fontmetrics = QFontMetrics(font)

        # Margin 0 is used for line numbers, 1 is used for marker
        self.setMarginWidth(0, fontmetrics.width("000"))
        self.setMarginWidth(1,0)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("#cccccc"))

        # Clickable margin 1 for showing markers
        #self.setMarginSensitivity(1, True)

        #self.connect(self, SIGNAL('marginClicked(int, int, Qt::KeyboardModifiers)'), self.on_margin_clicked)
        #self.markerDefine(QsciScintilla.RightArrow,
        #    self.ARROW_MARKER_NUM)
        #self.setMarkerBackgroundColor(QColor("#ee1111"),
        #    self.ARROW_MARKER_NUM)

        # Brace matching: enable for a brace immediately before or after
        # the current position
        #
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # Current line visible with special background color
        self.setCaretLineVisible(True)
        #self.setCaretLineBackgroundColor(QColor("#ffffff"))
        

        # Set Python lexer
        # Set style for Python comments (style number 1) to a fixed-width
        lexer = QsciLexerPython()
        lexer.setDefaultFont(font)
        #lexer.setColor(QColor("#ffffff"))  
        lexer.setPaper(QColor(39,39,39))  
        lexer.setColor(QColor("#a6e22e"),QsciLexerPython.ClassName)  
        lexer.setColor(QColor("#66d9ef"),QsciLexerPython.Keyword)  
        lexer.setColor(QColor("#75715e"),QsciLexerPython.Comment)  
        lexer.setColor(QColor("#ae81ff"),QsciLexerPython.Number)  
        lexer.setColor(QColor("#e6db74"),QsciLexerPython.DoubleQuotedString)  
        lexer.setColor(QColor("#e6db74"),QsciLexerPython.TripleSingleQuotedString)  
        lexer.setColor(QColor("#e6db74"),QsciLexerPython.TripleDoubleQuotedString)  
        lexer.setColor(QColor("#a6e22e"),QsciLexerPython.FunctionMethodName)  
        lexer.setColor(QColor("#f92672"),QsciLexerPython.Operator)  
        lexer.setColor(QColor("#FFFFFF"),QsciLexerPython.Identifier)  
        lexer.setColor(QColor("#75715e"),QsciLexerPython.CommentBlock)  
        lexer.setColor(QColor("#ae81ff"),QsciLexerPython.UnclosedString)  
        lexer.setColor(QColor("#F1E607"),QsciLexerPython.HighlightedIdentifier)  
        lexer.setColor(QColor("#a6e22e"),QsciLexerPython.Decorator)  

        self.setLexer(lexer)
        #self.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, 'Courier')

        # Don't want to see the horizontal scrollbar at all
        # Use raw message to Scintilla here (all messages are documented
        # here: http://www.scintilla.org/ScintillaDoc.html)
        #self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)

        # not too small

    def on_margin_clicked(self, nmargin, nline, modifiers):
        # Toggle marker for the line the margin was clicked on
        if self.markersAtLine(nline) != 0:
            self.markerDelete(nline, self.ARROW_MARKER_NUM)
        else:
            self.markerAdd(nline, self.ARROW_MARKER_NUM)


class SimplePythonViewer(QWebView):
    def __init__(self, *args):
        QWebView.__init__(self)
        #self.show()
        #self.verticalScrollBar().setStyleSheet(open('../qss/ScrollBarStyle.qss','r').read())
       
        #self.setStyleSheet(open('../qss/ScrollBarStyle.qss','r').read())
        
        self.page().mainFrame()
        self.setHtml(open('test.html','r').read().decode('utf8'))


class CodeWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QHBoxLayout()
        self.list = MainList()
        self.codeView = SimplePythonViewer()
        
        #self.textEdit = SimplePythonEditor()
        #x = open('test.py','r').read().decode('utf8')

        #self.textEdit.setText(x)

        layout.addWidget(self.list)
        layout.addWidget(self.codeView)

        self.setLayout(layout)
        self.setMinimumWidth(840)



