try:
  file = open("a_file.txt")
except:
  open("a_file.txt", "w")
  file.write("something")
finally:
  file.close()
# from tkinter import *
# Label(text="Password:", font=("Segoe UI", 10), bg="#f7f7f7").grid(row=3, column=0, sticky="e")          