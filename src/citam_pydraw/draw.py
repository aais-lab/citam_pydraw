###
# プログラミング基礎 v3
###
import tkinter
import tkinter.font as font
from math import sin, cos, radians
from colorsys import hsv_to_rgb
import datetime
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
from re import sub, compile, match
from inspect import stack
import sys
from pathlib import Path
from typing import Final, Pattern, Never
from PIL import Image as PILImage
from PIL import ImageTk
from just_playback import Playback

# stack trace
def allTraceBack():
    _Config.IS_ALL_TRACE = not _Config.IS_ALL_TRACE

def _TraceBack(level=2,limit=0):
    sys.tracebacklimit=limit
    print("\nTraceback (most recent call last):")
    print("File \"" + stack()[level].filename + "\", line " + str(stack()[level].lineno) + ", in " + str(stack()[level][3])+"\n   " + sub("(\[)|(\])|(')|(\")",'',str(stack()[level][4]))[:-2])

# animation
class _Config:
    IS_ALL_TRACE = False
    RATE = 30
    IS_DRAW_MOVED = True
    COLOR_MORD = "RGB"
    COLOR = ['black','white','snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace','linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff', 'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender', 'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray', 'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue', 'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue', 'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue', 'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise', 'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green', 'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green', 'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green', 'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow', 'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown', 'indian red', 'saddle brown', 'sandy brown', 'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange', 'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',    'pale violet red', 'maroon', 'medium violet red', 'violet red', 'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',    'thistle', 'snow2', 'snow3',    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
    COLOR_CORD: Pattern[str] = compile('^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$')
    FONTS = None

# Date Class（Singleton）
class Date:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Date, cls).__new__(cls)
        return cls._instance
    
    @property
    def date(self) -> str:
        now = datetime.datetime.now()
        return f"{now.year}-{now.month}-{now.day}"
    
    @property
    def year(self) -> int:
        return datetime.datetime.now().year

    @property
    def month(self) -> int:
        return datetime.datetime.now().month

    @property
    def day(self) -> int:
        return datetime.datetime.now().day

    @property
    def hour(self) -> int:
        return datetime.datetime.now().hour

    @property
    def minute(self) -> int:
        return datetime.datetime.now().minute

    @property
    def second(self) -> int:
        return datetime.datetime.now().second

