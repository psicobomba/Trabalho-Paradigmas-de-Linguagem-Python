#Cronômetro Python
#Instalando a bliblioteca Tkinter ao Python
import tkinter as tk
#Definindo a classe Cronômetro
class Stopwatch:
#Inicializando o Estado do Cronômetro
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cronômetro")
        #Adicionando a contagem de tempo
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        self.time_label = tk.Label(self.root, text=self.format_time(), font=("Helvetica", 48))
        self.time_label.pack()
#Adicionando os botões
        self.start_button = tk.Button(self.root, text="Iniciar", command=self.start)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.root, text="Parar", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(self.root, text="Resetar", command=self.reset)
        self.reset_button.pack(side=tk.LEFT)
#Formatando o tempo do cronômetro
    def format_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
#Atualizando o tempo do cronômetro
    def update_time(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
                if self.minutes == 60:
                    self.minutes = 0
                    self.hours += 1

            self.time_label.config(text=self.format_time())
            self.root.after(1000, self.update_time)
#Função de começar
    def start(self):
        if not self.running:
            self.running = True
            self.update_time()
#Função para parar o cronômetro
    def stop(self):
        if self.running:
            self.running = False
#Função para resetar o cronômetro
    def reset(self):
        if not self.running:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
            self.time_label.config(text=self.format_time())

# Executando o loop principal
if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.root.mainloop()