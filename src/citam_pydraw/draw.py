###
# プログラミング基礎 v1.5.6
###
import tkinter
import tkinter.font as font
from math import sin, cos, radians
from colorsys import hsv_to_rgb
import datetime
import subprocess
from platform import uname
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from time import sleep,perf_counter
from re import sub, compile, match
from inspect import stack
import sys
from pathlib import Path
from typing import Final, Pattern, Never
from PIL import Image as PILImage
from PIL import ImageTk
from . import mouse
from . import keyboard

# stack trace
_IS_ALL_TRACE = False
def allTraceBack():
    global _IS_ALL_TRACE
    _IS_ALL_TRACE = not _IS_ALL_TRACE

def _TraceBack(level=2,limit=0):
    sys.tracebacklimit=limit
    print("\nTraceback (most recent call last):")
    print("File \"" + stack()[level].filename + "\", line " + str(stack()[level].lineno) + ", in " + str(stack()[level][3])+"\n   " + sub("(\[)|(\])|(')|(\")",'',str(stack()[level][4]))[:-2])

# animation
_RATE = 30

# window
MAX_HEIGHT = 700
MAX_WIDTH = 1000

# canvas
_ROOT = None
CANVAS = None
_CANVAS_WIDTH = 500
_CANVAS_HEIGHT = 500
_IS_DRAW_MOVED = True

# fig tag
_TAG: Final = "onCanvas"

