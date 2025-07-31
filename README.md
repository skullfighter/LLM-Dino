# 🦖 LLM Dino Bot

An AI-powered bot that plays the Chrome Dino Game by detecting obstacles using computer vision and asking a local language model (LLM) whether the Dino should jump. It utilizes a local LLM served via [Ollama](https://ollama.com/) (e.g., Mistral) to make decisions in real time.

---

## 📸 Features

- Captures a specific screen region in front of the Dino.
- Detects obstacles using OpenCV.
- Asks a locally running LLM whether to jump.
- Uses `pyautogui` to press the space bar and make the Dino jump.
- Fully autonomous and runs in real-time.

---

## 🛠️ Requirements

- Python 3.7+
- A local LLM served via [Ollama](https://ollama.com/) (e.g., `mistral`)
- Chrome Dino Game (https://chromedino.com/)
- Game window must be focused and placed in the default detection region

---

1. **Download the Ollama from given website :- https://ollama.com/ **

2. **Install dependencies**:

    ```bash
    pip install opencv-python numpy pyautogui mss requests pillow
    ```

3. **Install and run Ollama**:

    Follow instructions on https://ollama.com to install and run an LLM like `mistral`.

    ```bash
    ollama run mistral
    ```

---

## ⚙️ Configuration

You can change the following in the script:

```python
OLLAMA_URL = "http://localhost:11434/api/generate"  # LLM API endpoint
MODEL = "mistral"                                   # LLM model name
SPEED = 0.05                                        # Dino speed / loop interval

DETECTION_REGION = {
    'top': 272,
    'left': 922,
    'width': 233,
    'height': 190
}