# _keyboard（Singleton）
class KeyBoard:
    _instance = None
    
    def __new__(cls):
        # ROOTがNoneの時はinitでイベントバインドができないので生成しない
        if Window.ROOT() is not None and cls._instance is None:
            cls._instance = super(KeyBoard, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self._key = ""
        self._code = ""
        self._char = ""
        self._is_pressed = False
        self._is_pressed_before = False
        self._is_released_before = False
        
        Window._root.bind("<KeyPress>", self._keyPress)
        Window._root.bind("<KeyRelease>", self._keyRelease)
    
    def _keyPress(self, event):
        self._key, self._char = event.keysym, event.char
        try:
            self._code = ord(event.keysym)
        except :
            self._code = event.keycode
        self._is_pressed = True
        self._is_pressed_before = False
    
    def _keyRelease(self, event):
        self._is_pressed = False
        self._is_released_before = True
        
    @property
    def key(self) -> str:
        return self._key
    
    @property
    def code(self) -> str:
        return self._code
    
    @property
    def char(self) -> str:
        return self._char
    
    @property
    def isPressed(self) -> bool:
        return self._is_pressed

# Mouse
class Mouse:
    _instance = None
    
    def __new__(cls):
        if Window.ROOT() is not None and cls._instance is None:
            cls._instance = super(Mouse, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self._X = 0
        self._Y = 0
        
        self._preMouseX: deque[int] = deque([],4)
        self._preMouseY: deque[int] = deque([],4)
        self._beforeX = 0
        self._beforeY = 0
        
        self._pressX = 0
        self._pressY = 0
        self._releaseX = 0
        self._releaseY = 0
        
        self._buttons = ["left", "right", "center"]
        self._press_button = ""
        self._is_pressed = False
        self._is_pressed_before = False
        self._is_released_before = False
        
        Window._root.bind("<Motion>", self._mousePosition)
        Window._root.bind("<ButtonPress>", self._mousePress)
        Window._root.bind("<ButtonRelease>", self._mouseRelease)
    
    def _mousePosition(self, event):
        self._preMouseX.append(self._X)
        self._preMouseY.append(self._Y)
        if len(self._preMouseY) > 3:
            self._beforeX, self._beforeY = self._preMouseX.popleft(), self._preMouseY.popleft()
        self._X, self._Y = event.x, event.y
        
    def _mousePress(self, event):
        # NOTE: macのトラックパッドだと1本が1,2本が2,3は返ってこない
        self._pressX, self._pressY = event.x, event.y
        self._mouseButton = self._buttons[event.num-1]
        self._is_pressed = True
        self._is_pressed_before = False
        
    def _mouseRelease(self, event):
        self._clickX, self._clickY = event.x, event.y
        self._is_pressed = False
        self._is_released_before = True
        
    @property
    def X(self) -> int:
        return self._X
    
    @property
    def Y(self) -> int:
        return self._Y
    
    @property
    def beforeX(self) -> int:
        return self._beforeX
    
    @property
    def beforeY(self) -> int:
        return self._beforeY
    
    @property
    def pressX(self) -> int:
        return self._pressX
    
    @property
    def pressY(self) -> int:
        return self._pressY
    
    @property
    def releaseX(self) -> int:
        return self._releaseX
    
    @property
    def releaseY(self) -> int:
        return self._releaseY
    
    @property
    def pressButton(self) -> str:
        return self._press_button
    
    @property
    def isPressed(self) -> bool:
        return self._is_pressed

# thread
_executor = ThreadPoolExecutor(max_workers=6)

# Exception
class ColorError(Exception):
    pass

class FontError(Exception):
    pass

class ShapeError(Exception):
    pass

class FileTypeError(Exception):
    pass

class BackgroundException(Exception):
    pass

class NotFoundFunction(Exception):
    pass

class LoadingException(Exception):
    pass

class EnvironmentException(Exception):
    pass

class ProcessingIsLaggy(Exception):
    pass

def _checkColor(arg):
    if arg in _Config.COLOR or _Config.COLOR_CORD.fullmatch(arg):
        return
    elif arg not in _Config.COLOR:
        if not _Config.IS_ALL_TRACE : _TraceBack(3)
        raise ColorError(f"{arg} は指定可能な色名ではありません")
    elif match("^#",arg) and not _Config.COLOR_CORD.fullmatch(arg):
        if not _Config.IS_ALL_TRACE : _TraceBack(3)
        raise ColorError(f"{arg} はカラーコードとして不正です")
    
# decolater
# animation
def animation(isAnimated: bool):
    def _ani(func):
        def _reg(*args, **kwargs):
            if isAnimated:
                clear()
            process_start = perf_counter()
            func(*args, **kwargs)
            process_time = (perf_counter() - process_start)*1000
            call_time = _Config.RATE if process_time < _Config.RATE else int(process_time)
            if isAnimated and call_time > 1000 :
                if not _Config.IS_ALL_TRACE : _TraceBack(2)
                raise ProcessingIsLaggy("描画する関数の処理時間が1秒を超えています。PCに負荷がかかっているか、関数内の処理が重すぎます")
            if _Config.IS_DRAW_MOVED:
                Window.CANVAS().after(call_time, _ani(func))
        return _reg
    return _ani

# event
def mouseMoved(func):
    def _reg(*args, **kwargs):
        def tmp():
            if not _mouse.isPressed:
                if 0 < _mouse.X < Window._canvas_width and 0 < _mouse.Y < Window._canvas_height:
                    _executor.submit(lambda:func(*args, **kwargs))
        Window.CANVAS().bind("<Motion>", tmp())
    return _reg

def mousePressed(func):
    def _reg(*args, **kwargs):
        def tmp():
            if _mouse.isPressed and not _mouse._is_pressed_before:
                _mouse._is_pressed_before = True
                _executor.submit(lambda:func(*args, **kwargs))
        Window.CANVAS().bind("<ButtonPress>", tmp())
    return _reg

def mouseReleased(func):
    def _reg(*args, **kwargs):
        def tmp():
            if _mouse._is_released_before:
                _mouse._is_released_before = False
                _executor.submit(lambda:func(*args, **kwargs))
        Window.CANVAS().bind("<ButtonRelease>", tmp())
    return _reg

def mouseDragged(func):
    def _reg(*args, **kwargs):
        def tmp():
            if _mouse.isPressed:
                func(*args, **kwargs)
                _mouse._pressX, _mouse._pressY = _mouse.X, _mouse.Y
        Window.CANVAS().bind("<Motion>", tmp())
    return _reg

def keyPressed(func):
    def _reg(*args, **kwargs):
        def tmp():
            if _keyboard.isPressed and not _keyboard._is_pressed_before:
                _keyboard._is_pressed_before = True
                _executor.submit(lambda:func(*args, **kwargs))
        Window.CANVAS().bind("<KeyPressed>", tmp())
    return _reg

def keyReleased(func):
    def _reg(*args, **kwargs):
        def tmp():
            if _keyboard._is_released_before:
                _keyboard._is_released_before = False
                _executor.submit(lambda:func(*args, **kwargs))
        Window.CANVAS().bind("<KeyRelease>", tmp())
    return _reg

# callable function
def windowMaxSize(width: int, height: int) -> None:
    Window._max_width, Window._max_height  = width, height

def colorMode(colorMode: str) -> None:
    if colorMode not in ["HSV", "RGB"]:
        if not _Config.IS_ALL_TRACE :_TraceBack()
        raise ColorError(f"{colorMode} は対応しているカラーモードではありません。HSVもしくはRGBが指定できます")
    _Config.COLOR_MORD = colorMode
    
def color(v1: int, v2: int, v3: int):
    if type(v1)!=int or type(v2)!=int or type(v3)!=int:
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise ColorError(f"color({v1},{v2},{v3}) で指定されたいずれかの値が整数ではありません")
    if v1<0 or v2<0 or v3<0:
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise ColorError("色の指定に0以下は使用できません")
    if _Config.COLOR_MORD == "RGB":
        if v1>255 or v2>255 or v3>255:
            if not _Config.IS_ALL_TRACE : _TraceBack()
            raise ColorError(f"color({v1},{v2},{v3}) はRGBで指定可能な範囲を超えています")
    else:
        if v1>100 or v2>100 or v3>100:
            if not _Config.IS_ALL_TRACE : _TraceBack()
            raise ColorError(f"color({v1},{v2},{v3}) はHSVで指定可能な範囲を超えています")
        v1, v2, v3 = hsv_to_rgb(v1/100, v2/100, v3/100)
        v1, v2, v3 = int(v1*255), int(v2*255), int(v3*255)
    return "#"+format(v1,'02x')+format(v2,'02x')+format(v3,'02x')

def availableColors(colorname: str ='all'):
    if colorname != 'all':
        if colorname in _Config.COLOR:
            print(f"{colorname}は使用可能です")
        else:
            print(f"{colorname}は使用できません")
    else:
        root = tkinter.Tk()
        root.title("色名と色")
        r = 0
        c = 0
        frame = tkinter.Frame(root)
        for color in _Config.COLOR:
            label = tkinter.Label(frame, text=color, bg=color)
            label.grid(row=r, column=c, sticky="ew")
            r += 1
            if r > 36:
                r = 0
                c += 1
        frame.pack(expand=1, fill="both")
        root.mainloop()
    
def availableFonts(fontname: str ='all'):
    root = tkinter.Tk()
    fontlist = list(font.families(root))
    if fontname != 'all':
        if fontname in fontlist:
            print(f"{fontname}は使用可能です")
        else:
            print(f"{fontname}は使用できません")
    else:
        root.title("使用可能フォント")
        frame = tkinter.Frame(root)
        r = 0
        c = 0
        for fontname in fontlist:
            label = tkinter.Label(frame, text=fontname,font=(fontname, 12, "bold"))
            label.grid(row=r, column=c, sticky="ew")
            r += 1
            if r > 36:
                r = 0
                c += 1
        frame.pack(expand=1, fill="both")
        root.mainloop()
    
def clear():
    canvas = Window.CANVAS()
    if canvas is not None:
        canvas.delete(Window._tag)

def stop():
    _Config.IS_DRAW_MOVED = False

def animationSpeed(rate: int):
    if type(rate) != int:
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise ValueError(f"{rate} は整数値ではありません")
    if 1 > rate or rate > 100:
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise ValueError(f"{rate} はanimationSpeedで指定可能な範囲ではありません")
    _Config.RATE = 101 - rate
    
# internal function
def _calc_rotate(basePoint: dict, movePoint: dict, angle: int|float) -> dict:
    point = {}
    point["x"] = (movePoint["x"]-basePoint["x"]) * cos(radians(angle)) - (movePoint["y"]-basePoint["y"]) * sin(radians(angle)) +basePoint["x"]
    point["y"] = (movePoint["x"]-basePoint["x"]) * sin(radians(angle)) + (movePoint["y"]-basePoint["y"]) * cos(radians(angle)) +basePoint["y"]
    return point        

# window class
class Window:
    _max_height = 700
    _max_width = 1000
    _canvas_height = 500
    _canvas_width = 500
    _canvas = None
    _root = None
    _tag :Final = "onCanvas"
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Window, cls).__new__(cls)
        return cls._instance
     
    def __init__(self, width: int =500, height: int =500, background: str ="white") -> 'Window':
        self.title_text = None
        self.background_color = background
        
        if Window._max_width < width or Window._max_height < height:
            if not _Config.IS_ALL_TRACE : _TraceBack()
            raise ValueError(f"指定されたウィンドウサイズ(width:{width}, height:{height})は上限値を超えています。width:{Window._max_width}, height:{Window._max_height}以下で設定してください。\nウィンドウサイズをより大きくしたい場合は、windowMaxSize関数を使用して上限サイズを変更してください。") from None
        Window._canvas_height, Window._canvas_width = height, width
        _checkColor(background)
        
        Window._root = tkinter.Tk()
        _Config.FONTS = list(font.families(Window._root))
        Window._root.resizable(width=False, height=False)
        Window._root.geometry('{}x{}+0+0'.format(str(Window._canvas_width), str(Window._canvas_height)))
        canvas = tkinter.Canvas(Window._root, background=background)
        canvas.pack(expand=True, fill=tkinter.BOTH)
        Window._canvas = canvas
        
        global _keyboard, _mouse
        _keyboard = KeyBoard()
        _mouse = Mouse()
    
    def size(self, width: int, height: int) -> 'Window':
        if Window._max_width < width or Window._max_height < height:
            if not _Config.IS_ALL_TRACE : _TraceBack()
            raise ValueError(f"指定されたウィンドウサイズ(width:{width}, height:{height})は上限を超えています。width:{Window._max_width}, height:{Window._max_height}以下で設定してください。\nウィンドウサイズをより大きくしたい場合は、windowMaxSize関数を使用して上限サイズを変更してください。") from None
        Window._canvas_height, Window._canvas_width = height, width
        
        Window._root.geometry('{}x{}+0+0'.format(str(Window._canvas_width), str(Window._canvas_height)))
        return self
        
    def title(self, title: str) -> 'Window':
        self.title_text = title
        Window._root.title(str(self.title_text))
        return self
        
    def background(self, background: str) -> 'Window':
        if isinstance(background, Image):
            if not _Config.IS_ALL_TRACE : _TraceBack()
            raise BackgroundException("背景色に画像を指定することはできません") from None
        _checkColor(background)
        self.background_color = background
        Window._canvas.configure(background=self.background_color)
        return self
    
    def getInfo(self) -> dict:
        return {"Object":self.__class__.__name__, "Title":self.title_text, "Size":{"Width":self._canvas_width, "Height":self._canvas_height}, "BackgroundColor":self.background_color}
        
    def show(self) -> None:
        Window._root.mainloop()
    
    @property
    def height(self) -> int:
        return Window._canvas_height
    
    @property
    def width(self) -> int:
        return Window._canvas_width
    
    @staticmethod
    def CANVAS() -> tkinter.Canvas|None :
        return Window._canvas
    
    @staticmethod
    def ROOT() -> tkinter.Tk|None:
        return Window._root
    
    @staticmethod
    def MAX_HEIGHT() -> int:
        return Window._max_height
    
    @staticmethod
    def MAX_WIDTH() -> int:
        return Window._max_width

# figure class (super)
class Figure:    
    def __init__(self):
        self.fill_color = "black"
        self.outline_color = "black"
        self.outline_width = 1
        self.rotate_point = {"x":0, "y":0}
        self.figure = None
        self._INFO_KEYS = {"fill_color":"FillColor", "outline_color":"OutlineFill", "outline_width":"OutlineWidth", "rotate_point":"RotationCenter"}
        self._EXCLUSION_KEYS = ["figure", "_INFO_KEYS", "_EXCLUSION_KEYS"]
        
    def fill(self, color: str):
        self.fill_color = color
        Window.CANVAS().itemconfigure(self.figure, fill=self.fill_color)
        return self
        
    def noFill(self):
        self.fill_color = ""
        Window.CANVAS().itemconfigure(self.figure, fill=self.fill_color)
        return self
        
    def outlineFill(self, color: str):
        self.outline_color = color
        Window.CANVAS().itemconfigure(self.figure, outline=self.outline_color)
        return self
        
    def noOutline(self):
        self.outline_color = ""
        Window.CANVAS().itemconfigure(self.figure, outline=self.outline_color)
        return self
        
    def outlineWidth(self, width: int):
        self.outline_width = width
        Window.CANVAS().itemconfigure(self.figure, width=self.outline_width)
        return self
        
    def setRotationCenter(self, base_x: int, base_y: int):
        self.rotate_point.update({"x":base_x, "y":base_y})
        return self
    
    def getInfo(self) -> dict:
        instance_info = {**{"Object":self.__class__.__name__}, **{self._INFO_KEYS[k]: v for k, v in vars(self).items() if k not in self._EXCLUSION_KEYS}}
        return instance_info
        
    def delete(self):
        Window.CANVAS().delete(self.figure)
 
# figure class
class Line(Figure):
    def __init__(self, startX: int|float, startY: int|float, endX: int|float, endY: int|float, lineWeight: int =1) -> 'Line':
        super().__init__()
        self.point1 = {"x":startX, "y":startY}
        self.point2 = {"x":endX, "y":endY}
        self.line_weight = lineWeight
        self.figure = Window.CANVAS().create_line(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], fill=self.fill_color, width=self.line_weight, tags=Window._tag)
        self._INFO_KEYS.update(point1="Start", point2="End", line_weight="LineWeight")
        
    def lineWeight(self, lineWeight: int) -> 'Line':
        self.line_weight = lineWeight
        Window.CANVAS().itemconfigure(self.figure, width=self.line_weight)
        return self
        
    def rotate(self, angle: int) -> 'Line':
        self.point1.update(_calc_rotate(self.rotate_point, self.point1, angle))
        self.point2.update(_calc_rotate(self.rotate_point, self.point2, angle))
        Window.CANVAS().coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"])
        return self

    def outlineFill(self, color: str) -> Never:
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("LineでoutlineFill関数は使用できません")
    def noOutline(self) -> Never:
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("LineでnoOutline関数は使用できません")
    def outlineWidth(self, width: int) -> Never:
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("LineでoutlineWidth関数は使用できません")
        
