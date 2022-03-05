from art import text2art
import sys
import webbrowser
import os

print(text2art("Desert Fox"))
print("If you know nothing about BASIC programming languages, Go check wikipedia page")
print("Speacial Thanks to Ruslan and CodePlus")
webbrowser.open("https://ruslanspivak.com/lsbasi-part1/")
webbrowser.open("https://www.youtube.com/playlist?list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD")

print(text2art("---------------------------"))
programname = input("The name of your programming language:").replace(" ", "_") 
programext = input("The extension of your programming language (without dot):")


default_shell = open("shell.py","r").read()
custom_shell  = open(programname+".py", "w")


KEYWORDS = [
  'customized VAR',
  'customized AND',
  'customized OR',
  'customized NOT',
  'customized IF',
  'customized ELSE',
  'customized ELIF',
  'customized FOR',
  'customized TO',
  'customized STEP',
  'customized WHILE',
  'customized FUNC',
  'customized THEN',
  'customized END',
  'customized RETURN',
  'customized CONTINUE',
  'customized BREAK']
builtin_KEYWORDS = [
  "customized NULL",
  "customized FALSE",
  "customized TRUE",
  "customized MATH_PI", 
  "customized PRINT",
  "customized PRINT_RET",
  "customized INPUT",
  "customized INPUT_INT",
  "customized CLEAR",
  "customized IS_NUM",
  "customized IS_STR",
  "customized IS_LIST", 
  "customized IS_FUN", 
  "customized APPEND",
  "customized POP",
  "customized EXTEND",
  "customized LEN",
  "customized RUN"
  ]


for i in KEYWORDS:
  custom_KEYWORD = input(f"Your {i}:")
  default_shell = default_shell.replace(i,custom_KEYWORD)


Builtinfuncs    = input("Do you Want to Customize built-in functions? (Y/N):")
while not Builtinfuncs in ("Y", "N"):
  Builtinfuncs = input("Please give a valid answer (Y/N):")

if Builtinfuncs == "Y":
  for i in builtin_KEYWORDS:
    custom_builtin_KEYWORD = input(f"Your {i}:")
    default_shell = default_shell.replace(i,custom_builtin_KEYWORD)
elif Builtinfuncs == "N":
  for i in builtin_KEYWORDS:
    default_shell = default_shell.replace(i,i.replace("customized "))

default_shell = default_shell.replace("PROGRAM_NAME",programname)


custom_shell.write(default_shell)
print("DO NOT TOUCH ANYTHING")

os.system("pip install pyinstaller")
os.system(f"pyinstaller --onefile --name {programname} {programname}.py")
print(text2art("---------------------------"))
print("here you go, you can find your programming language in 'dist' file. You made it all by own, good job!")
print("If you want you can delete everything except .exe file. To write a program just create a new file with your extension end edit it with your editor")
print("I will update this program to new things such as cheetsheats. Keep following.")
print("If anything goes wrong contact me via instagram: @mehmet_deniz_yapici")
input("Press Anything to Close the Program")
sys.exit()