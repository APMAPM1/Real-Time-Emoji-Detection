# Real-Time Emoji Detection from Face Emotions 😊
This project performs **real-time emotion detection** using your webcam and displays the corresponding **emoji in the top-left corner** of the screen based on the detected facial emotion.

## 🚀 Project Overview

- Real-time face and emotion detection using webcam.
- Displays a **corresponding emoji in the top-left corner** based on the detected emotion.
- Uses OpenCV's Haar Cascade for face detection.
- Lightweight, interactive, and fun to run.

## 📂 Folder Structure

```plaintext
├── emojis/
│    ├── happy.png
│    ├── sad.png
│    ├── angry.png
│    └── surprise.png
│
├── haarcascades/
│    └── haarcascade_frontalface_default.xml
│ 
├── .gitignore
│
├── README.md
│
├── main.py
│
└── requirements.txt
```

## ⚙️ Requirements

- Python 3.7 or higher
- Webcam
- OpenCV
- FER Library
- TensorFlow
- MoviePy

## 🛠️ Setup & Installation

1.  **Clone the Repository:**

    ```bash
    # Replace with your repo URL if you put it on GitHub
    git clone https://github.com/APMAPM1/Real-Time-Emoji-Detection.git
    cd Real-Time-Emoji-Detection
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run:**

    ```bash
    python main.py
    ```

    Your webcam will open automatically.
    Detected faces will be highlighted.
    The corresponding emoji will appear in the top-left corner based on the detected emotion.

    Press 'q' to exit the program.

## 🔗 Resources

- [OpenCV Haar Cascade Tutorial](https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html)
- [OpenCV Python Documentation](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [Haarcascade Files on GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades)
- [FER Library GitHub](https://github.com/justinshenk/fer)
- [TensorFlow Documentation](https://www.tensorflow.org/)
