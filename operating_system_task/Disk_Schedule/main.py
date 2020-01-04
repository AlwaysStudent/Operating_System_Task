import random
import time
import tkinter as tk
import Disk


class Windows(tk.Tk):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.title('Disk Schedule')
        self.geometry('700x400')

        self.max_disk_size_label = tk.Label(self, text='Max Size', width=20, anchor=tk.NW)
        self.begin_disk_label = tk.Label(self, text='Begin Disk Number', width=20, anchor=tk.NW)
        self.algorithm_label = tk.Label(self, text='Algorithm', width=20, anchor=tk.NW)
        self.algorithm_tips_label = tk.Label(self, text='Tips: Algorithm include FCFS, SSTF, SCAN, CSCAN, NSSCAN',
                                             height=2, anchor=tk.NW)
        self.random_choice_label = tk.Label(self, text='Random Choice Disk Number', anchor=tk.NW)
        self.insert_item_label = tk.Label(self, text='Insert Disk Number', anchor=tk.NW)

        self.max_disk_size_entry = tk.Entry(self, width=20)
        self.max_disk_size_entry.insert('end', '500')
        self.begin_disk_entry = tk.Entry(self, width=20)
        self.begin_disk_entry.insert('end', '200')
        self.algorithm_entry = tk.Entry(self, width=20)
        self.algorithm_entry.insert('end', 'SCAN')
        self.random_choice_entry = tk.Entry(self, width=20)
        self.insert_item_entry = tk.Entry(self, width=20)

        self.setup_button = tk.Button(self, width=10, height=1, text='Set up', command=self.setup_list)
        self.random_choice_button = tk.Button(self, width=11, height=1, text='Random', command=self.random_insert)
        self.insert_item_button = tk.Button(self, width=11, height=1, text='Insert', command=self.insert_item)
        self.run_button = tk.Button(self, width=11, height=1, text='Run', command=self.run)


        self.disk_list_listbox = tk.Listbox(self, font=('consolas', 10),
                                            width=70, height=14)
        self.list_scrollbar = tk.Scrollbar(self.disk_list_listbox, command=self.disk_list_listbox.yview)

        self.disk_list_listbox.config(yscrollcommand=self.list_scrollbar.set)

        self.canvas = tk.Canvas(self, width=240, height=240)
        self.canvas.create_oval(0, 0, 240, 240, fill='gray')

        self.max_disk_size_label.place(x=20, y=20)
        self.max_disk_size_entry.place(x=150, y=20)
        self.begin_disk_label.place(x=20, y=50)
        self.begin_disk_entry.place(x=150, y=50)
        self.algorithm_label.place(x=300, y=20)
        self.algorithm_entry.place(x=420, y=20)
        self.algorithm_tips_label.place(x=300, y=50)
        self.setup_button.place(x=580, y=16)

        self.disk_list_listbox.place(x=20, y=90, relwidth=0.6, relheight=0.5)
        self.list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.random_choice_label.place(x=20, y=310)
        self.random_choice_entry.place(x=200, y=310)
        self.insert_item_label.place(x=20, y=350)
        self.insert_item_entry.place(x=200, y=350)
        self.random_choice_button.place(x=350, y=304)
        self.insert_item_button.place(x=350, y=344)

        self.canvas.place(x=450, y=90)

        self.run_button.place(x=530, y=344)

    def setup_list(self):
        self.begin = int(self.begin_disk_entry.get())
        self.max_size = int(self.max_disk_size_entry.get())
        self.algorithm = self.algorithm_entry.get()
        self.disk_list = Disk.DiskList(self.begin, self.algorithm, self.max_size)
        self.begin_disk_entry['state'] = 'disable'
        self.max_disk_size_entry['state'] = 'disable'
        self.algorithm_entry['state'] = 'disable'
        self.setup_button['state'] = 'disable'

    def random_insert(self):
        number = int(self.random_choice_entry.get())
        self.random_choice_entry.delete(0, 'end')
        temp_disk_list = []
        for _ in range(number):
            temp_disk_list.append(Disk.Disk(random.randint(0, self.disk_list.max_disk)))
        self.disk_list.insert_list(temp_disk_list)
        self.show_in_list()

    def insert_item(self):
        number = int(self.insert_item_entry.get())
        self.insert_item_entry.delete(0, 'end')
        self.disk_list.insert_item(Disk.Disk(number))
        self.show_in_list()

    def show_in_list(self):
        self.disk_list_listbox.delete(0, 'end')
        for i in self.disk_list.begin_list:
            self.disk_list_listbox.insert('end', '{:<6d} : {:>8d}'.format(i.id, i.disk_number))

    def draw_circle(self, t):
        x0 = int(t * 120 / 500)
        y0 = x0
        x1 = 240 - x0
        y1 = x1
        self.canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill='red')
        self.canvas.create_oval(x0, y0, x1, y1, fill='grey')

    def run(self):
        result = self.disk_list.run()
        for i in self.disk_list.route_list:
            for j in self.disk_list.begin_list:
                if i == j.disk_number:
                    self.disk_list.begin_list.remove(j)
                    break
            self.draw_circle(i)
            self.show_in_list()
            time.sleep(1)
            self.update()
            self.canvas.create_oval(0, 0, 240, 240, fill='gray')
        self.disk_list.clear()


def main():
    window = Windows()
    window.mainloop()


if __name__ == '__main__':
    main()
