import Memory
import tkinter as tk


class Windows(tk.Tk):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.memory_list = None

    def setup_ui(self):
        self.title('Memory Schedule')
        self.geometry('600x400')
        self.max_memory_label = tk.Label(self, text='Max Memory', width=12)
        self.algorithm_label = tk.Label(self, text='Algorithm', width=12)
        self.algorithm_label_tips = tk.Label(self, text='tips: best, bad and first', width=30)

        self.max_memory_entry = tk.Entry(self, width=16)
        self.algorithm_entry = tk.Entry(self, width=16, text='best')

        self.setup_button = tk.Button(self, text='Set Up', state='normal', width=20, command=self.setup_list)

        self.memory_list_box = tk.Listbox(self, width=65, height=14)

        self.memory_canvas = tk.Canvas(self, bg='green', width=100, height=350)

        self.max_memory_label.place(x=10, y=20)
        self.max_memory_entry.place(x=120, y=20)

        self.algorithm_label.place(x=10, y=60)
        self.algorithm_entry.place(x=120, y=60)
        self.algorithm_label_tips.place(x=240, y=60)

        self.setup_button.place(x=260, y=18)

        self.memory_list_box.place(x=14, y=95)

        self.memory_canvas.place(x=450, y=20)


    def setup_list(self):
        length = int(self.max_memory_entry.get())
        algorithm = self.algorithm_entry.get()
        self.memory_list = Memory.MemoryList(length, func=algorithm)
        self.setup_button['state'] = 'disable'
        self.max_memory_entry['state'] = 'disable'
        self.algorithm_entry['state'] = 'disable'



def main():
    window = Windows()
    window.mainloop()
    # memory_list = Memory.MemoryList(500, 'bad')
    # x = Memory.MemoryBlock(100)
    # y = Memory.MemoryBlock(200)
    # z = Memory.MemoryBlock(150)
    # j = Memory.MemoryBlock(50)
    # k = Memory.MemoryBlock(125)
    # memory_list.add(x)
    # print(memory_list.free_block_list)
    # print(memory_list.busy_block_list)
    # print('---------------------------------------------------')
    # memory_list.add(y)
    # print(memory_list.free_block_list)
    # print(memory_list.busy_block_list)
    # print('---------------------------------------------------')
    # memory_list.add(z)
    # print(memory_list.free_block_list)
    # print(memory_list.busy_block_list)
    # print('---------------------------------------------------')
    # memory_list.add(j)
    # print(memory_list.free_block_list)
    # print(memory_list.busy_block_list)
    # print('---------------------------------------------------')
    # memory_list.remove(x.pid)
    # print(memory_list.free_block_list)
    # print(memory_list.busy_block_list)
    # print('---------------------------------------------------')
    # memory_list.remove(z.pid)
    # print(memory_list.free_block_list)
    # print(memory_list.busy_block_list)
    # print('---------------------------------------------------')
    # memory_list.add(k)
    # print(memory_list.free_block_list)
    # print(memory_list.busy_block_list)
    # print('---------------------------------------------------')
    # memory_list.remove(y.pid)
    # print(memory_list.free_block_list)
    # print(memory_list.busy_block_list)
    # print('---------------------------------------------------')
    # memory_list.remove(j.pid)
    # print(memory_list.free_block_list)
    # print(memory_list.busy_block_list)
    # print('---------------------------------------------------')
    # memory_list.remove(k.pid)
    # print(memory_list.free_block_list)
    # print(memory_list.busy_block_list)
    # print('---------------------------------------------------')


if __name__ == '__main__':
    main()
