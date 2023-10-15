# !/usr/bin/python
# -*- coding: utf-8 -*-


from PySide2.QtCore import Qt
from PySide2.QtWidgets import QPushButton, QGraphicsDropShadowEffect
from PySide2.QtGui import QColor, QFontMetrics, QFont


class CommonBtn(QPushButton):
    def __init__(self, text:str, color: str='white', bkColor: str='#14aaf5', fontSize: int=8, borderRadius: int=2,
                 fontFamily: str="微软雅黑", fitText: bool=False):
        super().__init__(text)
        self._color = color
        self._bkColor = bkColor
        self._borderRadius = borderRadius

        self.setCursor(Qt.PointingHandCursor)
        _style = '''
                QPushButton{{
                    border-radius:{2}px;
                    background-color:{1};
                    color:{0};
                    }}  
            '''.format(self._color, self._bkColor, self._borderRadius)
        self.setStyleSheet(_style)

        font = QFont(fontFamily, fontSize)
        self.setFont(font)
        if fitText:
            rect = QFontMetrics(font).boundingRect(text)
            self.setFixedSize(rect.width() + 2*fontSize, rect.height()+ fontSize)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(5)
        self.shadow.setOffset(0, 0)
        self.shadow.setColor(QColor(bkColor).lighter())
        self.setGraphicsEffect(self.shadow)
    
    def mousePressEvent(self, e) -> None:
        bkcolor = f'rgba{str(QColor(self._bkColor).darker(110).toTuple())}'
        _style = '''
                QPushButton{{
                    border-radius:{2}px;
                    background-color:{1};
                    color:{0};
                    }}  
            '''.format(self._color, bkcolor, self._borderRadius)
        self.setStyleSheet(_style)
        return super().mousePressEvent(e)

    def mouseReleaseEvent(self, e) -> None:
        _style = '''
                QPushButton{{
                    border-radius:{2}px;
                    background-color:{1};
                    color:{0};
                    }}  
            '''.format(self._color, self._bkColor, self._borderRadius)
        self.setStyleSheet(_style)
        return super().mouseReleaseEvent(e)
    
    def enterEvent(self, event) -> None:
        bkcolor = f'rgba{str(QColor(self._bkColor).lighter(110).toTuple())}'
        _style = '''
                QPushButton{{
                    border-radius:{2}px;
                    background-color:{1};
                    color:{0};
                    }}  
            '''.format(self._color, bkcolor, self._borderRadius)
        self.setStyleSheet(_style)
        return super().enterEvent(event)

    def leaveEvent(self, event) -> None:
        _style = '''
                QPushButton{{
                    border-radius:{2}px;
                    background-color:{1};
                    color:{0};
                    }}  
            '''.format(self._color, self._bkColor, self._borderRadius)
        self.setStyleSheet(_style)
        return super().leaveEvent(event)
