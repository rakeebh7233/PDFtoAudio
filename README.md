# 📖 PDF to Voice Converter

A Python desktop app that converts PDF files into **speech** and saves them as **MP3 audio files**.  
Built with **Tkinter** for GUI, **PyPDF2** for text extraction, and **pyttsx3** for offline text-to-speech.

---

## 🚀 Features
- Select **one or multiple PDF files**.
- Convert PDFs into **MP3 audio files** (same name as the PDF).
- Choose from available **system voices** (male, female, accent depending on OS).
- Adjust **speech rate** (100–300 words per minute).
- Supports **multi-batch conversion**:
  - Upload → Convert → Upload new files → Convert again (no need to restart the app).
- Works **offline** (no internet connection required).

---

## 🛠 Requirements
- Python **3.8+**
- Libraries:
  - `pyttsx3` (Text-to-Speech engine)
  - `PyPDF2` (PDF reader/extractor)
  - `tkinter` (GUI framework, included with Python on most systems)

Install dependencies with:

```bash
pip install pyttsx3 PyPDF2
```
## :camera: Snapshots
<img width="503" height="334" alt="PDFtoAudioGUI" src="https://github.com/user-attachments/assets/8c81dc80-6bc5-4727-a10d-312806c504a9" />


## 📂 Project Structure
```bash
pdf-to-voice/
│
├── main.py # Main application script
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

## ▶️ Usage
Run the application:

```bash
python main.py
```

1. Click "Select PDF(s)" and choose one or more PDF files.

2. Select a voice from the available list.

3. Adjust the speech rate (slider).

4. Click "Convert to Audio".

5. The program will generate .mp3 files in the same folder as the PDFs.

6. After conversion, you can select new PDFs and repeat the process without restarting the app.

## 🎯 Example
If you select [report.pdf], the app will generate:

```bash
report.mp3
```
## 🧩 Future Improvements
* Add pause/resume/stop controls while reading.

* Display highlighted text in sync with audio.

* Integrate with cloud TTS (Google, Azure, Amazon Polly) for more natural voices.

* Summarize PDFs before reading.

* Export to more audio formats (e.g., WAV, OGG).
