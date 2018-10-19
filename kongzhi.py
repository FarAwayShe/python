import win32gui
import win32con
import win32api
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("陈文兴,i love you ")
Win = win32gui.FindWindow(None, "TIM")
win32gui.ShowWindow(Win, win32con.SW_HIDE)
dict1 = {1: '', 2: '二', 3: '三'}
for i in dict1.values():
	print(i)
win32api.ShellExecute(0, 'open', 'D:/坚果云/Nutstore.exe', ",", 1)
win32api.ShellExecute(0, 'open', 'D:/坚果云/Nutstore.exe', '', '', 0)