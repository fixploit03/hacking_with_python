from scapy.all import sniff, IP, TCP

# Fungsi untuk memproses paket yang ditangkap
def packet_callback(packet):
    if IP in packet and TCP in packet:
        ip_src = packet[IP].src
        port_dst = packet[TCP].dport
        print(f"Deteksi paket dari {ip_src} ke port {port_dst}")

# Fungsi utama untuk memulai sniffing
def main():
    print("Mulai menangkap paket...")
    # Menangkap paket TCP
    sniff(filter="tcp", prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
