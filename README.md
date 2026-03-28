# 🏍️ Varroc Smart HUD: AI Audio Hazard Detection
**An AI-powered "second set of ears" for rider safety.**

## 🛑 The Problem
Motorcycle riders frequently suffer from auditory masking at high speeds. Wind noise, engine roar, and the physical insulation of modern helmets block out crucial environmental audio cues—like approaching ambulances or aggressive blind-spot honking. This auditory blind spot is a leading cause of fatal accidents.

## 💡 Our Solution
The **Varroc Smart HUD** is a real-time acoustic monitoring system designed to be integrated directly into a motorcycle helmet. 
Instead of relying purely on visual checks, our system constantly analyzes the acoustic environment using a deep neural network. When a critical hazard (like a siren or car horn) is detected, it instantly flashes a high-contrast visual alert on the rider's Heads-Up Display (HUD), saving vital reaction time.

### ✨ Key Features
* **Real-Time Acoustic Processing:** Standardized audio extraction at 22,050Hz for immediate analysis.
* **Smart Filtering:** Ignores normal street noise and traffic to prevent HUD distraction.
* **Instant Visual Feedback:** Millisecond-response alerts when threat thresholds are crossed.

## 🧠 Tech Stack
* **Audio Processing:** `librosa` (Extracting 40 MFCC bins, amplitude normalization)
* **AI/ML:** `TensorFlow` / `Keras` (Deep Neural Network trained on the UrbanSound8K dataset)
* **Frontend/UI:** `Streamlit` for rapid HUD simulation and prototyping
* **Data Handling:** `NumPy`, `Pandas`, `scikit-learn` (Oversampling for class balance)

## 🚀 How to Run the Prototype Locally
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Varroc-Smart-HUD.git](https://github.com/YOUR_USERNAME/Varroc-Smart-HUD.git)

   Install the required dependencies:

Bash
pip install -r requirements.txt
Run the Streamlit HUD application:

Bash
streamlit run app.py
Upload a .wav file to test the environment analysis!
