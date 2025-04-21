

import tkinter as tk
from tkinter import messagebox

class Gui:
    def __init__(self):
        self.resolver = False
        self.fileName = ""
        self.fileNameSolve = self.fileName + "Solve"

        self.root = tk.Tk()

        self.root.geometry("400x300")

        self.root.title("Generador de Sudokus Instantaneo")

        self.label = tk.Label(self.root, text="Genera tu sudoku ya", font=('Arial', 20))
        self.label.pack(padx=10, pady=10)

        self.label = tk.Label(self.root, text="Pon el nombre de archivo a generar", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=1, width=20 ,font=('Arial', 18))
        self.textbox.pack(padx=10, pady=10)

        self.checkState = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Generar archivo con respuesta", font=('Arial', 18), variable=self.checkState)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Generar", font=('Arial',20), command=self.Generar)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def Generar(self):
        if self.checkState.get() == 1:
            self.resolver = True
            self.fileName = self.textbox.get('1.0', tk.END)
            self.fileNameSolve = self.fileName + "Solve"
            message = "Archivo generado: \n" + self.fileName + ".pdf\n" + "Y \n" + self.fileNameSolve + ".pdf"
            messagebox.showinfo(title="Informacion", message=message)
            return self.fileName, self.fileNameSolve, self.resolver
        else:
            self.fileName = self.textbox.get('1.0', tk.END)
            message = "Archivo generado: \n" + self.fileName + ".pdf\n" 
            messagebox.showinfo(title="Informacion", message=message)
            return self.fileName, self.fileNameSolve, self.resolver

        
