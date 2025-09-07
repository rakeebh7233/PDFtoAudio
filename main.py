import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
import PyPDF2
import os

# ---------------- TTS Engine Setup ----------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("PDF to Voice Converter")
root.geometry("500x300")

selected_files = []

# ---------------- Functions ----------------
def select_files():
    global selected_files
    selected_files = filedialog.askopenfilenames(
        title="Select PDF file(s)",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if selected_files:
        file_label.config(text=f"{len(selected_files)} file(s) selected")
    else:
        file_label.config(text="No files selected")

def read_pdf(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read {file_path}\n{e}")
    return text

def convert_to_audio():
    if not selected_files:
        messagebox.showwarning("No files", "Please select at least one PDF")
        return
    
    # Get user choices
    voice_index = voice_var.get()
    rate = rate_var.get()
    
    engine.setProperty('voice', voices[voice_index].id)
    engine.setProperty('rate', rate)

    converted_files = []
    for file_path in selected_files:
        text = read_pdf(file_path)
        if text.strip():
            base = os.path.splitext(os.path.basename(file_path))[0]
            output_file = f"{base}.mp3"
            engine.save_to_file(text, output_file)
            converted_files.append(output_file)
    
    if converted_files:
        engine.runAndWait()
        messagebox.showinfo("Done", "Converted:\n" + "\n".join(converted_files))
    else:
        messagebox.showwarning("No text", "No readable text found in selected PDFs")


# ---------------- GUI Widgets ----------------
# File selection
tk.Button(root, text="Select PDF(s)", command=select_files).pack(pady=10)
file_label = tk.Label(root, text="No files selected")
file_label.pack()

# Voice selection
voice_var = tk.IntVar(value=0)
tk.Label(root, text="Select Voice:").pack(pady=5)
for idx, v in enumerate(voices):
    tk.Radiobutton(root, text=v.name, variable=voice_var, value=idx).pack(anchor='w')

# Speech rate
rate_var = tk.IntVar(value=150)
tk.Label(root, text="Speech Rate (words per minute):").pack(pady=5)
tk.Scale(root, from_=100, to=300, orient='horizontal', variable=rate_var).pack()

# Convert button
tk.Button(root, text="Convert to Audio", command=convert_to_audio, bg="green", fg="white").pack(pady=20)

root.mainloop()
