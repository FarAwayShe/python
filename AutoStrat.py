# import os
import time
import win32com.client
import win32con
import win32gui
import _thread
import win32api
# import traceback
time.sleep(10)
dict1 = {
		"D:/坚果云/Nutstore.exe": '坚果云',
		"C:/Users/ChloeChow/Desktop/ahk.exe": 'autohotkey',
		"C:/Users/ChloeChow/AppData/Local/Wox/Wox.exe": 'Wox',
		"C:/Users/ChloeChow/AppData/Local/FluxSoftware/Flux/flux.exe": 'flux',
		# "D:/TIM/Bin/QQScLauncher.exe": 'TIM',
		"C:/Program Files/WindowsApps/45479liulios.17062D84F7C46_2.0.1.0_x64__p7pnf6hceqser/Snipaste.exe": 'Snipaste',
		"C:/Program Files/Everything/Everything.exe": 'Everything'
		}


def strat(path, name):
	win32api.ShellExecute(0, 'open', path, '', '', 0)
	speaker = win32com.client.Dispatch("SAPI.SpVoice")
	speaker.Speak("启动")
	time.sleep(0.1)
	speaker.Speak(name)
	if dict1[i] == '坚果云':
		time.sleep(3)
		Win = win32gui.FindWindow(None, '坚果云')
		win32gui.ShowWindow(Win, win32con.SW_HIDE)
try:
	for i in dict1.keys():
		_thread.start_new_thread(strat, (i, dict1[i]))
		# print('已启动{}'.format(dict1[i]))
		time.sleep(5)
except Exception as e:
	print(e)
