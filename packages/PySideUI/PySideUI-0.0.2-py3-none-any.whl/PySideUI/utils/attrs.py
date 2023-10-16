

import typing as tp


class WidgetStyle:
    def __init__(self, style: tp.Dict):
        self._style = style

    def copy(self):
        return WidgetStyle(self._style.copy())

    def getStyleString(self):
        return  ';'.join([str(a) + ':' + str(b) for a, b in self._style.items()])
    
    def __setitem__(self, key: str, value: str):
        self._style[key] = value

    def __getitem__(self, key: str) -> str:
        return self._style[key]

    def __str__(self) -> str:
        return self.getStyleString()

    def __contains__(self, key: str):
        return key in self._style



if __name__ == '__main__':
    c = {'s':2, 'font-family':5}
    s = WidgetStyle(c)
    print(s.getStyleString())
    s['123'] =12
    print(s)
    print('123' in s)

    