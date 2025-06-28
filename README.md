# 🔁 YouTube Viewer via Rotating VPN

This Python tool opens a specified YouTube video multiple times using different VPN connections through OpenVPN. It helps simulate views (for educational/testing purposes only).

## 🚀 Features

- Loop through `.ovpn` files to rotate VPNs
- Auto connect/disconnect VPN for each session
- Launch YouTube in Firefox with autoplay
- Closes browser and VPN every 2 minutes

## ⚙️ Requirements

- Python 3.8+
- Firefox installed
- OpenVPN installed and working
- VPN `.ovpn` config files (in `ovpns/` folder)

## 🔧 Installation

```bash
sudo apt update
sudo apt install openvpn firefox python3-pip
pip install -r requirements.txt

▶️ Usage
Run the script using:

bash
Copy
Edit
python3 fire.py "<YouTube_Link>" "<VPN_Username>" "<VPN_Password>"
Example:
bash
Copy
Edit
python3 fire.py "https://www.youtube.com/watch?v=o_3R0lE48B8" "myvpnuser" "mypassword"
This will:

Loop through all .ovpn files in the ovpns/ folder

Connect to VPN using provided credentials

Open YouTube video in Firefox with autoplay enabled

Wait 2 minutes

Disconnect VPN and close Firefox

Repeat the process with the next .ovpn config

📁 Folder Structure
Copy
Edit
your-project/
├── gui/
│   └── fire.py
├── ovpns/
│   ├── 1.ovpn
│   ├── 2.ovpn
│   └── ...
├── logo.png
├── requirements.txt
└── README.md
⚠️ Disclaimer
This tool is for educational and testing purposes only. Misuse may violate YouTube's Terms of Service.

📄 License
MIT License
© 2025 R4in8ow
