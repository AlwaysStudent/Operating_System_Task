import time
import tkinter as tk

import Pcb


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pcb_list = Pcb.ProcessPCBList()
        self.setup_ui()

    def setup_ui(self):
        self.title('Process Scheduling')
        self.geometry('600x400')

        self.label_now_running = tk.Label(self, text='Now Running PCB')
        self.label_others = tk.Label(self, text='Other PCBs')
        self.priority_label = tk.Label(self, text='Priority')
        self.service_time_label = tk.Label(self, text='Service Time')

        self.value1 = tk.StringVar()
        self.now_label = tk.Label(self, bg='green', textvariable=self.value1, width=46)

        self.priority_entry = tk.Entry(self, width=46)
        self.service_time_entry = tk.Entry(self, width=46)

        self.value2 = tk.StringVar()
        self.other_list_box = tk.Listbox(self, height=7, width=46)

        self.add_button = tk.Button(self, text='Add', command=self.add)
        self.run_button = tk.Button(self, text='Run', command=self.run)

        self.label_now_running.place(x=30, y=30)
        self.label_others.place(x=30, y=80)
        self.now_label.place(x=150, y=30)
        self.priority_label.place(x=30, y=240)
        self.service_time_label.place(x=30, y=280)

        self.priority_entry.place(x=150, y=240)
        self.service_time_entry.place(x=150, y=280)

        self.other_list_box.place(x=150, y=80)

        self.add_button.place(x=510, y=275)
        self.run_button.place(x=510, y=75)

    def add(self):
        v1 = int(self.priority_entry.get())
        v2 = int(self.service_time_entry.get())
        temp_pcb = Pcb.ProcessPCB(v1, v2)
        self.pcb_list.put(temp_pcb)
        pcb_string = 'PID: {:<10} Priority: {:<10} Service Time: {:<10}'\
            .format(temp_pcb.pid, temp_pcb.priority, temp_pcb.service_time)
        self.other_list_box.insert('end', pcb_string)

    def run(self):
        self.dynamic_priority()

    def dynamic_priority(self):
        while self.pcb_list.empty() is False:
            time.sleep(1)
            self.update()
            temp_pcb = self.pcb_list.get()
            self.value1.set('PID: {:<10} Priority: {:<10} Service Time: {:<10}'
                            .format(temp_pcb.pid, temp_pcb.priority, temp_pcb.service_time))
            self.other_list_box.delete(0, last=len(self.pcb_list.pcb_list))
            for each in self.pcb_list.pcb_list:
                self.other_list_box.insert('end', 'PID: {:<10} Priority: {:<10} Service Time: {:<10}'
                                           .format(each[0].pid, each[0].priority, each[0].service_time))
            temp_pcb.run()
            if temp_pcb.service_time != 0:
                self.pcb_list.put(temp_pcb)


def main():
    windows = Window()
    windows.mainloop()


if __name__ == '__main__':
    main()
