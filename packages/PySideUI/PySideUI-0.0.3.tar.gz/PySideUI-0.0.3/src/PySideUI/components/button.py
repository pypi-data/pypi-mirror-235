# !/usr/bin/python
# -*- coding: utf-8 -*-

import typing as tp
import re

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QPushButton, QGraphicsDropShadowEffect, QWidget
from PySide2.QtGui import QColor, QIcon

from ..utils.attrs import WidgetStyle


class Button(QPushButton):

    def __init__(self, text: str, style: WidgetStyle, parent: tp.Optional[QWidget]=None):
        super().__init__(text, parent=parent)
        self._style = style
        self.setCursor(Qt.PointingHandCursor)
        self.dealStyle()
        self.setStyleSheet(self._style.getStyleString())

    def dealStyle(self):
        '''对 style 预处理， 对缺失属性做默认处理'''
        raise NotImplementedError


class PrimaryBtn(Button):
    def __init__(self, 
                 text: str, 
                 style: tp.Optional[tp.Dict]=None, 
                 icon: str='',
                 clicked: tp.Optional[tp.Callable]=None,
                 parent: tp.Optional[QWidget]=None, 
                 ):
        style = style or {}
        self._style = WidgetStyle(style)
        self.clickedFunc = clicked

        super().__init__(text, self._style, parent)

        if icon:
            self.setIcon(QIcon(icon))

        self.setShadowEffect()

    def dealStyle(self):

        if 'color' not in self._style:
            self._style['color'] = 'white'
        if 'background-color' not in self._style:
            self._style['background-color'] = '#14aaf5'
        if 'border-radius' not in self._style:
            self._style['border-radius'] = '2px'
        if 'font-size' not in self._style:
            self._style['font-size'] = '12px'
        if 'font-family' not in self._style:
            self._style['font-family'] = '微软雅黑'

        if 'padding' not in self._style:
            fontSize = int(re.findall('\d+', self._style['font-size'])[0])
            self._style['padding'] = f'{fontSize // 3}px {fontSize * 2 // 3}px'

    def setShadowEffect(self):
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(5)
        self.shadow.setOffset(0, 0)
        self.shadow.setColor(QColor(self._style['background-color']).lighter())
        self.setGraphicsEffect(self.shadow)

    def mousePressEvent(self, e) -> None:
        style = self._style.copy()
        style['background-color'] = f"rgba{str(QColor(style['background-color'] ).darker(105).toTuple())}"
        self.setStyleSheet(style.getStyleString())
        return super().mousePressEvent(e)

    def mouseReleaseEvent(self, e) -> None:
        self.setStyleSheet(self._style.getStyleString())
        if self.clickedFunc:
            self.clickedFunc()
        return super().mouseReleaseEvent(e)
    
    def enterEvent(self, event) -> None:
        style = self._style.copy()
        style['background-color'] = f"rgba{str(QColor(style['background-color'] ).lighter(105).toTuple())}"
        self.setStyleSheet(style.getStyleString())
        return super().enterEvent(event)

    def leaveEvent(self, event) -> None:
        self.setStyleSheet(self._style.getStyleString())
        return super().leaveEvent(event)


