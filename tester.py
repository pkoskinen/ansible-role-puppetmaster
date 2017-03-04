from scapy.all import *

SRC_NTP = '10.100.100.11'
DEST_NTP = '10.100.100.10'
DPORT_NTP = 123
DEST_REAL = '192.168.10.12'

print "---\nExpected result: Fail, port 666/udp, source 10.100.100.11, dest 10.100.100.10\n---\n"
ans,unans = sr(IP(src=SRC_NTP, dst=DEST_NTP) / UDP(dport=[666]), timeout=1, retry=0, multi=0)
ans.summary()

print "---\nExpected result: Fail, port 123/tcp, source 10.100.100.11, dest 10.100.100.10\n---\n"
ans,unans = sr(IP(src=SRC_NTP, dst=DEST_NTP) / TCP(dport=[DPORT_NTP]), timeout=1, retry=0, multi=0)
ans.summary()

print "---\nExpected result: Success, port 123/udp, source 10.100.100.11, dest 10.100.100.11\n---\n"
ans,unans = sr(IP(src=SRC_NTP, dst=DEST_NTP) / UDP(dport=[DPORT_NTP]), timeout=1, retry=0, multi=0)
ans.summary()

print "---\nExpected result: Success, ports 22/tcp, 443/tcp, 80/tcp, 8080/tcp, source 192.168.10.10, dest 192.168.10.12\n---\n"
ans,unans = sr(IP(dst=DEST_REAL) / TCP(dport=[22,443,80,8080]), timeout=1, retry=0, multi=0)
ans.summary()

print "---\nExpected result: Fail, port 8080/tcp, source 10.100.100.11, dest 10.100.100.10\n---\n"
ans,unans = sr(IP(src=SRC_NTP, dst=DEST_NTP) / TCP(dport=[8080]), timeout=1, retry=0, multi=0)
ans.summary()

print "---\nExpected result: Success, port 8080/tcp, source 192.168.10.10, dest 10.100.100.10\n---\n"
ans,unans = sr(IP(dst=DEST_NTP) / TCP(dport=[8080]), timeout=1, retry=0, multi=0)
ans.summary()

print "---\nExpected result: Success, port 22/tcp, source 10.100.100.11, dest 10.100.100.10\n---\n"
ans,unans = sr(IP(src=SRC_NTP, dst=DEST_REAL) / TCP(dport=[22]), timeout=1, retry=0, multi=0)
ans.summary()

