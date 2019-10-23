import tkinter as tk 
import webbrowser as wb
#from PIL import ImageTk, Image

def OpenDoc():
	wb.open_new('https://drive.google.com/open?id=1Wi6vTs4UpHZIsDLA-S_BWiwHK9TuY-w4TFQfpT5UlFw')
	return 0

def OpenCredits():
	wb.open_new('https://drive.google.com/open?id=0BzMlLgwt8GfyT0NmZjlUWFpQaVE')
	return 0

def OpenHelp():
	wb.open_new('https://drive.google.com/open?id=0BzMlLgwt8GfyTW9tRnJTWUhWaUU')
	return 0

def restore():
	global root1
	root1.destroy()
	root2 = tk.Tk()
	root2.title("Test")

	#Background Pic
	bgi = tk.PhotoImage(file = 'yo.gif')
	w = tk.Label(root2,image = bgi)
	w.grid(row = 0, column = 0, rowspan = 10, columnspan = 5)

	#Run Button
	run = tk.PhotoImage(file = 'run.gif')
	runButton = tk.Button(root2,image = run,)
	runButton.grid(row = 10, column = 2, pady = 8)

	#Credits Button
	Credits = tk.PhotoImage(file = 'Credits.gif')
	CreditsBtn = tk.Button(root2,image = Credits, command = OpenCredits)
	CreditsBtn.grid(row = 10, column = 1, pady = 8)

	#Doc Button
	Doc = tk.PhotoImage(file = 'Documentation.jpeg')
	DocBtn = tk.Button(root2, image = Doc, command = OpenDoc)
	DocBtn.grid(row = 10, column = 3 , pady = 8)

	#	Help Button
	help = tk.PhotoImage(file = 'help.gif')
	hBtn = tk.Button(root2, image = help, command = OpenHelp)
	hBtn.grid(row = 10, column = 0, pady = 8)
'''
	#justtry
	wc = tk.PhotoImage(file = 'help.gif')
	wcBtn = tk.Button(root2, image = wc, command = func)
	wcBtn.grid(row = 9, column = 1,sticky = 'w')
	root2.geometry('{}x{}'.format(1920, 780))
	root2.mainloop()
'''


def func():
	global root
	root.destroy()
	root1 = tk.Tk()
	root1.title("Test")
	root1.geometry('{}x{}'.format(1920, 780))

	#Background Pic
	bgi = tk.PhotoImage(file = 'yo.gif')
	w = tk.Label(root1,image = bgi)
	w.grid(row = 0, column = 0, rowspan = 10, columnspan = 5)

	#Run Button
	run = tk.PhotoImage(file = 'run.gif')
	runButton = tk.Button(root1,image = run,)
	runButton.grid(row = 10, column = 2, pady = 8)

	#Credits Button
	Credits = tk.PhotoImage(file = 'Credits.gif')
	CreditsBtn = tk.Button(root1,image = Credits, command = OpenCredits)
	CreditsBtn.grid(row = 10, column = 1, pady = 8)

	#Doc Button
	Doc = tk.PhotoImage(file = 'Documentation.gif')
	DocBtn = tk.Button(root1, image = Doc, command = OpenDoc)
	DocBtn.grid(row = 10, column = 3 , pady = 8)

	#Help Button
	help = tk.PhotoImage(file = 'help.gif')
	hBtn = tk.Button(root1, image = help, command = OpenHelp)
	hBtn.grid(row = 10, column = 0)

	#Text
	w1 = tk.Label(root1,text = "Manimouse Testing window\n of Dimensions 1920 x 780.", font=('Helvetica',36,'bold'),justify=tk.LEFT,padx=20)
	w1.grid(row = 5, column = 1, columnspan = 3)

	#Back Button
	back = tk.PhotoImage(file = 'Credits.gif')
	backBtn = tk.Button(root1,image = back, command = restore)
	backBtn.grid(row = 9, column = 1)

	root1.mainloop()


root = tk.Tk()
root.title("Test")

#Background Pic
bgi = tk.PhotoImage(file = 'yo.gif')
w = tk.Label(root,image = bgi)
w.grid(row = 0, column = 0, rowspan = 10, columnspan = 5)

#Run Button
run = tk.PhotoImage(file = 'run.gif')
runButton = tk.Button(root,image = run,)
runButton.grid(row = 10, column = 2, pady = 8)

#Credits Button
Credits = tk.PhotoImage(file = 'Credits.gif')
CreditsBtn = tk.Button(root,image = Credits, command = OpenCredits)
CreditsBtn.grid(row = 10, column = 1, pady = 8)

#Doc Button
Doc = tk.PhotoImage(file = 'Documentation.gif')
DocBtn = tk.Button(root, image = Doc, command = OpenDoc)
DocBtn.grid(row = 10, column = 3 , pady = 8)

#Help Button
help = tk.PhotoImage(file = 'help.gif')
hBtn = tk.Button(root, image = help, command = OpenHelp)
hBtn.grid(row = 10, column = 0, pady = 8)

#justtry
wc = tk.PhotoImage(file = 'help.gif')
wcBtn = tk.Button(root, image = wc, command = func)
wcBtn.grid(row = 9, column = 1,sticky = 'w')

root.geometry('{}x{}'.format(1920, 1080))
#root.resizable(width=False, height=False)


#canvas=tk.Canvas(root,bg='grey',height=400,width=800)

#filename = ImageTk.PhotoImage(Image.open("ITSPlogo.gif"))
#image = canvas.create_image(250, 250,  image=filename)

#panel = Label(root, image = image)
#panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()
