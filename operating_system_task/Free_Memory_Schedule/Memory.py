class Counter(object):
    count = 1


class MemoryBlock(Counter):
    def __init__(self, length):
        self.pid = Counter.count
        Counter.count += 1
        self.head = None
        self.length = length


class MemoryList(object):
    def __init__(self, length, func=None):
        self.length = length
        self.free_block_list = [[0, length, length - 1]]
        self.busy_block_list = []
        self.pid_list = []
        if func is None:
            self.func = 'best'
        else:
            self.func = func

    def add(self, memory):
        if self.func == 'best':
            self.best_fit(memory)
        elif self.func == 'first':
            self.first_fit(memory)
        elif self.func == 'bad':
            self.bad_fit(memory)
        else:
            return MemoryError

    def remove(self, pid):
        temp = self.busy_block_list[self.pid_list.index(pid)]
        self.busy_block_list.remove(temp)
        self.pid_list.remove(pid)

        self.free_block_list.append([temp[1], temp[2], temp[3]])
        self.free_block_list = sorted(self.free_block_list, key=lambda k: k[0], reverse=False)
        i = 0
        while i != len(self.free_block_list) - 1:
            if (self.free_block_list[i][2] + 1) == self.free_block_list[i + 1][0]:
                temp1 = self.free_block_list[i]
                temp2 = self.free_block_list[i + 1]
                self.free_block_list.append([temp1[0], temp1[1] + temp2[1], temp2[2]])
                self.free_block_list.remove(temp1)
                self.free_block_list.remove(temp2)
                self.free_block_list = sorted(self.free_block_list, key=lambda k: k[0], reverse=False)
                i = 0
            else:
                i += 1

    def best_fit(self, memory_block):
        self.free_block_list = sorted(self.free_block_list, key=lambda block: block[1])
        flag = 0
        for i in self.free_block_list:
            if i[1] >= memory_block.length:
                flag = 1
                self.malloc(i, memory_block)
                break
        if flag != 1:
            print('[info] There is no space...')

    def first_fit(self, memory_block):
        flag = 0
        for i in self.free_block_list:
            if i[1] >= memory_block.length:
                flag = 1
                self.malloc(i, memory_block)
                break
        if flag != 1:
            print('[info] There is no space...')

    def bad_fit(self, memory_block):
        self.free_block_list = sorted(self.free_block_list, key=lambda block: block[1], reverse=True)
        flag = 0
        if self.free_block_list[0][1] >= memory_block.length:
            self.malloc(self.free_block_list[0], memory_block)
            flag = 1
        if flag != 1:
            print('[info] There is no space...')

    def malloc(self, block, memory_block):
        self.busy_block_list.append(
            [memory_block.pid,
             block[0],
             memory_block.length,
             block[0] + memory_block.length - 1]
        )
        self.pid_list.append(memory_block.pid)

        self.free_block_list.remove(block)
        block[0] += memory_block.length
        block[1] -= memory_block.length
        if block[0] != block[2]:
            self.free_block_list.append(block)
        self.free_block_list = sorted(self.free_block_list, key=lambda k: k[0])


def main():
    memory_list = MemoryList(500, 'best')
    x = MemoryBlock(100)
    y = MemoryBlock(200)
    memory_list.add(x)
    memory_list.add(y)
    memory_list.remove(x.pid)
    # print(memory_list.free_block_list)
    # print(memory_list.busy_block_list)
    memory_list.remove(y.pid)
    # print(memory_list.free_block_list)
    # print(memory_list.busy_block_list)


if __name__ == '__main__':
    main()
