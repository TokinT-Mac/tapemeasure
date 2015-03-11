import time
import threading

class Watchdog(threading.Thread):
    def __init__(self):
        self.stats = []
        super(Watchdog, self).__init__()
        self.daemon = True
        self.interval = 1

    def setInterval(self, interval):
        self.interval = interval

    def run(self):
        while True:
            cpu = loadCpu()
            mem = loadMem()
            measure = {"cpu":cpu, "memory":mem, "time": time.time()}
            self.stats.append(measure)
            if len(self.stats)>10:
                self.stats.pop(0)
            time.sleep(self.interval)

    def getData(self):
        y = {}
        z = 0
        for x in self.stats:
            y[z]=x
            z = z+1
        return y
def loadCpu():
    with file('/proc/stat', 'r') as stats:
        cpus = {}
        for line in stats:
            if line[:3] == 'cpu':
                l = line.split(" ")
                if "" in l:
                    l.remove("")
 
                cpus[l[0]] = l[1:4]
    return cpus 
    
def loadMem():
    filter = ['MemTotal', 'MemFree', 'MemAvailable', 'SwapTotal', 'SwapFree']
    meminfo = {}
    with file('/proc/meminfo', 'r') as stats:
        for entry in stats:
            label = entry[:entry.find(':')]
            data = entry[entry.find(':'):].strip()
            #print label, data
            if label in filter:
                meminfo[label] = data
    return meminfo

watchd = Watchdog()
watchd.start()

def getData():
    return watchd.getData()