# color
COLOR_MORD = "RGB"
# エラー用
_COLOR = ['black','white','snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace','linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff', 'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender', 'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray', 'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue', 'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue', 'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue', 'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise', 'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green', 'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green', 'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green', 'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow', 'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown', 'indian red', 'saddle brown', 'sandy brown', 'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange', 'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',    'pale violet red', 'maroon', 'medium violet red', 'violet red', 'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',    'thistle', 'snow2', 'snow3',    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
_COLOR_CORD: Pattern[str] = compile('^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$')
_FONTS = None
_OS = uname().system

# key pressed before
_IS_KEY_PRESSED_BEFORE = False
_IS_MOUSE_PRESSED_BEFORE = False

# pre point
_preMouseX: deque[int] = deque([],4)
_preMouseY: deque[int] = deque([],4)

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

# default font
_DEFAULT_FONT = ""
if _OS == "Darwin":
    _DEFAULT_FONT = "Helvetica"
elif _OS == "Windows":
    _DEFAULT_FONT = "Segoe UI"
elif _OS == "Linux":
    _DEFAULT_FONT = "Noto Serif CJK JP"

def _checkColor(arg):
    if arg in _COLOR or _COLOR_CORD.fullmatch(arg):
        return
    elif arg not in _COLOR:
        if not _IS_ALL_TRACE : _TraceBack(3)
        raise ColorError(f"{arg} は指定可能な色名ではありません")
    elif match("^#",arg) and not _COLOR_CORD.fullmatch(arg):
        if not _IS_ALL_TRACE : _TraceBack(3)
        raise ColorError(f"{arg} はカラーコードとして不正です")

def _checkProcess(obj, process):
    while process.poll() is None:
        sleep(0.5)
    obj.process = None
    
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
            call_time = _RATE if process_time < _RATE else int(process_time)
            if isAnimated and call_time > 1000 :
                if not _IS_ALL_TRACE : _TraceBack(2)
                raise ProcessingIsLaggy("描画する関数の処理時間が1秒を超えています。PCに負荷がかかっているか、関数内の処理が重すぎます")
            if _IS_DRAW_MOVED:
                CANVAS.after(call_time, _ani(func))
        return _reg
    return _ani

# event
def mouseMoved(func):
    def _reg(*args, **kwargs):
        def tmp():
            if not mouse.isPressed:
                if 0 < mouse.X < _CANVAS_WIDTH and 0 < mouse.Y < _CANVAS_HEIGHT:
                    _executor.submit(lambda:func(*args, **kwargs))
        CANVAS.bind("<Motion>", tmp())
    return _reg

def mousePressed(func):
    def _reg(*args, **kwargs):
        def tmp():
            global _IS_MOUSE_PRESSED_BEFORE
            if mouse.isPressed  and not _IS_MOUSE_PRESSED_BEFORE:
                _executor.submit(lambda:func(*args, **kwargs))
                _IS_MOUSE_PRESSED_BEFORE = True
        CANVAS.bind("<ButtonPress>", tmp())
    return _reg

def mouseReleased(func):
    def _reg(*args, **kwargs):
        def tmp():
            global _IS_MOUSE_PRESSED_BEFORE
            if _IS_MOUSE_PRESSED_BEFORE:
                _executor.submit(lambda:func(*args, **kwargs))
                _IS_MOUSE_PRESSED_BEFORE = False
        CANVAS.bind("<ButtonRelease>", tmp())
    return _reg

def mouseDragged(func):
    def _reg(*args, **kwargs):
        def tmp():
            if mouse.isPressed:
                func(*args, **kwargs)
                mouse.pressX, mouse.pressY = mouse.X, mouse.Y
        CANVAS.bind("<Motion>", tmp())
    return _reg

def keyPressed(func):
    def _reg(*args, **kwargs):
        def tmp():
            if keyboard.isPressed:
                _executor.submit(lambda:func(*args, **kwargs))
        CANVAS.bind("<KeyPressed>", tmp())
    return _reg

def keyReleased(func):
    def _reg(*args, **kwargs):
        def tmp():
            global _IS_KEY_PRESSED_BEFORE
            if _IS_KEY_PRESSED_BEFORE and not keyboard.isPressed:
                _executor.submit(lambda:func(*args, **kwargs))
                _IS_KEY_PRESSED_BEFORE = False
        CANVAS.bind("<KeyRelease>", tmp())
    return _reg


# callable function
def windowMaxSize(width: int, height: int) -> None:
    global MAX_WIDTH, MAX_HEIGHT
    MAX_WIDTH, MAX_HEIGHT  = width, height

def colorMode(colorMode: str) -> None:
    if colorMode not in ["HSV", "RGB"]:
        if not _IS_ALL_TRACE :_TraceBack()
        raise ColorError(f"{colorMode} は対応しているカラーモードではありません。HSVもしくはRGBが指定できます")
    global COLOR_MORD
    COLOR_MORD = colorMode
    
def color(v1: int, v2: int, v3: int):
    if type(v1)!=int or type(v2)!=int or type(v3)!=int:
        if not _IS_ALL_TRACE : _TraceBack()
        raise ColorError(f"color({v1},{v2},{v3}) で指定されたいずれかの値が整数ではありません")
    if v1<0 or v2<0 or v3<0:
        if not _IS_ALL_TRACE : _TraceBack()
        raise ColorError("色の指定に0以下は使用できません")
    if COLOR_MORD == "RGB":
        if v1>255 or v2>255 or v3>255:
            if not _IS_ALL_TRACE : _TraceBack()
            raise ColorError(f"color({v1},{v2},{v3}) はRGBで指定可能な範囲を超えています")
    else:
        if v1>100 or v2>100 or v3>100:
            if not _IS_ALL_TRACE : _TraceBack()
            raise ColorError(f"color({v1},{v2},{v3}) はHSVで指定可能な範囲を超えています")
        v1, v2, v3 = hsv_to_rgb(v1/100, v2/100, v3/100)
        v1, v2, v3 = int(v1*255), int(v2*255), int(v3*255)
    return "#"+format(v1,'02x')+format(v2,'02x')+format(v3,'02x')

def availableColors(colorname: str ='all'):
    if colorname != 'all':
        if colorname in _COLOR:
            print(f"{colorname}は使用可能です")
        else:
            print(f"{colorname}は使用できません")
    else:
        root = tkinter.Tk()
        root.title("色名と色")
        r = 0
        c = 0
        frame = tkinter.Frame(root)
        for color in _COLOR:
            label = tkinter.Label(frame, text=color, bg=color,font=(_DEFAULT_FONT, 10, "bold"))
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
    CANVAS.delete(_TAG)

def stop():
    global _IS_DRAW_MOVED
    _IS_DRAW_MOVED = False

def date() -> str:
    date = datetime.datetime.now()
    return f"{date.year}-{date.month}-{date.day}"

def year() -> int:
    return datetime.datetime.now().year

def month() -> int:
    return datetime.datetime.now().month

def day() -> int:
    return datetime.datetime.now().day

def hour() -> int:
    return datetime.datetime.now().hour

def minute() -> int:
    return datetime.datetime.now().minute

def second() -> int:
    return datetime.datetime.now().second

def animationSpeed(rate: int):
    if type(rate) != int:
        if not _IS_ALL_TRACE : _TraceBack()
        raise ValueError(f"{rate} は整数値ではありません")
    if 1 > rate or rate > 100:
        if not _IS_ALL_TRACE : _TraceBack()
        raise ValueError(f"{rate} はanimationSpeedで指定可能な範囲ではありません")
    global _RATE
    _RATE = 101 - rate
    
# internal function
def _calc_rotate(basePoint: dict, movePoint: dict, angle: int|float) -> dict:
    point = {}
    point["x"] = (movePoint["x"]-basePoint["x"]) * cos(radians(angle)) - (movePoint["y"]-basePoint["y"]) * sin(radians(angle)) +basePoint["x"]
    point["y"] = (movePoint["x"]-basePoint["x"]) * sin(radians(angle)) + (movePoint["y"]-basePoint["y"]) * cos(radians(angle)) +basePoint["y"]
    return point

# window class
class Window:
    def __init__(self, width: int =500, height: int =500, background: str ="white") -> 'Window':
        global CANVAS, _CANVAS_WIDTH, _CANVAS_HEIGHT, _FONTS, _ROOT
        
        self.title_text = None
        self.background_color = background
        
        if MAX_WIDTH < width or MAX_HEIGHT < height:
            print(MAX_WIDTH < width, MAX_HEIGHT < height)
            if not _IS_ALL_TRACE : _TraceBack()
            raise ValueError(f"指定されたウィンドウサイズ(width:{width}, height:{height})は上限値を超えています。width:{MAX_WIDTH}, height:{MAX_HEIGHT}以下で設定してください。\nウィンドウサイズをより大きくしたい場合は、windowMaxSize関数を使用して上限サイズを変更してください。") from None
        _CANVAS_HEIGHT, _CANVAS_WIDTH = height, width
        _checkColor(background)
        
        _ROOT = tkinter.Tk()
        _FONTS = list(font.families(_ROOT))
        _ROOT.resizable(width=False, height=False)
        # _ROOT.wm_maxsize(width=MAX_WIDTH, height=MAX_HEIGHT)
        _ROOT.geometry('{}x{}+0+0'.format(str(_CANVAS_WIDTH), str(_CANVAS_HEIGHT)))
        CANVAS = _Canvas_(_ROOT, background=background)
        CANVAS.pack(expand=True, fill=tkinter.BOTH)
    
    def size(self, width: int, height: int) -> 'Window':
        global _CANVAS_WIDTH, _CANVAS_HEIGHT
        if MAX_WIDTH < width or MAX_HEIGHT < height:
            if not _IS_ALL_TRACE : _TraceBack()
            raise ValueError(f"指定されたウィンドウサイズ(width:{width}, height:{height})は上限を超えています。width:{MAX_WIDTH}, height:{MAX_HEIGHT}以下で設定してください。\nウィンドウサイズをより大きくしたい場合は、windowMaxSize関数を使用して上限サイズを変更してください。") from None
        _CANVAS_HEIGHT, _CANVAS_WIDTH = height, width
        
        _ROOT.geometry('{}x{}+0+0'.format(str(_CANVAS_WIDTH), str(_CANVAS_HEIGHT)))
        return self
        
    def title(self, title: str) -> 'Window':
        self.title_text = title
        _ROOT.title(str(self.title_text))
        return self
        
    def background(self, background: str) -> 'Window':
        if isinstance(background, Image):
            if not _IS_ALL_TRACE : _TraceBack()
            raise BackgroundException("背景色に画像を指定することはできません") from None
        _checkColor(background)
        self.background_color = background
        CANVAS.configure(background=self.background_color)
        return self
    
    def getInfo(self) -> dict:
        return {"Object":self.__class__.__name__, "Title":self.title_text, "Size":{"Width":_CANVAS_WIDTH, "Height":_CANVAS_HEIGHT}, "BackgroundColor":self.background_color}
        
    def show(self) -> None:
        _ROOT.mainloop()
        

# canvas class
class _Canvas_(tkinter.Canvas):
    def __init__(self, master, background):
        super().__init__(
            master,
            background=background,
        )
        self.bind("<Motion>", self.mousePosition)
        self.bind("<ButtonPress>", self.mousePress)
        self.bind("<ButtonRelease>", self.mouseRelease)
        master.bind("<KeyPress>", self.keyPress)
        master.bind("<KeyRelease>", self.keyRelease)

    def mousePosition(self, event):
        _preMouseX.append(mouse.X)
        _preMouseY.append(mouse.Y)
        if len(_preMouseY) > 3:
            mouse.beforeX, mouse.beforeY = _preMouseX.popleft(), _preMouseY.popleft()
        mouse.X, mouse.Y = event.x, event.y
        
    def mousePress(self, event):
        # NOTE: macのトラックパッドだと1本が1,2本が2,3は返ってこない
        mouse.pressX, mouse.pressY = event.x, event.y
        button = ["left", "right", "center"]
        mouse.mouseButton = button[event.num-1]
        mouse.isPressed = True
        global _IS_MOUSE_PRESSED_BEFORE
        _IS_MOUSE_PRESSED_BEFORE = False
        
    def mouseRelease(self, event):
        mouse.clickX, mouse.clickY = event.x, event.y
        mouse.isPressed = False
        global _IS_MOUSE_PRESSED_BEFORE
        _IS_MOUSE_PRESSED_BEFORE = True
        
    def keyPress(self, event):
        keyboard.key, keyboard.char = event.keysym, event.char
        try:
            keyboard.code = ord(event.keysym)
        except :
            keyboard.code = event.keycode
        keyboard.isPressed = True
        global _IS_KEY_PRESSED_BEFORE
        _IS_KEY_PRESSED_BEFORE = False
        
    def keyRelease(self, event):
        keyboard.isPressed = False
        global _IS_KEY_PRESSED_BEFORE
        _IS_KEY_PRESSED_BEFORE = True


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
        CANVAS.itemconfigure(self.figure, fill=self.fill_color)
        return self
        
    def noFill(self):
        self.fill_color = ""
        CANVAS.itemconfigure(self.figure, fill=self.fill_color)
        return self
        
    def outlineFill(self, color: str):
        self.outline_color = color
        CANVAS.itemconfigure(self.figure, outline=self.outline_color)
        return self
        
    def noOutline(self):
        self.outline_color = ""
        CANVAS.itemconfigure(self.figure, outline=self.outline_color)
        return self
        
    def outlineWidth(self, width: int):
        self.outline_width = width
        CANVAS.itemconfigure(self.figure, width=self.outline_width)
        return self
        
    def changeBasePoint(self, base_x: int, base_y: int):
        self.rotate_point.update({"x":base_x, "y":base_y})
        return self
    
    def getInfo(self) -> dict:
        instance_info = {**{"Object":self.__class__.__name__}, **{self._INFO_KEYS[k]: v for k, v in vars(self).items() if k not in self._EXCLUSION_KEYS}}
        return instance_info
        
    def delete(self):
        CANVAS.delete(self.figure)
 
# figure class
class Line(Figure):
    def __init__(self, startX: int|float, startY: int|float, endX: int|float, endY: int|float, lineWeight: int =1) -> 'Line':
        super().__init__()
        self.point1 = {"x":startX, "y":startY}
        self.point2 = {"x":endX, "y":endY}
        self.line_weight = lineWeight
        self.figure = CANVAS.create_line(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], fill=self.fill_color, width=self.line_weight, tags=_TAG)
        self._INFO_KEYS.update(point1="Start", point2="End", line_weight="LineWeight")
        
    def lineWeight(self, lineWeight: int) -> 'Line':
        self.line_weight = lineWeight
        CANVAS.itemconfigure(self.figure, width=self.line_weight)
        return self
        
    def rotate(self, angle: int) -> 'Line':
        self.point1.update(_calc_rotate(self.rotate_point, self.point1, angle))
        self.point2.update(_calc_rotate(self.rotate_point, self.point2, angle))
        CANVAS.coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"])
        return self

    def outlineFill(self, color: str) -> Never:
        if not _IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("LineでoutlineFill関数は使用できません")
    def noOutline(self) -> Never:
        if not _IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("LineでnoOutline関数は使用できません")
    def outlineWidth(self, width: int) -> Never:
        if not _IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("LineでoutlineWidth関数は使用できません")
        
