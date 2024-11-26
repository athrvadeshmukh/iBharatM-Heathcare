# IBharatM Health Care AI Project
![image](https://github.com/user-attachments/assets/21125e44-3bf6-4213-b46f-e3eeefe93429)

![IBMSplashScreen](https://github.com/user-attachments/assets/63b1248f-f92c-4ec4-83ab-64ff2b60a3fb)

*An innovative solution for early detection of lung diseases using AI.*

---

## Introduction

**IBharatM Health Care AI** is a cutting-edge healthcare project aimed at assisting medical professionals and individuals in identifying lung diseases like **COVID-19**, **Pneumonia**, and normal conditions from chest X-rays. Built using **Microsoft Azure Custom Vision Service**, the application predicts disease probabilities and provides an interactive interface for better analysis. The project also integrates the **Microsoft Health Bot Service**, offering users healthcare-related guidance.

---

## Features
- **Chest X-ray Disease Detection**: Predict lung diseases from uploaded or URL-based chest X-rays.
- **Interactive Visualizations**: Analyze predictions using bar graphs, pie charts, and progress bars.
- **Health Bot Assistance**: Get healthcare-related advice and information from the integrated bot.
- **User-Friendly Interface**: A sleek desktop application built with **PySide6**.

---

## Technology Stack
- **Programming Language**: Python 3.8+
- **Cloud Services**: Microsoft Azure Custom Vision, Microsoft Health Bot
- **Libraries**:
  ```
  - PySide6: GUI framework
  - Pillow: Image processing
  - Requests: API interaction
  - Matplotlib: Data visualization
  ```

---

## Team Members
- **Athrva Deshmukh** (Team Lead)  
- **Gourav Kushwaha** (Team Lead)  
- **Sonu Kushwaha**  
- **Naushad Ali**

---

## How It Works
1. **Custom Vision AI Model**: Trained on datasets of chest X-ray images (COVID-19, pneumonia, normal lungs).
   - Upload or link an X-ray image.
   - Get predictions for potential diseases with associated probabilities.
2. **Interactive Results**:
   - View results in graph formats (bar graph, pie chart, etc.).
3. **Health Bot**:
   - Provides healthcare information, including disease symptoms, tips, and general assistance.

---

## Installation

### Prerequisites
```
- Python >= 3.8
```
- An active internet connection for API calls.

### Steps
1. Clone the repository:
   ```
   git clone https://github.com/your-username/ibharatm-healthcare-ai.git
   cd ibharatm-healthcare-ai
   ```
2.  Install dependencies:
```
     pip install -r requirements.txt
```
4. Run the application:
```
   python main.py
```

## Usage
Launch the application.
Upload a chest X-ray image or provide a URL.
Wait for the AI model to analyze the image.
View the prediction results along with interactive graphs.
Use the Health Bot for further healthcare-related guidance.

## Screenshots
1. Application Home Screen

2. X-ray Upload & Prediction

3. Health Bot Interface

![WhatsApp Image 2024-11-26 at 22 25 53_a6ef8027](https://github.com/user-attachments/assets/9ce14b64-46c2-4dad-9c27-44926f7b62f4)
![WhatsApp Image 2024-11-26 at 22 25 14_12b7f001](https://github.com/user-attachments/assets/538094cc-d891-44df-be38-d5e03d5f31c1)
![WhatsApp Image 2024-11-26 at 22 24 55_1dd11b24](https://github.com/user-attachments/assets/2dfb74ff-0e5b-4242-ad27-ec498d47b38b)
![WhatsApp Image 2024-11-26 at 22 24 23_abaa3981](https://github.com/user-attachments/assets/4c9d87a2-e164-40e0-845d-da67a5f80644)
![WhatsApp Image 2024-11-26 at 22 23 21_8441ca9a](https://github.com/user-attachments/assets/91a0f872-e3c2-441d-a4a3-c477d34a3bf5)
![WhatsApp Image 2024-11-26 at 22 22 42_42f237d6](https://github.com/user-attachments/assets/dcd53e65-1631-4bcd-bc9b-cfb905a08243)


## Demo Video

##  Set Up a Virtual Environment
It is recommended to use a virtual environment to isolate dependencies. Follow these steps:

On Windows:
```
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```


## Configure API Keys
Add your Azure Custom Vision Prediction Key and Endpoint in the predict_image() function in the main.py file:
```
headers = {
    "Prediction-Key": "YOUR_AZURE_PREDICTION_KEY"
}
url = "YOUR_AZURE_CUSTOM_VISION_URL"
```

## Requirements
Refer to the requirements.txt file for all dependencies:

### **requirements.txt File:**
```
plaintext
PySide6==6.6.0
requests==2.31.0
Pillow==9.2.0
matplotlib==3.8.0
```

## Contributions
We welcome contributions!
```
Fork the repository.
Create a new branch: git checkout -b feature/YourFeatureName.
Commit your changes: git commit -m 'Add some feature'.
Push to the branch: git push origin feature/YourFeatureName.
Open a pull request.
```
