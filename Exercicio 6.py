#Lista de tarefas Python

#instalando tkinter
import tkinter as tk
from tkinter import messagebox
#Criando a classe Principal do aplicativo
class ToDoListApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")
        
        # Elementos da interface
        self.label = tk.Label(root, text="Digite uma tarefa:")
        self.label.pack(pady=5)
        
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=5)
        
        self.add_button = tk.Button(root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.tasks_listbox = tk.Listbox(root, width=50, height=10)
        self.tasks_listbox.pack(pady=5)
        
        self.remove_button = tk.Button(root, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.pack(pady=5)
        
        self.tasks = []
    #Atualizando a lista de tarefas
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vazia", "Digite uma tarefa para adicionar.")
    #Defenindo função para remover tarefas
    def remove_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Nenhuma Seleção", "Selecione uma tarefa para remover.")
    #Função para atulizar a lista de tarefas
    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)
#Configuração do loop principal
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()