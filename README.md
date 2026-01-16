# 👁️ Smart Vision using Raspberry Pi + YOLOv8 + Voice Assistance

## 📌 Project Overview
This project is a **Real-Time Smart Vision System** built using a **Raspberry Pi Camera** and **YOLOv8 Object Detection**.  
It detects important objects and gives **voice announcements** using Text-to-Speech (TTS).

✅ Live camera streaming  
✅ Object detection using YOLOv8  
✅ Voice feedback using gTTS  
✅ Direction guidance: left / ahead / right  
✅ Distance estimation: near / far  

---

## 🎯 Applications
- Smart assistance for visually impaired people  
- Indoor navigation and object awareness  
- Safety monitoring system  
- Smart robotics vision module  

---

## 🧰 Hardware Requirements
- Raspberry Pi (3 / 4 / 5 recommended)  
- Raspberry Pi Camera Module (IMX219 / IMX708)  
- Speaker / Earphones (3.5mm / USB)  
- Internet connection (for gTTS)  

---

## 💻 Software Requirements
- Raspberry Pi OS (Latest recommended)  
- Python 3  
- Picamera2  
- OpenCV  
- Ultralytics YOLOv8  
- gTTS  
- mpg123  

---

## ✅ Step 1: Enable Camera on Raspberry Pi
1. Click **Raspberry Pi icon (top-left)**
2. Go to **Preferences**
3. Open **Raspberry Pi Configuration**
4. Click **Interfaces**
5. Enable **Camera**
6. Click **OK**

✅ Raspberry Pi will reboot automatically.

---

## ✅ Step 2: Verify Pi Camera Connection
Run this command:
dmesg | grep imx

✅ Step 3: Install Required Libraries


🔹 Update System


-> sudo apt update


-> sudo apt upgrade -y

🔹 Install Picamera2


-> sudo apt install -y python3-picamera2

🔹 Install OpenCV


-> sudo apt install -y python3-opencv

🔹 Install YOLOv8 (Ultralytics)


-> python3 -m pip install ultralytics --break-system-packages

🔹 Install Text-to-Speech (gTTS)


-> python3 -m pip install gTTS --break-system-packages

🔹 Install Audio Player


-> sudo apt install mpg123 -y


📦 Download YOLOv8 Model


Download the model:


wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt


Move it into the Models folder:


mkdir -p Models


mv yolov8n.pt Models/


▶️ Run the Project


Run Smart Vision code:


python3 Code/Smart_Vision.py


Press q to exit.