class Triangle(Figure):
    def __init__(self, x1: int|float, y1: int|float, x2: int|float, y2: int|float, x3: int|float, y3: int|float):
        super().__init__()
        self.point1 = {"x":x1, "y":y1}
        self.point2 = {"x":x2, "y":y2}
        self.point3 = {"x":x3, "y":y3}
        self.figure = CANVAS.create_polygon(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"], fill=self.fill_color, outline=self.outline_color, width=self.outline_width, tags=_TAG)
        self._INFO_KEYS.update(point1="Point1", point2="Point2", point3="Point3")

    def rotate(self, angle: int) -> 'Triangle':
        self.point1.update(_calc_rotate(self.rotate_point, self.point1, angle))
        self.point2.update(_calc_rotate(self.rotate_point, self.point2, angle))
        self.point3.update(_calc_rotate(self.rotate_point, self.point3, angle))
        CANVAS.coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"])
        return self

class Rectangle(Figure):
    def __init__(self, x: int|float, y: int|float, width: int|float, height: int|float):
        super().__init__()
        self.size = {"width":width, "height":height}
        self.point1 = {"x":x, "y":y}
        self.point2 = {"x":x+width, "y":y}
        self.point3 = {"x":x+width, "y":y+height}
        self.point4 = {"x":x, "y":y+height}
        self.figure = CANVAS.create_polygon(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"], self.point4["x"], self.point4["y"], fill=self.fill_color, outline=self.outline_color, width=self.outline_width, tags=_TAG)
        self._INFO_KEYS.update(point1="Point1", point2="Point2", point3="Point3", point4="Point4", size="Size")
        
    def rotate(self, angle: int) -> 'Rectangle':
        self.point1.update(_calc_rotate(self.rotate_point, self.point1, angle))
        self.point2.update(_calc_rotate(self.rotate_point, self.point2, angle))
        self.point3.update(_calc_rotate(self.rotate_point, self.point3, angle))
        self.point4.update(_calc_rotate(self.rotate_point, self.point4, angle))
        CANVAS.coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"], self.point4["x"], self.point4["y"])
        return self
        
class Quad(Figure):
    def __init__(self, x1: int|float, y1: int|float, x2: int|float, y2: int|float, x3: int|float, y3: int|float, x4: int|float, y4: int|float):
        super().__init__()
        self.point1 = {"x":x1, "y":y1}
        self.point2 = {"x":x2, "y":y2}
        self.point3 = {"x":x3, "y":y3}
        self.point4 = {"x":x4, "y":y4}
        self.figure = CANVAS.create_polygon(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"], self.point4["x"], self.point4["y"], fill=self.fill_color, outline=self.outline_color, width=self.outline_width, tags=_TAG)
        self._INFO_KEYS.update(point1="Point1", point2="Point2", point3="Point3", point4="Point4")

    def rotate(self, angle: int) -> 'Quad':
        self.point1.update(_calc_rotate(self.rotate_point, self.point1, angle))
        self.point2.update(_calc_rotate(self.rotate_point, self.point2, angle))
        self.point3.update(_calc_rotate(self.rotate_point, self.point3, angle))
        self.point4.update(_calc_rotate(self.rotate_point, self.point4, angle))
        CANVAS.coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"], self.point4["x"], self.point4["y"])
        return self

class Ellipse(Figure):
    def __init__(self, x: int|float, y: int|float, width: int|float, height: int|float):
        super().__init__()
        self.figure_center_point = {"x":x, "y":y}
        self.size = {"width":width, "height":height}
        self.point1 = {"x":x-width/2, "y":y-height/2}
        self.point2 = {"x":x+width/2, "y":y+height/2}
        self.figure = CANVAS.create_oval(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], fill=self.fill_color, outline=self.outline_color, width=self.outline_width, tags=_TAG)
        self._INFO_KEYS.update(figure_center_point="CenterPoint", size="Size")
        self._EXCLUSION_KEYS.extend(["point1", "point2"])
        
    def rotate(self, angle: int) -> 'Ellipse':
        self.figure_center_point.update(_calc_rotate(self.rotate_point, self.figure_center_point, angle))
        self.point1.update({"x":self.figure_center_point["x"]-self.size["width"]/2, "y":self.figure_center_point["y"]-self.size["height"]/2})
        self.point2.update({"x":self.figure_center_point["x"]+self.size["width"]/2, "y":self.figure_center_point["y"]+self.size["height"]/2})
        CANVAS.coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"])
        return self

class Point(Figure):
    def __init__(self, x: int|float, y: int|float, size: int|float):
        super().__init__()
        self.outline_color = ""
        self.figure_center_point = {"x":x, "y":y}
        self.size = size
        self.point1 = {"x":x-size/2, "y":y-size/2}
        self.point2 = {"x":x+size/2, "y":y+size/2}
        self.figure = CANVAS.create_oval(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], fill=self.fill_color, outline=self.outline_color, tags=_TAG)
        self._INFO_KEYS.update(figure_center_point="CenterPoint", size="Size")
        self._EXCLUSION_KEYS.extend(["point1", "point2"])

    def rotate(self, angle: int):
        self.figure_center_point.update(_calc_rotate(self.rotate_point, self.figure_center_point, angle))
        self.point1.update({"x":self.figure_center_point["x"]-self.size/2, "y":self.figure_center_point["y"]-self.size/2})
        self.point2.update({"x":self.figure_center_point["x"]+self.size/2, "y":self.figure_center_point["y"]+self.size/2})
        CANVAS.coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"])
        return self

    def outlineFill(self, color: str) -> Never:
        if not _IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("PointでoutlineFill関数は使用できません")
    def noOutline(self) -> Never:
        if not _IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("PointでnoOutline関数は使用できません")
    def outlineWidth(self, width: int) -> Never:
        if not _IS_ALL_TRACE : _TraceBack()
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
        self.figure = CANVAS.create_arc(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], start=self.start_angle, extent=self.interior_angle, fill=self.fill_color, outline=self.outline_color, width=self.outline_width, style=self.outline_style, tags=_TAG)
        self._INFO_KEYS.update(figure_center_point="CenterPoint", size="Size", start_angle="StartAngle", interior_angle="IntoriorAngle", outline_style="OutlineStyle")
        self._EXCLUSION_KEYS.extend(["point1", "point2"])

    def rotate(self, angle: int) -> 'Arc':
        self.figure_center_point.update(_calc_rotate(self.rotate_point, self.figure_center_point, angle))
        self.point1.update({"x":self.figure_center_point["x"]-self.size["width"]/2, "y":self.figure_center_point["y"]-self.size["height"]/2})
        self.point2.update({"x":self.figure_center_point["x"]+self.size["width"]/2, "y":self.figure_center_point["y"]+self.size["height"]/2})
        CANVAS.coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"])
        return self

    def outlineStyle(self, style: str) -> 'Arc':
        styleList = ["pieslice","arc","chord"]
        if style in styleList:
            self.outline_style = style
        else:
            raise ShapeError(f"{style}は使用可能な外枠線のスタイルではありません。扇形'pieslice',円弧'arc',円弧と弦'chord'のいずれかを指定してください。")
        CANVAS.itemconfigure(self.figure, style=self.outline_style)
        return self

