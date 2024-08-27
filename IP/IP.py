###
# プログラミング基礎 v1.5.2
###
from collections.abc import Callable, Iterable, Mapping
import tkinter
import tkinter.font as font
import math
import colorsys
import datetime
import subprocess
import platform
from collections import deque
import concurrent.futures
import time
import re
import inspect
import sys
import os
from typing import Any
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
    print("File \"" + inspect.stack()[level].filename + "\", line " + str(inspect.stack()[level].lineno) + ", in " + str(inspect.stack()[level][3])+"\n   " + re.sub("(\[)|(\])|(')|(\")",'',str(inspect.stack()[level][4]))[:-2])

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
_TAG = "onCanvas"

# color
COLOR_MORD = "RGB"
# エラー用
_COLOR = ['black','white','snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace','linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff', 'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender', 'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray', 'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue', 'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue', 'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue', 'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise', 'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green', 'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green', 'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green', 'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow', 'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown', 'indian red', 'saddle brown', 'sandy brown', 'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange', 'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',    'pale violet red', 'maroon', 'medium violet red', 'violet red', 'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',    'thistle', 'snow2', 'snow3',    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
_COLOR_CORD = re.compile('^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$')
_FONTS = ''
_OS = platform.uname().system

# key pressed before
_IS_KEY_PRESSED_BEFORE = None
_IS_MOUSE_PRESSED_BEFORE = None

# pre point
_preMouseX = deque([],4)
_preMouseY = deque([],4)

# thread
_executor = concurrent.futures.ThreadPoolExecutor(max_workers=6)

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
    elif re.match("^#",arg) and not _COLOR_CORD.fullmatch(arg):
        if not _IS_ALL_TRACE : _TraceBack(3)
        raise ColorError(f"{arg} はカラーコードとして不正です")

def _checkProcess(obj, process):
    while process.poll() is None:
        time.sleep(0.5)
    obj.process = None
    
# decolater
# animation
def animation(isAnimated):
    def _ani(func):
        def _reg(*args, **kwargs):
            if isAnimated:
                clear()
            process_start = time.perf_counter()
            func(*args, **kwargs)
            process_time = (time.perf_counter() - process_start)*1000
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
# NOTE:ウィンドウの最大サイズを変化できるようにしてほしいという要望があったため追加
def windowMaxSize(width, height):
    global MAX_WIDTH, MAX_HEIGHT
    MAX_WIDTH, MAX_HEIGHT  = width, height

def colorMode(colorMode):
    if colorMode not in ["HSV", "RGB"]:
        if not _IS_ALL_TRACE :_TraceBack()
        raise ColorError(f"{colorMode} は対応しているカラーモードではありません。HSVもしくはRGBが指定できます")
    global COLOR_MORD
    COLOR_MORD = colorMode
    
def color(v1, v2, v3):
    # NOTE: 先生に相談したところ、floatは許容しないとのことだったため修正
    # NOTE: 値のいずれかのみの型が異なっていた場合に正しくerrorを吐かなかったため修正
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
        v1, v2, v3 = colorsys.hsv_to_rgb(v1/100, v2/100, v3/100)
        v1, v2, v3 = int(v1*255), int(v2*255), int(v3*255)
    return "#"+format(v1,'02x')+format(v2,'02x')+format(v3,'02x')

def availableColors(colorname='all'):
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
    
def availableFonts(fontname='all'):
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

def date():
    date = datetime.datetime.now()
    return f"{date.year}-{date.month}-{date.day}"

def year():
    return datetime.datetime.now().year

def month():
    return datetime.datetime.now().month

def day():
    return datetime.datetime.now().day

def hour():
    return datetime.datetime.now().hour

def minute():
    return datetime.datetime.now().minute

def second():
    return datetime.datetime.now().second

def animationSpeed(rate):
    if type(rate) != int:
        if not _IS_ALL_TRACE : _TraceBack()
        raise ValueError(f"{rate} は整数値ではありません")
    if 1 > rate or rate > 100:
        if not _IS_ALL_TRACE : _TraceBack()
        raise ValueError(f"{rate} はanimationSpeedで指定可能な範囲ではありません")
    global _RATE
    _RATE = 101 - rate
    
# internal function
def _calc_rotate(basePoint, movePoint, angle):
    point = {}
    point["x"] = (movePoint["x"]-basePoint["x"]) * math.cos(math.radians(angle)) - (movePoint["y"]-basePoint["y"]) * math.sin(math.radians(angle)) +basePoint["x"]
    point["y"] = (movePoint["x"]-basePoint["x"]) * math.sin(math.radians(angle)) + (movePoint["y"]-basePoint["y"]) * math.cos(math.radians(angle)) +basePoint["y"]
    return point

# window class
class Window:
    def __init__(self, width=500, height=500, background="white"):
        _checkColor(background)
        global CANVAS, _CANVAS_WIDTH, _CANVAS_HEIGHT, _FONTS, _ROOT
        _CANVAS_WIDTH = width
        _CANVAS_HEIGHT = height
        _ROOT = tkinter.Tk()
        _FONTS = list(font.families(_ROOT))
        _ROOT.resizable(width=False, height=False)
        _ROOT.wm_maxsize(width=MAX_WIDTH,height=MAX_HEIGHT)
        _ROOT.geometry('{}x{}+0+0'.format(str(_CANVAS_WIDTH),str(_CANVAS_HEIGHT)))
        CANVAS = _Canvas_(_ROOT, background=background)
        CANVAS.pack(expand=True, fill=tkinter.BOTH)
    
    def size(self, width, height):
        global _CANVAS_WIDTH, _CANVAS_HEIGHT
        _CANVAS_HEIGHT = height
        _CANVAS_WIDTH = width
        _ROOT.geometry('{}x{}+0+0'.format(str(_CANVAS_WIDTH),str(_CANVAS_HEIGHT)))
        
    def title(self, title):
        _ROOT.title(str(title))
        
    def background(self, background):
        if isinstance(background, Image):
            if not _IS_ALL_TRACE : _TraceBack()
            raise BackgroundException("背景色に画像を指定することはできません") from None
        _checkColor(background)
        CANVAS.configure(background=background)
        
    def show(self):
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
        
    def fill(self, color):
        self.fill_color = color
        CANVAS.itemconfigure(self.figure, fill=self.fill_color)
        
    def noFill(self):
        self.fill_color = ""
        CANVAS.itemconfigure(self.figure, fill=self.fill_color)
        
    def outlineFill(self, color):
        self.outline_color = color
        CANVAS.itemconfigure(self.figure, outline=self.outline_color)
        
    def noOutline(self):
        self.outline_color = ""
        CANVAS.itemconfigure(self.figure, outline=self.outline_color)
        
    def outlineWidth(self, width):
        self.outline_width = width
        CANVAS.itemconfigure(self.figure, width=self.outline_width)
        
    def changeBasePoint(self, base_x, base_y):
        self.rotate_point.update({"x":base_x, "y":base_y})
        
    def delete(self):
        CANVAS.delete(self.figure)
 
# figure class
class Line(Figure):
    def __init__(self, startX, startY, endX, endY, lineWeight=1):
        super().__init__()
        self.point1 = {"x":startX, "y":startY}
        self.point2 = {"x":endX, "y":endY}
        self.line_weight = lineWeight
        self.figure = CANVAS.create_line(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], fill=self.fill_color, width=self.line_weight, tags=_TAG)
        
    def lineWeight(self, lineWeight):
        self.line_weight = lineWeight
        CANVAS.itemconfigure(self.figure, width=self.line_weight)
        
    def rotate(self, angle):
        self.point1.update(_calc_rotate(self.rotate_point, self.point1, angle))
        self.point2.update(_calc_rotate(self.rotate_point, self.point2, angle))
        CANVAS.coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"])

    def outlineFill(self, color):
        if not _IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("LineでoutlineFill関数は使用できません")
    def noOutline(self):
        if not _IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("LineでnoOutline関数は使用できません")
    def outlineWidth(self, width):
        if not _IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("LineでoutlineWidth関数は使用できません")
        
