# run with python3
from ApplicationServices import *
import tkinter as tk

# whether to dump all key events to stdout
keylogger = False;
nobg = True;


# here defines four keyboard areas from left to right
# special rules: x in l2 (for osu); [left] in r1 for other games

l1keys = set('`1qaz2ws');
l2keys = set('3edc4rfv5tgb x');
r1keys = set('6yhn7ujm8ik,');
r2keys = set('9ol.0p;/-[=]');

l1keys.add("[tab]");
l1keys.add("[esc]");
l1keys.add("[caps]");
l1keys.add("[left-ctrl]");
l1keys.add("[left-shift]");
l1keys.add("[left-option]");
l1keys.add("[f1]");
l1keys.add("[f2]");

l2keys.add("[left-cmd]");
l2keys.add("[f3]");
l2keys.add("[f4]");
l2keys.add("[f5]");

r1keys.add("[right-cmd]");
r1keys.add("[F6]");
r1keys.add("[F7]");
r1keys.add("[F8]");
r1keys.add("[left]");

r2keys.add("\\");
r2keys.add("'");
r2keys.add("[right-ctrl]");
r2keys.add("[right-shift]");
r2keys.add("[right-option]");
r2keys.add("[F9]");
r2keys.add("[F10]");
r2keys.add("[F11]");
r2keys.add("[F12]");
# all other keys are automatically put into r2keys


# translated from GiacomoLaw/Keylogger
def convertKeyCode(keyCode):
    a = {
        0:   "a",
        1:   "s",
        2:   "d",
        3:   "f",
        4:   "h",
        5:   "g",
        6:   "z",
        7:   "x",
        8:   "c",
        9:   "v",
        11:  "b",
        12:  "q",
        13:  "w",
        14:  "e",
        15:  "r",
        16:  "y",
        17:  "t",
        18:  "1",
        19:  "2",
        20:  "3",
        21:  "4",
        22:  "6",
        23:  "5",
        24:  "=",
        25:  "9",
        26:  "7",
        27:  "-",
        28:  "8",
        29:  "0",
        30:  "]",
        31:  "o",
        32:  "u",
        33:  "[",
        34:  "i",
        35:  "p",
        37:  "l",
        38:  "j",
        39:  "'",
        40:  "k",
        41:  ";",
        42:  "\\",
        43:  ",",
        44:  "/",
        45:  "n",
        46:  "m",
        47:  ".",
        50:  "`",
        65:  "[decimal]",
        67:  "[asterisk]",
        69:  "[plus]",
        71:  "[clear]",
        75:  "[divide]",
        76:  "[enter]",
        78:  "[hyphen]",
        81:  "[equals]",
        82:  "0",
        83:  "1",
        84:  "2",
        85:  "3",
        86:  "4",
        87:  "5",
        88:  "6",
        89:  "7",
        91:  "8",
        92:  "9",
        36:  "[return]",
        48:  "[tab]",
        49:  " ",
        51:  "[del]",
        53:  "[esc]",
        54:  "[right-cmd]",
        55:  "[left-cmd]",
        56:  "[left-shift]",
        57:  "[caps]",
        58:  "[left-option]",
        59:  "[left-ctrl]",
        60:  "[right-shift]",
        61:  "[right-option]",
        62:  "[right-ctrl]",
        63:  "[fn]",
        64:  "[f17]",
        72:  "[volup]",
        73:  "[voldown]",
        74:  "[mute]",
        79:  "[f18]",
        80:  "[f19]",
        90:  "[f20]",
        96:  "[f5]",
        97:  "[f6]",
        98:  "[f7]",
        99:  "[f3]",
        100: "[f8]",
        101: "[f9]",
        103: "[f11]",
        105: "[f13]",
        106: "[f16]",
        107: "[f14]",
        109: "[f10]",
        111: "[f12]",
        113: "[f15]",
        114: "[help]",
        115: "[home]",
        116: "[pgup]",
        117: "[fwddel]",
        118: "[f4]",
        119: "[end]",
        120: "[f2]",
        121: "[pgdown]",
        122: "[f1]",
        123: "[left]",
        124: "[right]",
        125: "[down]",
        126: "[up]"
    }
    return a.get(keyCode, "[unknown]");

modflag = {
    "[left-shift]"   : 0b000000100000000000000010,
    "[right-shift]"  : 0b000000100000000000000100,
    "[left-ctrl]"    : 0b000001000000000000000001,
    "[right-ctrl]"   : 0b000001000010000000000000,
    "[left-option]"  : 0b000010000000000000100000,
    "[right-option]" : 0b000010000000000001000000,
    "[left-cmd]"     : 0b000100000000000000001000,
    "[right-cmd]"    : 0b000100000000000000010000
};


