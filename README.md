# 📃 vtt2txt2docx
This Python script generates cleaned up versions of .txt and .docx files from an MS Stream .vtt caption file.  It strips out content such as lines beginning with WEBVTT, NOTE, a timestamp, or a reference such as 3dc72631-b191, leaving only the text generated from the speaker's voice.

<img src="https://raw.githubusercontent.com/Lynsay/vtt2txt2docx/main/gfx/vtt2txt2docx.png" alt="vtt2txt2docx on the command line" width="200"/>


## 🤔 Rationale
Last year (during COVID-19 times), I recorded some of my lectures without using a text script to guide me.  For consistency, this year, I would like to use a text script for all recorded lectures.  To help me write them up, I have developed this tool to take a .vtt caption file from my old lectures, and convert these into different formats, helping me to create new text scripts.

## ⚙️ Requirements
To run the script, the following packages are required:

* `python-docx` - Allows Python scripts to generate Word .docx files
* `cowsay` - Generates ASCII art pictures of a cow with a message (optional)

Install these via pip:

`pip install python-docx cowsay`

## ⌨️ Usage
* `python vtt2txt2docx.py fileYouWantToConvert.vtt`

## 🔨 Testing Notes
The script has been tested on MacOS Catalina version 10.15.7 with Python 3.6.10. Your mileage may vary.