class Triangle(Figure):
    def __init__(self, x1: int|float, y1: int|float, x2: int|float, y2: int|float, x3: int|float, y3: int|float):
        super().__init__()
        self.point1 = {"x":x1, "y":y1}
        self.point2 = {"x":x2, "y":y2}
        self.point3 = {"x":x3, "y":y3}
        self.figure = Window.CANVAS().create_polygon(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"], fill=self.fill_color, outline=self.outline_color, width=self.outline_width, tags=Window._tag)
        self._INFO_KEYS.update(point1="Point1", point2="Point2", point3="Point3")

    def rotate(self, angle: int) -> 'Triangle':
        self.point1.update(_calc_rotate(self.rotate_point, self.point1, angle))
        self.point2.update(_calc_rotate(self.rotate_point, self.point2, angle))
        self.point3.update(_calc_rotate(self.rotate_point, self.point3, angle))
        Window.CANVAS().coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"])
        return self

class Rectangle(Figure):
    def __init__(self, x: int|float, y: int|float, width: int|float, height: int|float):
        super().__init__()
        self.size = {"width":width, "height":height}
        self.point1 = {"x":x, "y":y}
        self.point2 = {"x":x+width, "y":y}
        self.point3 = {"x":x+width, "y":y+height}
        self.point4 = {"x":x, "y":y+height}
        self.figure = Window.CANVAS().create_polygon(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"], self.point4["x"], self.point4["y"], fill=self.fill_color, outline=self.outline_color, width=self.outline_width, tags=Window._tag)
        self._INFO_KEYS.update(point1="Point1", point2="Point2", point3="Point3", point4="Point4", size="Size")
        
    def rotate(self, angle: int) -> 'Rectangle':
        self.point1.update(_calc_rotate(self.rotate_point, self.point1, angle))
        self.point2.update(_calc_rotate(self.rotate_point, self.point2, angle))
        self.point3.update(_calc_rotate(self.rotate_point, self.point3, angle))
        self.point4.update(_calc_rotate(self.rotate_point, self.point4, angle))
        Window.CANVAS().coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"], self.point4["x"], self.point4["y"])
        return self
        
class Quad(Figure):
    def __init__(self, x1: int|float, y1: int|float, x2: int|float, y2: int|float, x3: int|float, y3: int|float, x4: int|float, y4: int|float):
        super().__init__()
        self.point1 = {"x":x1, "y":y1}
        self.point2 = {"x":x2, "y":y2}
        self.point3 = {"x":x3, "y":y3}
        self.point4 = {"x":x4, "y":y4}
        self.figure = Window.CANVAS().create_polygon(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"], self.point4["x"], self.point4["y"], fill=self.fill_color, outline=self.outline_color, width=self.outline_width, tags=Window._tag)
        self._INFO_KEYS.update(point1="Point1", point2="Point2", point3="Point3", point4="Point4")

    def rotate(self, angle: int) -> 'Quad':
        self.point1.update(_calc_rotate(self.rotate_point, self.point1, angle))
        self.point2.update(_calc_rotate(self.rotate_point, self.point2, angle))
        self.point3.update(_calc_rotate(self.rotate_point, self.point3, angle))
        self.point4.update(_calc_rotate(self.rotate_point, self.point4, angle))
        Window.CANVAS().coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"], self.point4["x"], self.point4["y"])
        return self

class Ellipse(Figure):
    def __init__(self, x: int|float, y: int|float, width: int|float, height: int|float):
        super().__init__()
        self.figure_center_point = {"x":x, "y":y}
        self.size = {"width":width, "height":height}
        self.point1 = {"x":x-width/2, "y":y-height/2}
        self.point2 = {"x":x+width/2, "y":y+height/2}
        self.figure = Window.CANVAS().create_oval(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], fill=self.fill_color, outline=self.outline_color, width=self.outline_width, tags=Window._tag)
        self._INFO_KEYS.update(figure_center_point="CenterPoint", size="Size")
        self._EXCLUSION_KEYS.extend(["point1", "point2"])
        
    def rotate(self, angle: int) -> 'Ellipse':
        self.figure_center_point.update(_calc_rotate(self.rotate_point, self.figure_center_point, angle))
        self.point1.update({"x":self.figure_center_point["x"]-self.size["width"]/2, "y":self.figure_center_point["y"]-self.size["height"]/2})
        self.point2.update({"x":self.figure_center_point["x"]+self.size["width"]/2, "y":self.figure_center_point["y"]+self.size["height"]/2})
        Window.CANVAS().coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"])
        return self

class Point(Figure):
    def __init__(self, x: int|float, y: int|float, size: int|float):
        super().__init__()
        self.outline_color = ""
        self.figure_center_point = {"x":x, "y":y}
        self.size = size
        self.point1 = {"x":x-size/2, "y":y-size/2}
        self.point2 = {"x":x+size/2, "y":y+size/2}
        self.figure = Window.CANVAS().create_oval(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], fill=self.fill_color, outline=self.outline_color, tags=Window._tag)
        self._INFO_KEYS.update(figure_center_point="CenterPoint", size="Size")
        self._EXCLUSION_KEYS.extend(["point1", "point2"])

    def rotate(self, angle: int):
        self.figure_center_point.update(_calc_rotate(self.rotate_point, self.figure_center_point, angle))
        self.point1.update({"x":self.figure_center_point["x"]-self.size/2, "y":self.figure_center_point["y"]-self.size/2})
        self.point2.update({"x":self.figure_center_point["x"]+self.size/2, "y":self.figure_center_point["y"]+self.size/2})
        Window.CANVAS().coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"])
        return self

    def outlineFill(self, color: str) -> Never:
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("PointでoutlineFill関数は使用できません")
    def noOutline(self) -> Never:
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("PointでnoOutline関数は使用できません")
    def outlineWidth(self, width: int) -> Never:
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("PointでoutlineWidth関数は使用できません")

class Arc(Figure):
    def __init__(self, x: int|float, y: int|float, width: int|float, height: int|float, startAngle: int, interiorAngle: int):
        super().__init__()
        self.figure_center_point = {"x":x, "y":y}
        self.size = {"width":width, "height":height}
        self.point1 = {"x":x-width/2, "y":y-height/2}
        self.point2 = {"x":x+width/2, "y":y+height/2}
        self.start_angle = startAngle
        self.interior_angle = interiorAngle
        self.outline_style = "pieslice"
        self.figure = Window.CANVAS().create_arc(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], start=self.start_angle, extent=self.interior_angle, fill=self.fill_color, outline=self.outline_color, width=self.outline_width, style=self.outline_style, tags=Window._tag)
        self._INFO_KEYS.update(figure_center_point="CenterPoint", size="Size", start_angle="StartAngle", interior_angle="IntoriorAngle", outline_style="OutlineStyle")
        self._EXCLUSION_KEYS.extend(["point1", "point2"])

    def rotate(self, angle: int) -> 'Arc':
        self.figure_center_point.update(_calc_rotate(self.rotate_point, self.figure_center_point, angle))
        self.point1.update({"x":self.figure_center_point["x"]-self.size["width"]/2, "y":self.figure_center_point["y"]-self.size["height"]/2})
        self.point2.update({"x":self.figure_center_point["x"]+self.size["width"]/2, "y":self.figure_center_point["y"]+self.size["height"]/2})
        Window.CANVAS().coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"])
        return self

    def outlineStyle(self, style: str) -> 'Arc':
        styleList = ["pieslice","arc","chord"]
        if style in styleList:
            self.outline_style = style
        else:
            raise ShapeError(f"{style}は使用可能な外枠線のスタイルではありません。扇形'pieslice',円弧'arc',円弧と弦'chord'のいずれかを指定してください。")
        Window.CANVAS().itemconfigure(self.figure, style=self.outline_style)
        return self