class Triangle(Figure):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__()
        self.point1 = {"x":x1, "y":y1}
        self.point2 = {"x":x2, "y":y2}
        self.point3 = {"x":x3, "y":y3}
        self.figure = CANVAS.create_polygon(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"], fill=self.fill_color, outline=self.outline_color, width=self.outline_width, tags=_TAG)

    def rotate(self, angle):
        self.point1.update(_calc_rotate(self.rotate_point, self.point1, angle))
        self.point2.update(_calc_rotate(self.rotate_point, self.point2, angle))
        self.point3.update(_calc_rotate(self.rotate_point, self.point3, angle))
        CANVAS.coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"])

class Rectangle(Figure):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.point1 = {"x":x, "y":y}
        self.point2 = {"x":x+width, "y":y}
        self.point3 = {"x":x+width, "y":y+height}
        self.point4 = {"x":x, "y":y+height}

        self.figure = CANVAS.create_polygon(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"], self.point4["x"], self.point4["y"], fill=self.fill_color, outline=self.outline_color, width=self.outline_width, tags=_TAG)
        
    def rotate(self, angle):
        self.point1.update(_calc_rotate(self.rotate_point, self.point1, angle))
        self.point2.update(_calc_rotate(self.rotate_point, self.point2, angle))
        self.point3.update(_calc_rotate(self.rotate_point, self.point3, angle))
        self.point4.update(_calc_rotate(self.rotate_point, self.point4, angle))
        CANVAS.coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"], self.point4["x"], self.point4["y"])
        
class Quad(Figure):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__()
        self.point1 = {"x":x1, "y":y1}
        self.point2 = {"x":x2, "y":y2}
        self.point3 = {"x":x3, "y":y3}
        self.point4 = {"x":x4, "y":y4}
        
        self.figure = CANVAS.create_polygon(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"], self.point4["x"], self.point4["y"], fill=self.fill_color, outline=self.outline_color, width=self.outline_width, tags=_TAG)

    def rotate(self, angle):
        self.point1.update(_calc_rotate(self.rotate_point, self.point1, angle))
        self.point2.update(_calc_rotate(self.rotate_point, self.point2, angle))
        self.point3.update(_calc_rotate(self.rotate_point, self.point3, angle))
        self.point4.update(_calc_rotate(self.rotate_point, self.point4, angle))
        CANVAS.coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], self.point3["x"], self.point3["y"], self.point4["x"], self.point4["y"])

class Ellipse(Figure):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.figure_center_point = {"x":x, "y":y}
        self.size = {"width":width, "height":height}
        self.point1 = {"x":x-width/2, "y":y-height/2}
        self.point2 = {"x":x+width/2, "y":y+height/2}
        self.figure = CANVAS.create_oval(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], fill=self.fill_color, outline=self.outline_color, width=self.outline_width, tags=_TAG)

    def rotate(self, angle):
        self.figure_center_point.update(_calc_rotate(self.rotate_point, self.figure_center_point, angle))
        self.point1.update({"x":self.figure_center_point["x"]-self.size["width"]/2, "y":self.figure_center_point["y"]-self.size["height"]/2})
        self.point2.update({"x":self.figure_center_point["x"]+self.size["width"]/2, "y":self.figure_center_point["y"]+self.size["height"]/2})
        CANVAS.coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"])

