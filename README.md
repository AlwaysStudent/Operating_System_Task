# Operating System Task

---

> Use Python language to finish the task
> The GUI is writen by using Tkinter (A basic GUI package)

## 1.Process Control Block Schedule

1. In the folder, the file `Pcb.py` includes the base `Process Control Block` class called `ProcessPCB`, the `queue of Process Control Block` class called `ProcessPCBList` and a `counter` to count the number of the `ProcessPCB`.
2. In the floder, the file `main.py` includes the basic GUI.
3. This file is made for someone just want to use it but no want to see the source code.

### How to use it

1. Copy the file `PCB.py` to your `workpath` and ensure you have python to run it.
2. Just use it.

First, you should use `import PCB` to load the module to you python file.

```python
import PCB
```

Second, you should use `PCB.ProcessPCB(priority, service_time)` to create a `PCB.ProcessPCB` object.

```python
PCB.processPCB(priority, service_time)
'''
:param priority int: describe the priority of this process.
:param service_time int: describe this process will use CPU how many seconds.
'''

    def set_priority(priority)
    '''
    reset the priority
    '''

    def set_service_time(service_time)
    '''
    reset the service_time
    '''

    def run()
    '''
    this PCB use CPU, so make its priority and service_time less
    '''
```

```python
a = PCB.ProcessPCB(4, 9)
```

You also can use `PCB.ProcessPCBList()` to create a `PCB.ProcessPCBList` object.

(The `PCB.ProcessPCBList()` don't have any parameter)

```python
pcb_list = PCB.ProcessPCBList()
```

