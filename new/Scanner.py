import nmap 
from threading import Thread, RLock


verrou = RLock()
DOM_NUM = 168
DOM_MID = DOM_NUM/2
DOM_IN = 'googleScrap.txt'
dom_list = list()

with open(DOM_IN, 'r') as fd :
    for domain in fd :
        dom_list.append(domain)

dom_concat1 = ''.join(dom_list[1:DOM_MID])
dom_concat2 = ''.join(dom_list[DOM_MID:DOM_NUM])
print(dom_concat1)
print("[+] Debut du scan...")

class Scannmap(Thread):
    def __init__(self, domains_concat):
        Thread.__init__(self)
        self.domains_concat = domains_concat

    def run(self):
        nm = nmap.PortScanner()
        res = nm.scan(hosts=self.domains_concat, arguments='-T4 -F')
        with verrou : 
            ff = open('outputScan.txt', 'w+') 
            ff.write(nm.csv())
            ff.close()

thread_1 = Scannmap(dom_concat1)
thread_2 = Scannmap(dom_concat2)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

