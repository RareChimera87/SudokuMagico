

import tkinter as tk
from tkinter import messagebox

class Gui:
    def __init__(self, callback=None):
        self.resolver = False
        self.fileName = ""
        self.fileNameSolve = ""
        self.dificultad = 1
        self.generateCallback = callback
        self.caracteresProhibidos = r'\/:*?"<>|'

        self.root = tk.Tk()

        self.root.geometry("500x500")

        self.root.title("Generador de Sudokus Instantaneo")

        self.label = tk.Label(self.root, text="Genera tu sudoku ya", font=('Arial', 20))
        self.label.pack(padx=10, pady=10)

        self.label = tk.Label(self.root, text="Pon el nombre de archivo a generar", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=1, width=20 ,font=('Arial', 18))
        self.textbox.pack(padx=10, pady=10)
        
        self.label = tk.Label(self.root, text="Escribe de 1 a 5 la dificultad, donde 1 es facil y 5 dificil", font=('Arial', 15))
        self.label.pack(padx=10, pady=10)

        self.textbox2 = tk.Text(self.root, height=1, width=1 ,font=('Arial', 18))
        self.textbox2.pack(padx=10, pady=10)

        self.checkState = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Generar archivo con respuesta", font=('Arial', 18), variable=self.checkState)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Generar", font=('Arial',20), command=self.Generar)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def Generar(self):
        textbox2 = self.textbox2.get('1.0', tk.END).strip()

        if textbox2:
            textbox2 = int(self.textbox2.get('1.0', tk.END).strip())
            if (1 <= int(self.textbox2.get('1.0', tk.END).strip()) <= 5): 
                self.dificultad = textbox2
                self.fileName = self.textbox.get('1.0', tk.END).strip()
                if not self.fileName or any(c in self.fileName for c in self.caracteresProhibidos):
                    messagebox.showinfo(title="ALERTA", message="Use Caracteres validos o Llenelo")
                else:
                    if self.checkState.get() == 1:
                        self.resolver = True
                        self.fileNameSolve = self.fileName + "Solve"
                        message = "Archivo generado: \n" + self.fileName + ".pdf\n" + "Y \n" + self.fileNameSolve + ".pdf"
                    else:
                        message = "Archivo generado: \n" + self.fileName + ".pdf\n" 
                    messagebox.showinfo(title="Informacion", message=message)

                    if self.generateCallback:

                        messagebox.showinfo(title="Informacion", message="Gracias por generar sudokus")
                        self.generateCallback(self.fileName, self.fileNameSolve, self.resolver, self.dificultad)
                        self.root.destroy()
            else:
                messagebox.showinfo(title="ALERTA", message="Elija un valor dentro del rango")

        else:
            messagebox.showinfo(title="ALERTA", message="Llenelo")
    

