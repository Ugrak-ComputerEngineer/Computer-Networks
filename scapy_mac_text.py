from scapy.all import *

file = open("mac.txt", "a+")


#my_macs = [get_if_hwaddr(i) for i in get_if_list()]

#for x in range(len(my_macs)):
#	file.write(my_macs[x]+"\n")


ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.2.0/24"),timeout=2)

for snd,rcv in ans:
	
	file.write(rcv.sprintf(r"%Ether.src% %ARP.psrc%"+"\n"))	
	
        for i in range(len(file)):
        	satir=file.readlines()
                satir.split(" ")
		


ans.summary(lambda (s,r): r.sprintf("%Ether.src% %ARP.psrc%") )

file.close()