# text class
class Text():
    def __init__(self, text: str, x: int|float, y: int|float):
        self.font_name = _DEFAULT_FONT
        self.fontsize = 20
        self.center_point = {"x":x, "y":y}
        self.text = text
        self.figure = CANVAS.create_text(x, y, text=self.text, font=(self.font, self.fontsize), fill="black", tags=_TAG)
        self.rotate_point = {"x":0, "y":0}
        self._INFO_KEYS = {"center_point":"CenterPoint", "text":"Text", "font_name":"FontName", "fontsize":"FontSize", "rotate_point":"BasePoint", "fill_color":"Color"}
        self._EXCLUSION_KEYS = ["figure", "_INFO_KEYS", "_EXCLUSION_KEYS"]
        
    def font(self, fontName: str, fontSize: int) -> 'Text':
        fontName = self.font_name if fontName == "" else fontName
        if _OS == "Linux":
            fontName = "Noto Serif CJK JP"
        if fontName not in _FONTS:
            if not _IS_ALL_TRACE : _TraceBack()
            raise FontError(f"{fontName}は使用可能なフォントではありません")
        self.font_name = fontName
        self.fontsize = fontSize
        CANVAS.itemconfigure(self.figure, font=(self.font_name, self.fontsize))
        return self
        
    def fill(self, color: str) -> 'Text':
        _checkColor(color)
        self.fill_color = color
        CANVAS.itemconfigure(self.figure, fill=color)
        return self
        
    def rotate(self, angle: int) -> 'Text':
        self.center_point.update(_calc_rotate(self.rotate_point, self.center_point, angle))
        CANVAS.coords(self.figure, self.center_point["x"], self.center_point["y"])
        return self

    def changeBasePoint(self, base_x: int|float, base_y: int|float) -> 'Text':
        self.rotate_point.update({"x":base_x, "y":base_y})
        return self
    
    def getInfo(self) -> dict:
        return {self._INFO_KEYS[k]: v for k, v in vars(self).items() if k not in self._EXCLUSION_KEYS}
    
    def delete(self):
        CANVAS.delete(self.figure)

