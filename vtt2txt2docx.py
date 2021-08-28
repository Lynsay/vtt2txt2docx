#!/usr/bin/env python
'''
	Author: Lynsay A. Shepherd
	
	Date: 27th August 2021

	Name: vtt2txt2docx.py

	Desc: Generate cleaned up .txt and .docx files from an MS Stream .vtt caption file- helpful for preparing scripts when new recordings are required for a lecture.
'''

#Imports required
import re
from docx import Document
import sys
import pathlib
import os
import cowsay #for the ascii art

#Process the original .vtt file
def processTheFile():
	try:
		#pass in file name via Terminal
		with open(sys.argv[1], "r") as f:
			
			#get file extension and check it's a .vtt
			fileExtension=pathlib.Path(sys.argv[1]).suffix

			if fileExtension == ".vtt":
				print("This is a .vtt file - proceeding with .vtt to .txt conversion")

				#grab the name of the existing file- this will be used for new files generated
				existingFileName=os.path.splitext(sys.argv[1])[0]
				
				with open(existingFileName+".txt", "w", encoding='utf-8') as createNew:
					for line in f:
						#If a MS Caption line starts with WEBVTT, NOTE, a timestamp, or a reference such as 3dc72631-b191-, do not include this in the new file generated.
						if line.startswith("WEBVTT") or line.startswith("NOTE ") or re.match("^[0-9][0-9]:",line) or re.match("^[A-Za-z0-9]{8,8}-",line):
							continue
						else:
							if re.match(r'^\s*$', line):
								continue
							else:
								#remove trailing newlines and replace with a space so strings do not join together
								line = line.replace('\n',' ')
								#add new lines after new sentences
								line = line.lstrip("  ")
								line = line.lstrip(" ")
								#add new lines after new sentences (but first ensure no sentence ends with a double space)
								line = line.replace('.  ','. ')
								line = line.replace('. ','. \n\n')
								#all good, write line to new file
								createNew.write(line)

				#take the newly created .txt file and generate a .docx
				txtToDocx(existingFileName)
			
			else:
				print("This is not a .vtt file - process terminating")

	except:
		print ("Error processing file")



#Also convert generated .txt file to .docx
def txtToDocx(existingFileName):
	try:
		print ("Converting .txt to .docx")
		document = Document()
		with open(existingFileName+".txt", "r", encoding='utf-8') as openNewFile:
			line = openNewFile.read()
			document.add_paragraph(line)
			document.save(existingFileName+".docx")
			print ("vtt2txt2docx - DONE")

	except:
		print ("Error with txtToDocx method")


#Main
def main():
	try:
		#cowsay ascii art
		cowsay.cow('vtt2txt2docx Tool\n------------------\nhttps://github.com/Lynsay')
		processTheFile()

		
	except:
		print ("Error with main method")
	

if __name__ == "__main__":
	main()