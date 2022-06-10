import psutil as pt
# from time import sleep

class CpuBar:

    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)
        self.cpu_count_logical = pt.cpu_count()

    def cpu_percent_return(self):
        return pt.cpu_percent(percpu=True)

    def mem_percent_return(self):
        return pt.virtual_memory()

    def cpu_one_return(self):
        return pt.cpu_percent()



# x = CpuBar()
#
#
# print(x.mem_percent_return())

