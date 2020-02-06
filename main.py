# run with python3
from ApplicationServices import *
import tkinter as tk


# here defines left-hand keys
# note that X isn't here
leftkeys = set('54321`trewqgfdsabvcz ');
leftkeys.add("[tab]");
leftkeys.add("[esc]");
leftkeys.add("[left-cmd]");
leftkeys.add("[left-ctrl]");
leftkeys.add("[left-shift]");
leftkeys.add("[left-option]");
leftkeys.add("[f1]");
leftkeys.add("[f2]");
leftkeys.add("[f3]");
leftkeys.add("[f4]");
leftkeys.add("[f5]");
# all other keys are deemed right-hand keys


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
        41:  ",",
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
root.config(bg='systemTransparent')

root.geometry("+300+300")

# Store the PhotoImage to prevent early garbage collection
# root.image0 = tk.PhotoImage(file="z.gif")
root.image00 = tk.PhotoImage(file="res/00.gif")
root.image01 = tk.PhotoImage(file="res/01.gif")
root.image02 = tk.PhotoImage(file="res/02.gif")
root.image10 = tk.PhotoImage(file="res/10.gif")
root.image11 = tk.PhotoImage(file="res/11.gif")
root.image12 = tk.PhotoImage(file="res/12.gif")
root.image20 = tk.PhotoImage(file="res/20.gif")
root.image21 = tk.PhotoImage(file="res/21.gif")
root.image22 = tk.PhotoImage(file="res/22.gif")
# Display the image on a label
label = tk.Label(root, image=root.image00)
# Set the label background color to a transparent color
label.config(bg='systemTransparent')
label.pack()


# keyboard area status
l = 0
r = 0

def CGEventCallback(proxy, type, event, refcon):
    global a;
    global label;
    if (type != kCGEventKeyDown and type != kCGEventFlagsChanged and type != kCGEventKeyUp):
        return event;
    keyCode = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode);
    keyname = convertKeyCode(keyCode);
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

    # calculate current keyboard state
    global l;
    global r;
    # simply ignoring modifiers and ignore overlaying multiple keys
    if (keyname in leftkeys):
        l = 0 if s=="up" else 1;
    else:
        r = 0 if s=="up" else 1;

    # label.configure(image=root.image0)
    # print(convertKeyCode(keyCode), s)
    # update image
    # label.pack_forget();
    # label.configure(image=root.image0);
    # label.pack()
    if l==0 and r==0:
    	label.configure(image=root.image00);
    if l==1 and r==0:
        label.configure(image=root.image20);
    if l==0 and r==1:
        label.configure(image=root.image01);
    if l==1 and r==1:
        label.configure(image=root.image21);
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
