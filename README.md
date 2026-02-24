🌿 YOLO-Based Weed Detection System (Streamlit)

A deep learning–based **weed detection system** built using **YOLO (You Only Look Once)** and deployed with **Streamlit**.  
This application detects weeds in agricultural field images/videos to support **precision farming** and reduce manual labor.

---

## 🚀 Features

- ✅ Real-time weed detection using YOLO
- 📸 Image upload and detection
- 🎥 Video/Camera-based weed detection (optional)
- 📊 Confidence score display
- 🌱 Helps reduce herbicide usage and improve crop yield
- 🌐 Simple and interactive Streamlit UI

---

## 🧠 Tech Stack

- **Python**
- **YOLO (v5 / v8 – depending on your implementation)**
- **OpenCV**
- **PyTorch**
- **Streamlit**
- **NumPy**
- **Pillow**

---

## 📁 Project Structure
weed-detection-system/ │ ├── app.py                      # Streamlit application ├── model/ │   └── best.pt                 # Trained YOLO model ├── utils/ │   ├── detector.py             # YOLO inference logic │   └── preprocessing.py        # Image/video preprocessing ├── sample_data/ │   ├── images/ │   └── videos/ ├── requirements.txt ├── README.md └── yolov8_training/ ├── data.yaml └── train.py
Copy code

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/weed-detection-system.git
cd weed-detection-system
2️⃣ Create Virtual Environment (Recommended)
Bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
Bash
Copy code
pip install -r requirements.txt
▶️ Run the Streamlit App
Bash
Copy code
streamlit run app.py
The app will start locally at:
Copy code

http://localhost:8501
📸 How It Works
Upload an image or video of a farm field
YOLO model processes the input
Weed regions are detected and highlighted with bounding boxes
Confidence score is displayed for each detection
🏋️ Model Training (Optional)
If you want to train your own YOLO model:
Dataset Format (YOLO)
Copy code

dataset/
├── images/
│   ├── train/
│   └── val/
├── labels/
│   ├── train/
│   └── val/
Train Command Example
Bash
Copy code
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640
After training, place best.pt inside the model/ folder.
📊 Use Cases
🌾 Smart agriculture
🚜 Automated weed monitoring
🌍 Precision farming
🧪 Agricultural research
🤖 AI-powered crop management
⚠️ Limitations
Performance depends on dataset quality
Low accuracy in poor lighting or blurred images
Needs retraining for different crop types
🔮 Future Improvements
Live drone feed integration
Multi-class weed classification
Mobile deployment
GPS-based weed mapping
Herbicide spraying automation
Author
Avikal Bhatt
📧 Email: avikalbhatt123@gmail.com
🔗 GitHub: https://github.com/avikal286⁠�
🔗 LinkedIn: https://www.linkedin.com/in/avikal-bhatt-418902372⁠�
