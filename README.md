Here is a complete and professional **README.md** for your **Eye Gaze Direction Classification** project.

# Eye Gaze Direction Classification

## 📌 Project Overview

Eye Gaze Direction Classification is a computer vision-based system that determines the direction in which a user is looking using real-time webcam input. The system detects facial landmarks and iris positions to classify gaze direction into four categories:

* Left
* Right
* Center
* Up

The project is implemented using **Python**, **OpenCV**, and **MediaPipe Face Mesh** and provides real-time gaze prediction with an accuracy greater than 80%.

---

## 🎯 Objective

The objective of this project is to accurately determine the direction in which a person is looking using webcam input. The system classifies eye movements into Left, Right, Center, and Up while handling challenges such as fast eye movements and users wearing glasses.

---

## 🛠 Technologies Used

* Python
* OpenCV
* MediaPipe Face Mesh
* NumPy
* GitHub

---

## 📂 Project Structure

```
eye-gaze-direction-classification/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── utils/
│   ├── __init__.py
│   ├── eye_landmarks.py
│   ├── gaze_estimator.py
│   └── visualization.py
│
├── models/
│   └── gaze_model.pkl
│
├── dataset/
│   ├── left/
│   ├── right/
│   ├── center/
│   └── up/
│
└── output/
```

---

## ⚙️ Features

* Real-time webcam-based gaze tracking
* Eye landmark detection
* Iris position estimation
* Classification into Left, Right, Center, and Up
* Handles fast eye movement
* Supports users wearing glasses
* Accuracy greater than 80%
* Lightweight and efficient implementation

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/eye-gaze-direction-classification.git
cd eye-gaze-direction-classification
```

### Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python app.py
```

The webcam will open and display the detected gaze direction in real time.

---

## 🔄 Workflow

1. Capture webcam frames using OpenCV.
2. Detect facial landmarks using MediaPipe Face Mesh.
3. Extract eye and iris coordinates.
4. Estimate iris position inside the eye.
5. Classify gaze direction.
6. Display the output in real time.

---

## 📊 Output Example

```json
{
    "gaze_direction": "left"
}
```

Possible outputs:

* Left
* Right
* Center
* Up

---

## 🧩 Module Description

### app.py

Main file responsible for:

* Webcam initialization
* Frame processing
* Calling gaze estimation functions
* Displaying results

### eye_landmarks.py

Responsible for:

* Extracting eye landmarks
* Detecting iris coordinates
* Returning eye positions

### gaze_estimator.py

Responsible for:

* Computing iris position
* Determining gaze direction
* Returning classification results

### visualization.py

Responsible for:

* Displaying gaze direction
* Drawing text and landmarks
* Providing visual feedback

---

## 🧪 Testing and Validation

Testing was performed under:

* Different lighting conditions
* Fast eye movement
* Users wearing glasses
* Minor head movements
* Real-time webcam input

### Performance

* Classification Accuracy: >80%
* Low latency
* Stable predictions
* Real-time processing

---

## ⚠ Challenges Faced

### Fast Eye Movement

Rapid eye movements caused unstable predictions.

**Solution:** Threshold values were adjusted to improve stability.

### Glass Reflections

Reflections affected iris detection.

**Solution:** MediaPipe Face Mesh with refined landmarks improved robustness.

### Dependency Issues

MediaPipe and TensorFlow version conflicts occurred.

**Solution:** Created a virtual environment and installed compatible versions.

---

## 📈 Future Enhancements

* Add Down gaze direction
* Blink detection
* Drowsiness detection
* Attention monitoring
* Deep learning-based gaze estimation
* Flask API deployment
* Web application integration

---

## 🎓 Learning Outcomes

Through this project, the following skills were gained:

* Computer Vision
* OpenCV
* MediaPipe Face Mesh
* Real-time image processing
* Facial landmark detection
* Debugging and testing
* Modular Python programming
* GitHub version control

---

## 📚 References

1. MediaPipe Documentation
   [https://developers.google.com/mediapipe](https://developers.google.com/mediapipe)

2. OpenCV Documentation
   [https://opencv.org/](https://opencv.org/)

3. NumPy Documentation
   [https://numpy.org/doc/](https://numpy.org/doc/)

4. Python Documentation
   [https://docs.python.org/3/](https://docs.python.org/3/)

5. MediaPipe GitHub Repository
   [https://github.com/google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe)

6. OpenCV GitHub Repository
   [https://github.com/opencv/opencv](https://github.com/opencv/opencv)

7. GitHub
   [https://github.com/](https://github.com/)

---

## 👩‍💻 Author

**Nandini Pulapa**

Supervisor: **Afjal**

Project: **Eye Gaze Direction Classification**

Year: **2026**

This README is suitable for a **GitHub repository** and gives your project a professional appearance.