# image class
def loadImage(filename: str) -> 'Image':
    dataDirPath = Path(stack()[1].filename).parent / Path("data/")
    if not dataDirPath.is_dir():
        if not _IS_ALL_TRACE : _TraceBack()
        raise LoadingException("ファイルの読み込みが指示されましたが、dataフォルダがありません。")
    
    filepath = dataDirPath / Path(filename)
    if not filepath.is_file():
        if not _IS_ALL_TRACE : _TraceBack()
        raise LoadingException(f"指定されたファイルがないか、ファイルではありません。\n指定されたファイル：{filepath}")
    
    if not (filepath.suffix in ['.png','.jpg']):
        if not _IS_ALL_TRACE : _TraceBack()
        raise FileTypeError("指定されたファイルは対応しているファイル形式ではありません。PNG もしくは JPEG の画像ファイルを指定してください。")
    return Image(filepath)
    
class Image():
    def __init__(self, filepath: Path):
        self.file_path = str(filepath)
        self.image = None
        self.anchor = "center"
        self.angle = 0
        self._INFO_KEYS = {"file_path":"FilePath", "anchor":"AnchorPoint", "angle":"Angle"}
        self._EXCLUSION_KEYS = ["image", "image_file", "_INFO_KEYS", "_EXCLUSION_KEYS"]
            
    def changeAnchor(self) -> 'Image':
        self.anchor = "nw" if self.anchor=="center" else "center"
        return self
        
    def rotate(self, angle: int) -> 'Image':
        self.angle = angle
        return self
        
    def show(self, x: int|float, y: int|float) -> None:
        if self.image is not None:
            CANVAS.delete(self.image)
        tmp_img = PILImage.open(self.file_path).convert("RGBA")
        if self.angle != 0:
            tmp_img = tmp_img.rotate(-self.angle, expand=True)
            new_img = PILImage.new("RGBA", tmp_img.size, color=(0,0,0))
            new_img.paste(tmp_img, ((new_img.width - tmp_img.width) // 2,(new_img.height - tmp_img.height) // 2), tmp_img)
        self.image_file = ImageTk.PhotoImage(tmp_img)
        self.image = CANVAS.create_image(x, y, anchor=self.anchor, image=self.image_file)
    
    def getInfo(self) -> dict:
        return {self._INFO_KEYS[k]: v for k, v in vars(self).items() if k not in self._EXCLUSION_KEYS}
    
    def delete(self):
        CANVAS.delete(self.image)

# Music Class
def loadMusic(filename: str) -> 'Music':
    if _OS == 'Windows':
        if not _IS_ALL_TRACE : _TraceBack()
        raise EnvironmentException("MusicはWindowsで利用できません")
    
    dataDirPath = Path(stack()[1].filename).parent / Path("data/")
    if not dataDirPath.is_dir():
        if not _IS_ALL_TRACE : _TraceBack()
        raise LoadingException("ファイルの読み込みが指示されましたが、dataフォルダがありません。")
    
    filepath = dataDirPath / Path(filename)
    if not filepath.is_file():
        if not _IS_ALL_TRACE : _TraceBack()
        raise LoadingException(f"指定されたファイルがありません。\n指定されたファイル：{filepath}")
    
    return Music(filepath)

class Music:
    def __init__(self, filepath: Path):
        self.music_path = str(filepath)
        self.process = None
        self._INFO_KEYS = {"music_path":"FilePath"}
        self._EXCLUSION_KEYS = ["process", "_INFO_KEYS", "_EXCLUSION_KEYS"]   
    
    def getInfo(self) -> dict:
        return {self._INFO_KEYS[k]: v for k, v in vars(self).items() if k not in self._EXCLUSION_KEYS}
 

    def play(self) -> int:
        if self.process is None :
            if _OS == "Darwin":
                self.process = subprocess.Popen(['afplay', self.music_path])
            elif _OS == "Linux":
                self.process = subprocess.Popen(['mpv', '--no-video', "--ao=pulse", self.music_path])
            _ROOT.protocol('WM_DELETE_WINDOW', self._kill)
            _executor.submit(lambda:_checkProcess(self,self.process))
            return 0 # 正常動作
        return 1 # すでに再生されているため再生不可
    
    def stop(self):
        if self.process is not None:
            self.process.kill()
        self.process = None
    
    def _kill(self) -> Never:
        if self.process is not None:
            self.process.kill()
        sys.exit()
