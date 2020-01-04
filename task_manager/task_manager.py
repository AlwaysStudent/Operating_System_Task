import os
import subprocess
import psutil
import signal
import time
import tkinter as tk
import tkinter.simpledialog


def percent(number):
	string = str(round(number, 4)) + '%'
	return string


def change_name(name):
	if len(name) < 18:
		return name.ljust(20)
	else:
		name = name[:17] + '...'
		return name


def process_state(process_id):
	process = psutil.Process(process_id)
	process_information = [
		str(process_id),
		change_name(process.name()),
		percent(process.cpu_percent()),
		percent(process.memory_percent()),
		time.asctime(time.localtime(process.create_time()))
	]
	temp_str = '{:<12}{:<20}{:<14}{:<16}{:<20}'.format(
		process_information[0],
		process_information[1],
		process_information[2],
		process_information[3],
		process_information[4]
	)
	return temp_str


def get_information():
	process_id_list = psutil.pids()
	result = []
	for i in process_id_list:
		try:
			result.append(process_state(i))
		except:
			pass
	return result


class Windows(tk.Tk):
	def __init__(self):
		super().__init__()
		self.setup_ui()
		self.information = get_information()

	def setup_ui(self):
		self.title('Task Manager')
		self.geometry('600x600')

		self.task_list_label = tk.Label(self, text='Task List', width=20, font=('consolas', 16), anchor=tk.CENTER)

		self.process_list_listbox = tk.Listbox(self, font=('consolas', 12), width=90, height=30)
		self.process_list_listbox.insert('end', '{:<12}{:<20}{:<14}{:<16}{:<20}'.format
		('Process ID', 'Process Name', 'CPU Percent', 'Memory Percent', 'Create Time'))
		self.list_scrollbar = tk.Scrollbar(self.process_list_listbox, command=self.process_list_listbox.yview)

		self.create_new_button = tk.Button(self, text='Create New Task', width=18, command=self.create_new_task)
		self.shut_down_button = tk.Button(self, text='Shut Down Task', width=18, command=self.shut_down_task)
		self.refresh_button = tk.Button(self, text='Refresh', width=18, command=self.refresh)

		self.task_list_label.place(x=250, y=20)
		self.process_list_listbox.place(x=30, y=60, relwidth=0.9, relheight=0.75)
		self.list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

		self.create_new_button.place(x=260, y=540)
		self.shut_down_button.place(x=430, y=540)
		self.refresh_button.place(x=90, y=540)

		self.refresh()

	def create_new_task(self):
		command = tkinter.simpledialog.askstring('Create New Task', 'Please input the Task or Command')
		subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		time.sleep(1)
		self.update()
		self.refresh()

	def shut_down_task(self):
		shut_index = self.process_list_listbox.curselection()[0]
		shut_pid = self.information[shut_index - 1][:12]
		if os.name == 'nt':
			os.popen('taskkill.exe /pid' + str(int(pid)))
		elif os.name == 'posix':
			os.kill(int(shut_pid), signal.SIGKILL)
		time.sleep(1)
		self.update()
		self.refresh()

	def refresh(self):
		self.information = get_information()
		self.process_list_listbox.delete(1, 'end')
		for i in self.information:
			self.process_list_listbox.insert('end', i)


def main():
	window = Windows()
	window.mainloop()


if __name__ == '__main__':
	main()
