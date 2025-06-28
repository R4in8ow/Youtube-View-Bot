import os
import time
import subprocess
import sys
from getpass import getpass

OVPN_DIR = 'ovpns'
WAIT_TIME = 120  # seconds

def connect_vpn(ovpn_file, username, password):
    print(f"\nStarting OpenVPN with config: {ovpn_file}")
    with open("vpn_auth.txt", "w") as f:
        f.write(f"{username}\n{password}\n")
    return subprocess.Popen([
        "sudo", "openvpn", "--config", ovpn_file, "--auth-user-pass", "vpn_auth.txt"
    ])

def disconnect_vpn(vpn_process):
    vpn_process.terminate()
    vpn_process.wait()
    print("VPN disconnected.")

def open_youtube(youtube_url):
    print("Launching Firefox...")
    subprocess.Popen(["firefox", "--new-window", youtube_url])

def close_firefox():
    subprocess.call(["pkill", "firefox"])
    print("Firefox closed.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <YouTube_URL>")
        sys.exit(1)

    youtube_url = sys.argv[1]
    username = input("Enter VPN username: ")
    password = getpass("Enter VPN password: ")

    ovpn_files = sorted(f for f in os.listdir(OVPN_DIR) if f.endswith(".ovpn"))
    print(f"\nFound {len(ovpn_files)} VPN config files.")

    for idx, ovpn in enumerate(ovpn_files, 1):
        print(f"\n[{idx}/{len(ovpn_files)}] Using VPN config: {ovpn}")
        vpn_process = connect_vpn(os.path.join(OVPN_DIR, ovpn), username, password)
        print("Waiting 15 seconds for VPN to stabilize...")
        time.sleep(15)

        open_youtube(youtube_url)
        print(f"Waiting {WAIT_TIME} seconds...")
        time.sleep(WAIT_TIME)

        close_firefox()
        disconnect_vpn(vpn_process)

    print("\n✅ Done with all VPNs.")

if __name__ == "__main__":
    main()
