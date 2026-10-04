# 👤 Face Detection using OpenCV

A simple real-time **face detection application** built using **Python and OpenCV**. The project uses OpenCV's **Haar Cascade Classifier** to detect human faces through a webcam and draws a bounding box around each detected face.

## ✨ Features

* 🎥 Real-time webcam face detection
* 👤 Detects multiple faces simultaneously
* 🟩 Draws bounding boxes around detected faces
* ⚡ Real-time processing using OpenCV
* 🖥️ Simple and beginner-friendly implementation
* ⌨️ Press `ESC` to exit

---

## 🛠️ Technologies Used

| Technology   | Purpose                              |
| ------------ | ------------------------------------ |
| Python       | Programming language                 |
| OpenCV       | Computer vision and image processing |
| Haar Cascade | Face detection                       |
| Webcam       | Real-time video input                |

---

## 📁 Project Structure

```text
Face-Detection-OpenCV/
│
├── face_detection.py
├── haarcascade_frontalface_default.xml
└── README.md
```

> **Important:** The `haarcascade_frontalface_default.xml` file must be present in the project folder because the program loads it directly.

---

## 🧠 How It Works

The project follows these steps:

```text
Webcam
   ↓
Capture Video Frame
   ↓
Convert Frame to Grayscale
   ↓
Haar Cascade Face Detection
   ↓
Detect Face Coordinates
   ↓
Draw Bounding Box
   ↓
Display Result
```

### 1. Access the webcam

OpenCV is used to access the computer's camera:

```python
webcam = cv2.VideoCapture(0)
```

### 2. Convert the frame to grayscale

Face detection is performed on a grayscale image:

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

### 3. Detect faces

The Haar Cascade classifier searches for faces:

```python
faces = face_cascade.detectMultiScale(
    gray,
    1.6,
    4
)
```

The detected faces are returned as:

```text
(x, y, width, height)
```

### 4. Draw bounding boxes

For every detected face, a green rectangle is drawn:

```python
cv2.rectangle(
    img,
    (x, y),
    (x + w, y + h),
    (0, 255, 0),
    3
)
```

---

## 📦 Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/Arpitadas001/face-detection-opencv.git
```

Then:

```bash
cd face-detection-opencv
```

### Step 2: Install OpenCV

```bash
pip install opencv-python
```

---

## ▶️ How to Run

Run the Python program:

```bash
python face_detection.py
```

The webcam will open and detected faces will be highlighted with green rectangles.

### Exit the application

Press:

```text
ESC
```

to close the webcam window.

---

## 📸 Example

When a face is detected, the application displays a bounding box around it:

```text
        ┌───────────────┐
        │               │
        │     FACE      │
        │               │
        └───────────────┘
```

The application can also detect multiple faces in the same frame.

---

## 🔍 Haar Cascade Classifier

This project uses:

```text
haarcascade_frontalface_default.xml
```

Haar Cascade is a classical computer vision technique used to detect objects in images.

For this project, it is specifically trained to detect **frontal human faces**.

---

## 💻 Complete Code

```python
import cv2

print("OpenCV version:", cv2.__version__)

# Load Haar Cascade classifier
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

# Open webcam
webcam = cv2.VideoCapture(0)

while True:

    success, img = webcam.read()

    if not success:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        1.6,
        4
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:

        cv2.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

    # Display result
    cv2.imshow("Face Detection", img)

    # Press ESC to exit
    key = cv2.waitKey(10)

    if key == 27:
        break

# Release webcam
webcam.release()

# Close OpenCV windows
cv2.destroyAllWindows()
```

---

## ⚙️ Parameters Used

The face detector uses:

```python
detectMultiScale(gray, 1.6, 4)
```

Here:

* `gray` → Grayscale input image
* `1.6` → Scale factor
* `4` → Minimum number of neighboring detections required to consider a region a face

The scale factor affects the detection process and can be adjusted depending on the desired speed and detection accuracy.

---

## 🚀 Future Improvements

This project can be extended with:

* 👁️ Eye detection
* 😊 Smile detection
* 😷 Mask detection
* 🧑‍🤝‍🧑 Face counting
* 🏷️ Face recognition
* 📸 Automatic face capture
* 🔐 Face-based authentication
* 📊 FPS counter
* 🎯 Improved detection accuracy using modern deep-learning models

---

## 🎯 Learning Outcomes

This project helps demonstrate:

* Python programming
* OpenCV fundamentals
* Computer vision
* Image preprocessing
* Grayscale conversion
* Haar Cascade classifiers
* Real-time video processing
* Object detection
* Webcam integration

---

## 👩‍💻 Author

**Arpita Das**

B.Tech Computer Science & Engineering

GitHub: [Arpitadas001](https://github.com/Arpitadas001?utm_source=chatgpt.com)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!