# text class
class Text():
    def __init__(self, text: str, x: int|float, y: int|float):
        self.font_name = "TkDefaultFont"
        self.fontsize = 20
        self.center_point = {"x":x, "y":y}
        self.text = text
        self.figure = Window.CANVAS().create_text(x, y, text=self.text, font=(self.font_name, self.fontsize), fill="black", tags=Window._tag)
        self.rotate_point = {"x":0, "y":0}
        self._INFO_KEYS = {"center_point":"CenterPoint", "text":"Text", "font_name":"FontName", "fontsize":"FontSize", "rotate_point":"RotationCenter", "fill_color":"Color"}
        self._EXCLUSION_KEYS = ["figure", "_INFO_KEYS", "_EXCLUSION_KEYS"]
        
    def font(self, fontName: str, fontSize: int) -> 'Text':
        if fontName != "":
            if fontName not in _Config.FONTS:
                if not _Config.IS_ALL_TRACE : _TraceBack()
                raise FontError(f"{fontName}は使用可能なフォントではありません")
            self.font_name = fontName
        self.fontsize = fontSize
        Window.CANVAS().itemconfigure(self.figure, font=(self.font_name, self.fontsize))
        return self
        
    def fill(self, color: str) -> 'Text':
        _checkColor(color)
        self.fill_color = color
        Window.CANVAS().itemconfigure(self.figure, fill=color)
        return self
        
    def rotate(self, angle: int) -> 'Text':
        self.center_point.update(_calc_rotate(self.rotate_point, self.center_point, angle))
        Window.CANVAS().coords(self.figure, self.center_point["x"], self.center_point["y"])
        return self

    def setRotationCenter(self, base_x: int|float, base_y: int|float) -> 'Text':
        self.rotate_point.update({"x":base_x, "y":base_y})
        return self
    
    def getInfo(self) -> dict:
        return {self._INFO_KEYS[k]: v for k, v in vars(self).items() if k not in self._EXCLUSION_KEYS}
    
    def delete(self):
        Window.CANVAS().delete(self.figure)

