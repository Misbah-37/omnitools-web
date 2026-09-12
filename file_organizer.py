"""
Tangent File Organizer — Open Source Desktop Utility
Part of the Tangent Suite (https://misbah-37.github.io/tangent/)

A 100% offline, privacy-first desktop utility to automatically categorize 
messy directories (Downloads, Desktop, etc.) into structured folders.

- Zero external dependencies (100% Python Standard Library).
- Zero network communication (0 bytes outbound).
- Zero registry modifications.
"""

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

FILE_TYPES = {
    "Data & Spreadsheets": [".csv", ".xlsx", ".xls", ".json", ".xml", ".sql"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".rtf", ".odt", ".md"],
    "Presentations": [".pptx", ".ppt", ".key"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".raw", ".heic"],
    "Design Files": [".psd", ".ai", ".xd", ".fig"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Archives & Zips": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programming": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".ipynb", ".sh"],
    "Applications & Installers": [".exe", ".msi", ".apk", ".dmg", ".bat"],
    "Disc Images": [".iso", ".img"],
    "Fonts": [".ttf", ".otf"]
}

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder_selected)

def organize_files():
    folder_path = path_entry.get()
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "Please select a valid folder path.")
        return
        
    try:
        all_files = os.listdir(folder_path)
        moved_count = 0
        
        for file in all_files:
            file_path = os.path.join(folder_path, file)
            # Skip folders, we only want to move files
            if os.path.isdir(file_path):
                continue
                
            name, extention = os.path.splitext(file)
            
            # Loop through the dictionary to find the right folder
            for folder_name, extensions in FILE_TYPES.items():
                if extention.lower() in extensions:
                    new_folder = os.path.join(folder_path, folder_name)
                    os.makedirs(new_folder, exist_ok=True)
                    shutil.move(file_path, new_folder)
                    moved_count += 1
                    break
                    
        messagebox.showinfo("Success", f"Successfully organized {moved_count} files!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Tangent File Organizer")
try:
    if os.path.exists("app_icon.ico"):
        root.iconbitmap("app_icon.ico")
except Exception:
    pass
root.geometry("400x150")
root.resizable(False, False)

# Create padding frame
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True, fill=tk.BOTH)

# Label
label = tk.Label(frame, text="Select Folder to Organize:")
label.pack(anchor=tk.W, pady=(0, 5))

# Path Entry and Browse Button Frame
input_frame = tk.Frame(frame)
input_frame.pack(fill=tk.X, pady=(0, 15))

path_entry = tk.Entry(input_frame)
path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

browse_btn = tk.Button(input_frame, text="Browse", command=browse_folder)
browse_btn.pack(side=tk.RIGHT)

# Organize Button
organize_btn = tk.Button(frame, text="Organize!", bg="#00d2ff", fg="#08090d", font=("Arial", 10, "bold"), command=organize_files)
organize_btn.pack(fill=tk.X)

# Start the application
if __name__ == "__main__":
    root.mainloop()