# create the transparent window
# Josselin https://stackoverflow.com/a/44296157
# https://stackoverflow.com/questions/19080499/transparent-background-in-a-tkinter-window/44296157#44296157

root = tk.Tk()
# Hide the root window drag bar and close button
root.overrideredirect(True)
# Make the root window always on top
root.wm_attributes("-topmost", True)
# Turn off the window shadow
root.wm_attributes("-transparent", True)
# Set the root window background color to a transparent color
if nobg:
    root.config(bg='systemTransparent')
else: 
    root.config(bg=#aaaaaa)

root.geometry("+300+300")

# Store the PhotoImage to prevent early garbage collection
# root.image0 = tk.PhotoImage(file="z.gif")
root.image = [
    tk.PhotoImage(file="res/00.gif"),
    tk.PhotoImage(file="res/01.gif"),
    tk.PhotoImage(file="res/02.gif")],[
    tk.PhotoImage(file="res/10.gif"),
    tk.PhotoImage(file="res/11.gif"),
    tk.PhotoImage(file="res/12.gif")],[
    tk.PhotoImage(file="res/20.gif"),
    tk.PhotoImage(file="res/21.gif"),
    tk.PhotoImage(file="res/22.gif")];
# Display the image on a label
label = tk.Label(root, image=root.image[0][0])
# Set the label background color to a transparent color
label.config(bg='systemTransparent')
label.pack()


# keyboard area status
l1 = 0
l2 = 0
r1 = 0
r2 = 0
# keyboard area status for display
lstate = 0
rstate = 0

def CGEventCallback(proxy, type, event, refcon):
    global a;
    global label;
    if (type != kCGEventKeyDown and type != kCGEventFlagsChanged and type != kCGEventKeyUp):
        return event;
    keyCode = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode);
    keyname = convertKeyCode(keyCode);
    repeat = CGEventGetIntegerValueField(event, kCGKeyboardEventAutorepeat);
    # whether key is pressed or released
    s = ""
    if (type == kCGEventKeyDown):
        s = "down";
    if (type == kCGEventKeyUp):
        s = "up";
    if type == kCGEventFlagsChanged:
        if (CGEventGetFlags(event) & modflag.get(keyname,0)) == modflag.get(keyname,1):
            s = "down"
        else:
            s = "up"
    # which keyboard area is the key in
    keyarea = 4; # 1/2/3/4, 4 by default
    if keyname in l1keys:
        keyarea = 1
    if keyname in l2keys:
        keyarea = 2
    if keyname in r1keys:
        keyarea = 3
    if keyname in r2keys:
        keyarea = 4
    if keylogger:
        print(keyname, s, "repeat" if repeat else "")
    # current keyboard state
    global l1;
    global l2;
    global r1;
    global r2;
    # ignore overlaying multiple keys in same area, to reduce sticky key caused by key conflict
    newstate = 1 if s=="down" else 0;
    if keyarea == 1:
        l1 = newstate;
    if keyarea == 2:
        l2 = newstate;
    if keyarea == 3:
        r1 = newstate;
    if keyarea == 4:
        r2 = newstate;
    # decide the state to display
    global lstate;
    if l1==0 and l2==0:
        lstate = 0;
    if l1==1 and l2==0 or l1==1 and l2==1 and s=="down" and keyarea==1:
        lstate = 1;
    if l1==0 and l2==1 or l1==1 and l2==1 and s=="down" and keyarea==2:
        lstate = 2;
    global rstate;
    if r1==0 and r2==0:
        rstate = 0;
    if r1==1 and r2==0 or r1==1 and r2==1 and s=="down" and keyarea==3:
        rstate = 1;
    if r1==0 and r2==1 or r1==1 and r2==1 and s=="down" and keyarea==4:
        rstate = 2;
    # update image for display
    label.configure(image=root.image[lstate][rstate]);
    label.pack()
    root.update();
    return event;



# translated from GiacomoLaw/Keylogger
eventMask = (CGEventMaskBit(kCGEventKeyDown) | CGEventMaskBit(kCGEventKeyUp) | CGEventMaskBit(kCGEventFlagsChanged));
eventTap = CGEventTapCreate(kCGSessionEventTap, kCGHeadInsertEventTap, 0, eventMask, CGEventCallback, 0);
if not eventTap:
    print("ERROR: Unable to create event tap.")
    exit(-1)

runLoopSource = CFMachPortCreateRunLoopSource(kCFAllocatorDefault, eventTap, 0);
CFRunLoopAddSource(CFRunLoopGetCurrent(), runLoopSource, kCFRunLoopCommonModes);
CGEventTapEnable(eventTap, True);



root.mainloop()