# image class
def loadImage(filename: str) -> 'Image':
    dataDirPath = Path(stack()[1].filename).parent / Path("data/")
    if not dataDirPath.is_dir():
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise LoadingException("ファイルの読み込みが指示されましたが、dataフォルダがありません。")
    
    filepath = dataDirPath / Path(filename)
    if not filepath.is_file():
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise LoadingException(f"指定されたファイルがないか、ファイルではありません。\n指定されたファイル：{filepath}")
    
    if not (filepath.suffix in ['.png','.jpg']):
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise FileTypeError("指定されたファイルは対応しているファイル形式ではありません。PNG もしくは JPEG の画像ファイルを指定してください。")
    return Image(filepath)
    
class Image():
    def __init__(self, filepath: Path):
        self.file_path = str(filepath)
        self.image = None
        self.anchor = "center"
        self.angle = 0
        self.center_point = {"x":None, "y":None}
        self._INFO_KEYS = {"file_path":"FilePath", "anchor":"AnchorPoint", "angle":"Angle", "center_point":"DrawPoint"}
        self._EXCLUSION_KEYS = ["image", "image_file", "_INFO_KEYS", "_EXCLUSION_KEYS"]
            
    def changeAnchor(self) -> 'Image':
        self.anchor = "nw" if self.anchor=="center" else "center"
        return self
        
    def rotate(self, angle: int) -> 'Image':
        self.angle = angle
        return self
        
    def show(self, x: int|float, y: int|float) -> None:
        self.center_point = {"x":x, "y":y}
        if self.image is not None:
            Window.CANVAS().delete(self.image)
        tmp_img = PILImage.open(self.file_path).convert("RGBA")
        if self.angle != 0:
            tmp_img = tmp_img.rotate(-self.angle, expand=True)
            new_img = PILImage.new("RGBA", tmp_img.size, color=(0,0,0))
            new_img.paste(tmp_img, ((new_img.width - tmp_img.width) // 2,(new_img.height - tmp_img.height) // 2), tmp_img)
        self.image_file = ImageTk.PhotoImage(tmp_img)
        self.image = Window.CANVAS().create_image(x, y, anchor=self.anchor, image=self.image_file)
    
    def getInfo(self) -> dict:
        return {self._INFO_KEYS[k]: v for k, v in vars(self).items() if k not in self._EXCLUSION_KEYS}
    
    def delete(self):
        Window.CANVAS().delete(self.image)

# Music Class
def loadMusic(filename: str) -> 'Music':    
    dataDirPath = Path(stack()[1].filename).parent / Path("data/")
    if not dataDirPath.is_dir():
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise LoadingException("ファイルの読み込みが指示されましたが、dataフォルダがありません。")
    
    filepath = dataDirPath / Path(filename)
    if not filepath.is_file():
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise LoadingException(f"指定されたファイルがありません。\n指定されたファイル：{filepath}")
    
    if not (filepath.suffix.lower() in ['.mp3','.wav']):
        if not _Config.IS_ALL_TRACE : _TraceBack()
        raise FileTypeError("指定されたファイルは対応しているファイル形式ではありません。MP3 もしくは WAV の音楽ファイルを指定してください。")
    
    return Music(filepath)

class Music():
    def __init__(self, filepath: Path):
        self.music_path = str(filepath)
        self._player = Playback(self.music_path)
        
        self._INFO_KEYS = {"music_path":"FilePath"}
        self._EXCLUSION_KEYS = ["_player", "_INFO_KEYS", "_EXCLUSION_KEYS"]   
    
    def play(self) -> None:
        self._player.stop()
        self._player.play()
        Window._root.protocol('WM_DELETE_WINDOW', self._kill)
        
    def stop(self) -> None:
        self._player.stop()
    
    def _kill(self) -> Never:
        self._player.stop()
        sys.exit()
        
    def getInfo(self) -> dict:
        return {self._INFO_KEYS[k]: v for k, v in vars(self).items() if k not in self._EXCLUSION_KEYS}
        
    @property
    def isPlaying(self) -> bool:
        return self._player.playing

# __all__ = ["Window", "Mouse", "animation"]
