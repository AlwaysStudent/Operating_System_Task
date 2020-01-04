import random


class Counter(object):
    count = 0


class Disk(Counter):
    def __init__(self, disk_number):
        self.disk_number = disk_number
        self.id = Counter.count
        Counter.count += 1


class DiskList(object):
    def __init__(self, begin=0, algorithm='SCAN', max_disk=500):
        self.disk_list = []
        self.begin = begin
        self.algorithm = algorithm
        self.route_list = [self.begin]
        self.begin_list = []
        self.max_disk = max_disk

    def set_begin(self, begin):
        self.begin = begin

    def insert_list(self, disks):
        for i in disks:
            if i.disk_number > self.max_disk:
                return 0
        self.disk_list.extend(disks)
        self.begin_list.extend(disks)
        return 1

    def insert_item(self, disk):
        if disk.disk_number > self.max_disk:
            return 0
        self.disk_list.append(disk)
        self.begin_list.extend(disk)
        return 1

    def clear(self):
        self.disk_list = []
        self.begin_list = []
        self.route_list = [self.begin]

    def run(self):
        result = []
        if self.algorithm == 'FCFS':
            result = self.first_come_first_serving()
        elif self.algorithm == 'SSTF':
            result = self.shortest_seek_time_first()
        elif self.algorithm == 'SCAN':
            result = self.scan()
        elif self.algorithm == 'CSCAN':
            result = self.circular_scan()
        elif self.algorithm == 'NSSCAN':
            result = self.n_step_scan()
        else:
            print('[info] Wrong Algorithm...')
            exit(0)
        return result

    def first_come_first_serving(self):
        result = []
        for _ in range(len(self.disk_list)):
            temp = self.disk_list[0]
            result.append(abs(self.begin - temp.disk_number))
            self.begin = temp.disk_number
            self.route_list.append(self.begin)
            self.disk_list.remove(temp)
        return result

    def shortest_seek_time_first(self):
        result = []
        for _ in range(len(self.disk_list)):
            self.disk_list.sort(key=lambda disk: disk.disk_number)
            for i in range(len(self.disk_list)):
                if i < len(self.disk_list) - 1:
                    if self.begin < self.disk_list[i].disk_number:
                        if abs(self.begin - self.disk_list[i].disk_number) > \
                                abs(self.begin - self.disk_list[i - 1].disk_number):
                            result.append(abs(self.begin - self.disk_list[i - 1].disk_number))
                            self.begin = self.disk_list[i - 1].disk_number
                            self.route_list.append(self.begin)
                            self.disk_list.remove(self.disk_list[i - 1])
                            break
                        else:
                            result.append(abs(self.begin - self.disk_list[i].disk_number))
                            self.begin = self.disk_list[i].disk_number
                            self.route_list.append(self.begin)
                            self.disk_list.remove(self.disk_list[i])
                            break
                else:
                    result.append(abs(self.begin - self.disk_list[i].disk_number))
                    self.begin = self.disk_list[i].disk_number
                    self.route_list.append(self.begin)
                    self.disk_list.remove(self.disk_list[i])
                    break
        return result

    def scan(self):
        result = []
        count = 0
        for i in range(len(self.disk_list)):
            if self.disk_list[i].disk_number < self.begin:
                count += 1
        if count > len(self.disk_list) // 2:
            flag = 0
        else:
            flag = 1

        if flag == 0:
            for _ in range(count):
                self.disk_list.sort(key=lambda disk: disk.disk_number, reverse=True)
                for i in range(len(self.disk_list)):
                    if self.begin >= self.disk_list[i].disk_number:
                        result.append(abs(self.begin - self.disk_list[i].disk_number))
                        self.begin = self.disk_list[i].disk_number
                        self.route_list.append(self.begin)
                        self.disk_list.remove(self.disk_list[i])
                        break

            for _ in range(len(self.disk_list) - count):
                self.disk_list.sort(key=lambda disk: disk.disk_number, reverse=True)
                result.append(abs(self.begin - self.disk_list[len(self.disk_list) - 1].disk_number))
                self.begin = self.disk_list[len(self.disk_list) - 1].disk_number
                self.route_list.append(self.begin)
                self.disk_list.remove(self.disk_list[len(self.disk_list) - 1])

        elif flag == 1:
            for _ in range(len(self.disk_list) - count):
                self.disk_list.sort(key=lambda disk: disk.disk_number)
                for i in range(len(self.disk_list)):
                    if self.begin <= self.disk_list[i].disk_number:
                        result.append(abs(self.begin - self.disk_list[i].disk_number))
                        self.begin = self.disk_list[i].disk_number
                        self.route_list.append(self.begin)
                        self.disk_list.remove(self.disk_list[i])
                        break

            for _ in range(count):
                self.disk_list.sort(key=lambda disk: disk.disk_number)
                result.append(abs(self.begin - self.disk_list[len(self.disk_list) - 1].disk_number))
                self.begin = self.disk_list[len(self.disk_list) - 1].disk_number
                self.route_list.append(self.begin)
                self.disk_list.remove(self.disk_list[len(self.disk_list) - 1])

        return result

    def circular_scan(self):
        result = []
        count = 0
        for i in range(len(self.disk_list)):
            if self.disk_list[i].disk_number < self.begin:
                count += 1
        if count > len(self.disk_list) // 2:
            flag = 0
        else:
            flag = 1

        if flag == 0:
            for _ in range(count):
                self.disk_list.sort(key=lambda disk: disk.disk_number, reverse=True)
                for i in range(len(self.disk_list)):
                    if self.begin >= self.disk_list[i].disk_number:
                        result.append(abs(self.begin - self.disk_list[i].disk_number))
                        self.begin = self.disk_list[i].disk_number
                        self.route_list.append(self.begin)
                        self.disk_list.remove(self.disk_list[i])
                        break

            for _ in range(len(self.disk_list) - count):
                self.disk_list.sort(key=lambda disk: disk.disk_number, reverse=True)
                result.append(abs(self.begin - self.disk_list[0].disk_number))
                self.begin = self.disk_list[0].disk_number
                self.route_list.append(self.begin)
                self.disk_list.remove(self.disk_list[0])

        elif flag == 1:
            for _ in range(len(self.disk_list) - count):
                self.disk_list.sort(key=lambda disk: disk.disk_number)
                for i in range(len(self.disk_list)):
                    if self.begin <= self.disk_list[i].disk_number:
                        result.append(abs(self.begin - self.disk_list[i].disk_number))
                        self.begin = self.disk_list[i].disk_number
                        self.route_list.append(self.begin)
                        self.disk_list.remove(self.disk_list[i])
                        break

            for _ in range(count):
                self.disk_list.sort(key=lambda disk: disk.disk_number)
                result.append(abs(self.begin - self.disk_list[0].disk_number))
                self.begin = self.disk_list[0].disk_number
                self.route_list.append(self.begin)
                self.disk_list.remove(self.disk_list[0])

        return result

    def n_step_scan(self):
        result_all = []
        temp_list = []

        for i in range(len(self.disk_list)):
            if i % 8 == 0:
                temp_list.append(self.disk_list[i:i + 8])

        for each in temp_list:
            result = []
            count = 0
            for i in range(len(each)):
                if each[i].disk_number < self.begin:
                    count += 1
            if count > len(each) // 2:
                flag = 0
            else:
                flag = 1

            if flag == 0:
                for _ in range(count):
                    each.sort(key=lambda disk: disk.disk_number, reverse=True)
                    for i in range(len(each)):
                        if self.begin >= each[i].disk_number:
                            result.append(abs(self.begin - each[i].disk_number))
                            self.begin = each[i].disk_number
                            self.route_list.append(self.begin)
                            each.remove(each[i])
                            break

                for _ in range(len(each) - count):
                    each.sort(key=lambda disk: disk.disk_number, reverse=True)
                    result.append(abs(self.begin - each[len(each) - 1].disk_number))
                    self.begin = each[len(each) - 1].disk_number
                    self.route_list.append(self.begin)
                    each.remove(each[len(each) - 1])

            elif flag == 1:
                for _ in range(len(each) - count):
                    each.sort(key=lambda disk: disk.disk_number)
                    for i in range(len(each)):
                        if self.begin <= each[i].disk_number:
                            result.append(abs(self.begin - each[i].disk_number))
                            self.begin = each[i].disk_number
                            self.route_list.append(self.begin)
                            each.remove(each[i])
                            break

                for _ in range(count):
                    each.sort(key=lambda disk: disk.disk_number)
                    result.append(abs(self.begin - each[len(each) - 1].disk_number))
                    self.begin = each[len(each) - 1].disk_number
                    self.route_list.append(self.begin)
                    each.remove(each[len(each) - 1])
            result_all.extend(result)

        return result_all


def main():
    x = []
    for i in range(20):
        x.append(Disk(random.randint(0, 300)))
    for i in x:
        print(i.disk_number, end=' ')
    print()
    y = sorted(x, key=lambda disk: disk.disk_number)
    for i in y:
        print(i.disk_number, end=' ')
    print()
    disk_list = DiskList(begin=100, algorithm='NSSCAN')
    disk_list.insert_list(x)
    result = disk_list.run()
    print(result)
    print(disk_list.route_list)


if __name__ == '__main__':
    main()


