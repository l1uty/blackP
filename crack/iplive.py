from collections import defaultdict
import ipaddress
import prettytable
import sys

def get_c_network(ip):
    network = ipaddress.ip_network(ip)
    network = ipaddress.ip_network(f"{network.network_address}/24", strict=False)
    return str(network)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 ip.py <file>")
        return

    filename = sys.argv[1]

    ip_dict = defaultdict(set)

    with open(filename, "r") as file:
        for line in file:
            ip = line.strip()
            c_network = get_c_network(ip)
            ip_dict[c_network].add(ip)

    sorted_ip_dict = dict(sorted(ip_dict.items(), key=lambda item: len(item[1]), reverse=True))

    table = prettytable.PrettyTable(['IP段', 'IP数量'])
    table.align = 'l'
    table.align['IP数量'] = 'r'
    for k, v in sorted_ip_dict.items():
        ip_count = len(v)
        row_color = lambda text: f"\033[91m{text}\033[0m" if ip_count >= 5 else text
        table.add_row([row_color(k), row_color(ip_count)])

    print(table)

if __name__ == "__main__":
    main()