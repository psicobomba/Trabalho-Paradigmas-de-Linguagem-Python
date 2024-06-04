#Calculadora de IMC Python
#Import do tkinter
import tkinter as tk
from tkinter import messagebox
#Definindo Calculadora
class BMICalculator:
    #Inicializando o Estado da Calculadora
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")
        self.create_widgets()
    #Criando os Widgets
    def create_widgets(self):
        # Labels
        self.label_height = tk.Label(self.root, text="Altura (m):")
        self.label_height.grid(row=0, column=0, padx=10, pady=10)
        
        self.label_weight = tk.Label(self.root, text="Peso (kg):")
        self.label_weight.grid(row=1, column=0, padx=10, pady=10)
        
        self.label_result = tk.Label(self.root, text="IMC:")
        self.label_result.grid(row=3, column=0, padx=10, pady=10)

        #Entradas
        self.entry_height = tk.Entry(self.root)
        self.entry_height.grid(row=0, column=1, padx=10, pady=10)
        
        self.entry_weight = tk.Entry(self.root)
        self.entry_weight.grid(row=1, column=1, padx=10, pady=10)
        
        self.label_bmi_value = tk.Label(self.root, text="")
        self.label_bmi_value.grid(row=3, column=1, padx=10, pady=10)

        #Botões
        self.calculate_button = tk.Button(self.root, text="Calcular IMC", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    #Função para calcular o IMC
    def calculate_bmi(self):
        try:
            height = float(self.entry_height.get())
            weight = float(self.entry_weight.get())
            bmi = weight / (height ** 2)
            self.label_bmi_value.config(text=f"{bmi:.2f}")
            self.show_bmi_category(bmi)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira apenas valores válidos para altura e peso.")

    #Função para mostrar a categoria da IMC
    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            category = "Peso normal"
        elif 25 <= bmi < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        messagebox.showinfo("Categoria de IMC", f"Seu IMC é {bmi:.2f}. Categoria: {category}")

#Executando o Programa Principal
if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()