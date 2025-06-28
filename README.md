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

## 🔧 Usage
python3 vpn_viewer.py "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
