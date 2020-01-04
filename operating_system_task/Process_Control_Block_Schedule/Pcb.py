class Counter(object):
    count = 0


class ProcessPCB(Counter):
    def __init__(self, priority, service_time):
        Counter.count += 1
        self.pid = Counter.count
        self.priority = priority
        self.service_time = service_time

    def set_priority(self, _priority):
        self.priority = _priority

    def set_service_time(self, _service_time):
        self.service_time = _service_time

    def run(self):
        self.service_time -= 1
        self.priority -= 1


class ProcessPCBList(object):
    def __init__(self):
        self.pcb_list = []
        self.count = 0

    def sort(self):
        self.pcb_list = sorted(self.pcb_list, key=lambda pcb: pcb[0].priority, reverse=True)
        for i in range(len(self.pcb_list) - 1):
            if self.pcb_list[i][0].priority == self.pcb_list[i + 1][0].priority:
                if self.pcb_list[i][1] < self.pcb_list[i + 1][1]:
                    temp = self.pcb_list[i]
                    self.pcb_list[i] = self.pcb_list[i + 1]
                    self.pcb_list[i + 1] = temp

    def put(self, pcb):
        self.pcb_list.append([pcb, self.count])
        self.count += 1
        self.sort()

    def get(self):
        result = self.pcb_list[0]
        self.pcb_list.remove(result)
        self.sort()
        return result[0]

    def empty(self):
        if len(self.pcb_list) > 0:
            return False
        return True


def dynamic_priority(pcb_list):
    while pcb_list.empty() is False:
        temp_pcb = pcb_list.get()
        print('---------------------------------------------------------------------')
        print('running:')
        print("PID: %d  Priority: %d Service_time: %d" % (temp_pcb.pid, temp_pcb.priority, temp_pcb.service_time))
        print('others:')
        for i in pcb_list.pcb_list:
            print("PID: %d  Priority: %d Service_time: %d counter: %d" %
                  (i[0].pid, i[0].priority, i[0].service_time, i[1]))
        print('---------------------------------------------------------------------')
        temp_pcb.run()
        if temp_pcb.service_time != 0:
            pcb_list.put(temp_pcb)


def main():
    a = ProcessPCB(4, 9)
    b = ProcessPCB(3, 8)
    c = ProcessPCB(2, 6)
    d = ProcessPCB(1, 7)
    pcb_list = ProcessPCBList()
    pcb_list.put(a)
    pcb_list.put(b)
    pcb_list.put(c)
    pcb_list.put(d)
    dynamic_priority(pcb_list)


if __name__ == '__main__':
    main()
