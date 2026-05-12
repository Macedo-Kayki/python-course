import tkinter as tk

class MeuApp:

    def __init__(self, master):
        self.master = master
        master.geometry("300x200")
        self.frame1 = tk.Frame(bg="yellow")
        self.frame2 = tk.Frame(bg="brown")
        self.etiquetandoa()
        self.etiquetandob()
        self.caixadetexto()
        self.botao()
        self.backbutton()
        self.frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    def etiquetandoa(self):
        self.label = tk.Label(
            self.frame1,
            text="Brincando com tkinter",
            bg="black",
            fg="red",
            width="25",
            font=("Arial", 12, "bold")
        )
        self.label.pack(expand=True, fill=tk.X)
    
    def etiquetandob(self):
        self.label = tk.Label(
            self.frame2,
            text="Tkinter",
            fg="black",
            bg="red",
            width="25",
            font=("Arial", 12, "bold"),
        )
        self.label.pack(expand=True, fill=tk.X)
        self.label.place(x=50, y=70)

    def botao(self):
        self.botao = tk.Button(
            self.frame1,
            text="Tela 2",
            width="35",
            height="2",
            bg="cyan",
            fg="white",
            command=lambda: self.trocarframe(self.frame1, self.frame2)
        )
        self.botao.pack()
    
    def backbutton(self):
        self.backbutton = tk.Button(
            self.frame2,
            text="VOLTAR",
            bg="green",
            fg="pink",
            command=lambda: self.trocarframe(self.frame2, self.frame1)
        )
        self.backbutton.pack()
    
    def caixadetexto(self):
        self.caixadetexto = tk.Entry(
            self.frame1,
            bg="blue",
            fg="yellow"
        )
        self.caixadetexto.pack(pady=20)
    
    def trocarframe(self, frame_sair, frame_entrar):
        frame_sair.pack_forget()
        frame_entrar.pack(fill="both", expand="True")


if __name__ == "__main__":
    root = tk.Tk()
    app = MeuApp(root)
    root.mainloop()