class SecondaryBtn(Button):
    defaultStyle = WidgetStyle({
        'border': '1px solid #d4d4d4',
        'border-radius': '2px',
        'background-color': 'transparent',
        'color': 'black',
        'font-size': '12px',
        'font-family': '微软雅黑'
        })

    def __init__(self, 
                 text: str, 
                 style: tp.Optional[tp.Dict]=None, 
                 icon: str='',
                 clicked: tp.Optional[tp.Callable]=None,
                 parent: tp.Optional[QWidget]=None, 
                 ):
        self._style2 = WidgetStyle(style or {})
        self.clickedFunc = clicked

        super().__init__(text, self.defaultStyle, parent)
        if icon:
            self.setIcon(QIcon(icon))

    def dealStyle(self):

        if 'color' not in self._style2:
            self._style2['color'] = '#14aaf5'
        if 'background-color' not in self._style2:
            self._style2['background-color'] = 'white'
        if 'border-radius' not in self._style2:
            self._style2['border-radius'] = '2px'
        else:
            self.defaultStyle['border-radius'] = self._style2['border-radius']

        if 'border' not in self._style2:
            # border 样式设置 border-width, border-style, border-color
            self._style2['border'] = f"1px solid {self._style2['color']}"
        else:
            # 删除border属性中连续多个空格
            self._style2['border'] = ' '.join([att for att in self._style2['border'].split(' ') if att])
            self.defaultStyle['border'] = ' '.join(self._style2['border'].split(' ')[:2] + ['#d4d4d4'])
    
        if 'font-size' not in self._style2:
            self._style2['font-size'] = '12px'
        else:
            self.defaultStyle['font-size'] = self._style2['font-size']
        if 'font-family' not in self._style2:
            self._style2['font-family'] = '微软雅黑'
        else:
            self.defaultStyle['font-family'] = self._style2['font-family']

        if 'padding' not in self._style2:
            fontSize = int(re.findall('\d+', self._style2['font-size'])[0])
            self._style2['padding'] = f'{fontSize // 3}px {fontSize * 2 // 3}px'
        
        self.defaultStyle['padding'] = self._style2['padding']

    def mousePressEvent(self, e) -> None:
        style = self._style2.copy()
        style['color'] = f"rgba{str(QColor(style['color']).darker(110).toTuple())}"
        self.setStyleSheet(style.getStyleString())
        return super().mousePressEvent(e)

    def mouseReleaseEvent(self, e) -> None:
        style = self._style2.copy()
        style['color'] = f"rgba{str(QColor(style['color']).lighter(110).toTuple())}"
        self.setStyleSheet(style.getStyleString())
        if self.clickedFunc:
            self.clickedFunc()
        return super().mouseReleaseEvent(e)
    
    def enterEvent(self, event) -> None:
        style = self._style2.copy()
        style['color'] = f"rgba{str(QColor(style['color']).lighter(110).toTuple())}"
        self.setStyleSheet(style.getStyleString())
        return super().enterEvent(event)

    def leaveEvent(self, event) -> None:
        self.setStyleSheet(self._style.getStyleString())
        return super().leaveEvent(event)


class PrimaryIconBtn(Button):
    defaultStyle = WidgetStyle({
        'border': '1px solid #d4d4d4',
        'border-radius': '2px',
        'background-color': 'transparent',
        'color': 'black',
        'font-size': '12px',
        'font-family': '微软雅黑'
        })

    def __init__(self, 
                 text: str, 
                 style: tp.Optional[tp.Dict]=None, 
                 clicked: tp.Optional[tp.Callable]=None,
                 parent: tp.Optional[QWidget]=None, 
                 ):
        self._style2 = WidgetStyle(style or {})
        self.clickedFunc = clicked

        super().__init__(text, self.defaultStyle, parent)


    def dealStyle(self):

        if 'color' not in self._style2:
            self._style2['color'] = '#14aaf5'
        if 'background-color' not in self._style2:
            self._style2['background-color'] = 'white'
        if 'border-radius' not in self._style2:
            self._style2['border-radius'] = '2px'
        else:
            self.defaultStyle['border-radius'] = self._style2['border-radius']

        if 'border' not in self._style2:
            # border 样式设置 border-width, border-style, border-color
            self._style2['border'] = f"1px solid {self._style2['color']}"
        else:
            # 删除border属性中连续多个空格
            self._style2['border'] = ' '.join([att for att in self._style2['border'].split(' ') if att])
            self.defaultStyle['border'] = ' '.join(self._style2['border'].split(' ')[:2] + ['#d4d4d4'])
    
        if 'font-size' not in self._style2:
            self._style2['font-size'] = '12px'
        else:
            self.defaultStyle['font-size'] = self._style2['font-size']
        if 'font-family' not in self._style2:
            self._style2['font-family'] = '微软雅黑'
        else:
            self.defaultStyle['font-family'] = self._style2['font-family']

        if 'padding' not in self._style2:
            fontSize = int(re.findall('\d+', self._style2['font-size'])[0])
            self._style2['padding'] = f'{fontSize // 3}px {fontSize * 2 // 3}px'
        
        self.defaultStyle['padding'] = self._style2['padding']

    def mousePressEvent(self, e) -> None:
        style = self._style2.copy()
        style['color'] = f"rgba{str(QColor(style['color']).darker(110).toTuple())}"
        self.setStyleSheet(style.getStyleString())
        return super().mousePressEvent(e)

    def mouseReleaseEvent(self, e) -> None:
        style = self._style2.copy()
        style['color'] = f"rgba{str(QColor(style['color']).lighter(110).toTuple())}"
        self.setStyleSheet(style.getStyleString())
        if self.clickedFunc:
            self.clickedFunc()
        return super().mouseReleaseEvent(e)
    
    def enterEvent(self, event) -> None:
        style = self._style2.copy()
        style['color'] = f"rgba{str(QColor(style['color']).lighter(110).toTuple())}"
        self.setStyleSheet(style.getStyleString())
        return super().enterEvent(event)

    def leaveEvent(self, event) -> None:
        self.setStyleSheet(self._style.getStyleString())
        return super().leaveEvent(event)
