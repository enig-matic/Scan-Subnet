import sys
from scapy.all import IP,ICMP,sr1
from netaddr import IPNetwork
import pyfiglet

name = "JANGOTRA"
print ("=" * 60)

ban = pyfiglet.figlet_format(
    name,
    font="slant"
)

print("\033[96m" + ban + "\033[0m")
print("=" * 60)
print("       Block IP Addresees")
print("=" * 60)
print("Date : 27/10/2026\n")

def check_host(network, netmask):

    live_host = []
    total_host = 0
    scan_host = 0 

    ip_network  = IPNetwork( network + '/' + netmask)

    for host in ip_network.iter_hosts():
        total_host += 1

    for host in ip_network.iter_hosts():
        scan_host += 1
        print(f"Scanning {scan_host}/{total_host}")
        response = sr1(
            IP(dst=str(host))/ICMP(),
            verbose =0,
            timeout=1
        )

        if response is not None and response.haslayer(ICMP):
            icmp = response.getlayer(ICMP)
            if icmp.type == 0:
                live_host.append(host)
    return live_host

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            f"Usuage: sudo python3 {sys.argv[0]} "
            "<network> <netmask>"
        )
        sys.exit(1)

    network = sys.argv[1]
    netmask = sys.argv[2]

    live_host = check_host(network, netmask)

    for index,host in enumerate(live_host,start=1):
        print(f"Online Host{index} = {host}")