class Point(Figure):
    def __init__(self, x, y, size):
        super().__init__()
        self.outline_color = ""
        self.figure_center_point = {"x":x, "y":y}
        self.size = size
        self.point1 = {"x":x-size/2, "y":y-size/2}
        self.point2 = {"x":x+size/2, "y":y+size/2}
        self.figure = CANVAS.create_oval(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], fill=self.fill_color, outline=self.outline_color, tags=_TAG)

    def rotate(self, angle):
        self.figure_center_point.update(_calc_rotate(self.rotate_point, self.figure_center_point, angle))
        self.point1.update({"x":self.figure_center_point["x"]-self.size/2, "y":self.figure_center_point["y"]-self.size/2})
        self.point2.update({"x":self.figure_center_point["x"]+self.size/2, "y":self.figure_center_point["y"]+self.size/2})
        CANVAS.coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"])

    def outlineFill(self, color):
        if not _IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("PointでoutlineFill関数は使用できません")
    def noOutline(self):
        if not _IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("PointでnoOutline関数は使用できません")
    def outlineWidth(self, width):
        if not _IS_ALL_TRACE : _TraceBack()
        raise NotFoundFunction("PointでoutlineWidth関数は使用できません")

class Arc(Figure):
    def __init__(self, x, y, width, height, startAngle, interiorAngle):
        super().__init__()
        self.figure_center_point = {"x":x, "y":y}
        self.size = {"width":width, "height":height}
        self.point1 = {"x":x-width/2, "y":y-height/2}
        self.point2 = {"x":x+width/2, "y":y+height/2}
        self.start_angle = startAngle
        self.interior_angle = interiorAngle
        self.outline_style = "pieslice"
        self.figure = CANVAS.create_arc(self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"], start=self.start_angle, extent=self.interior_angle, fill=self.fill_color, outline=self.outline_color, width=self.outline_width, style=self.outline_style, tags=_TAG)

    def rotate(self, angle):
        self.figure_center_point.update(_calc_rotate(self.rotate_point, self.figure_center_point, angle))
        self.point1.update({"x":self.figure_center_point["x"]-self.size["width"]/2, "y":self.figure_center_point["y"]-self.size["height"]/2})
        self.point2.update({"x":self.figure_center_point["x"]+self.size["width"]/2, "y":self.figure_center_point["y"]+self.size["height"]/2})
        CANVAS.coords(self.figure, self.point1["x"], self.point1["y"], self.point2["x"], self.point2["y"])

    def outlineStyle(self, style):
        styleList = ["pieslice","arc","chord"]
        if style in styleList:
            self.outline_style = style
        else:
            raise ShapeError(f"{style}は使用可能な外枠線のスタイルではありません。扇形'pieslice',円弧'arc',円弧と弦'chord'のいずれかを指定してください。")
        CANVAS.itemconfigure(self.figure, style=self.outline_style)

# text class
class Text():
    def __init__(self, text, x, y):
        self.font_name = _DEFAULT_FONT
        self.fontsize = 20
        self.center_point = {"x":x, "y":y}
        self.text = CANVAS.create_text(x, y, text=text, font=(self.font,self.fontsize), fill="black")
        self.rotate_point = {"x":0, "y":0}
        
    def font(self, fontName, fontSize):
        fontName = self.font_name if fontName=="" else fontName
        if _OS == "Linux":
            fontName = "Noto Serif CJK JP"
        if fontName not in _FONTS:
            if not _IS_ALL_TRACE : _TraceBack()
            raise FontError(f"{fontName}は使用可能なフォントではありません")
        self.font_name = fontName
        self.fontsize = fontSize
        CANVAS.itemconfigure(self.text,font=(self.font_name,self.fontsize))
        
    def fill(self, color):
        _checkColor(color)
        CANVAS.itemconfigure(self.text, fill=color)
        
    def rotate(self, angle):
        self.center_point.update(_calc_rotate(self.rotate_point, self.center_point, angle))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

    def changeBasePoint(self, base_x, base_y):
        self.rotate_point.update({"x":base_x, "y":base_y})
    
    def delete(self):
        CANVAS.delete(self.text)

# image class
def loadImage(filename):
    datafilepath = os.path.join(os.path.dirname(inspect.stack()[1].filename),"data")
    if not os.path.isdir(datafilepath):
        if not _IS_ALL_TRACE : _TraceBack()
        raise LoadingException("ファイルの読み込みが指示されましたが、dataフォルダがありません。")
    
    filepath = os.path.join(datafilepath,filename)
    if not os.path.isfile(filepath):
        if not _IS_ALL_TRACE : _TraceBack()
        raise LoadingException(f"指定されたファイルがありません。\n指定されたファイル：{filepath}")
    
    if not str(filename).lower().endswith(('.pgm','.ppm','.gif','.png','.xbm')):
        if not _IS_ALL_TRACE : _TraceBack()
        raise FileTypeError("指定されたファイルは対応しているファイル形式ではありません。PGM,PPM,GIF,PNG,XBMのいずれかの画像ファイルを指定してください。")
    return Image(filepath)
    
class Image():
    def __init__(self, filepath):
        self.file_path = filepath
        self.image_file = tkinter.PhotoImage(file=self.file_path)
        self.image = None
        self.anchor = "center"
            
    def changeAnchor(self):
        self.anchor = "nw" if self.anchor=="center" else "center"
        
    def show(self, x, y):
        if self.image is None:
            CANVAS.delete(self.image)
        self.image = CANVAS.create_image(x, y, anchor=self.anchor, image=self.image_file)
    
    def delete(self):
        CANVAS.delete(self.image)

# Music Class
def loadMusic(filename):
    if _OS == 'Windows':
        if not _IS_ALL_TRACE : _TraceBack()
        raise EnvironmentException("MusicはWindowsで利用できません")
    
    datafilepath = os.path.join(os.path.dirname(inspect.stack()[1].filename),"data")
    if not os.path.isdir(datafilepath):
        if not _IS_ALL_TRACE : _TraceBack()
        raise LoadingException("ファイルの読み込みが指示されましたが、dataフォルダがありません。")
    
    filepath = os.path.join(datafilepath,filename)
    if not os.path.isfile(filepath):
        if not _IS_ALL_TRACE : _TraceBack()
        raise LoadingException(f"指定されたファイルがありません。\n指定されたファイル：{filepath}")
    
    return Music(filepath)

class Music:
    def __init__(self, filepath):
        self.music_path = filepath
        self.process = None        

    def play(self):
        if self.process is None :
            if _OS == "Darwin":
                self.process = subprocess.Popen(['afplay', self.music_path])
            elif _OS == "Linux":
                self.process = subprocess.Popen(['mpv', '--no-video', self.music_path])
            _ROOT.protocol('WM_DELETE_WINDOW', self._kill)
            _executor.submit(lambda:_checkProcess(self,self.process))
    
    def stop(self):
        if self.process is not None:
            self.process.kill()
        self.process = None
    
    def _kill(self):
        if self.process is not None:
            self.process.kill()
        sys.exit()
