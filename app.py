import tkinter as tk
from tkinter import messagebox
import sqlite3

class Contato:
    def __init__(self, nome, telefone, email, favorito=False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

class Agenda:
    def __init__(self):
        self.conexao = sqlite3.connect("agenda.db")
        self.cursor = self.conexao.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS contatos (
                                id INTEGER PRIMARY KEY,
                                nome TEXT NOT NULL,
                                telefone TEXT NOT NULL,
                                email TEXT NOT NULL,
                                favorito BOOLEAN NOT NULL)''')
        self.conexao.commit()

    def adicionar_contato(self, contato):
        self.cursor.execute("INSERT INTO contatos (nome, telefone, email, favorito) VALUES (?, ?, ?, ?)", 
                            (contato.nome, contato.telefone, contato.email, contato.favorito))
        self.conexao.commit()

    def obter_contatos(self):
        self.cursor.execute("SELECT * FROM contatos")
        return self.cursor.fetchall()

    def editar_contato(self, indice, nome, telefone, email):
        self.cursor.execute("UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE id = ?", 
                            (nome, telefone, email, indice))
        self.conexao.commit()

    def marcar_desmarcar_favorito(self, indice):
        self.cursor.execute("SELECT favorito FROM contatos WHERE id = ?", (indice,))
        favorito = self.cursor.fetchone()[0]
        novo_status = not favorito
        self.cursor.execute("UPDATE contatos SET favorito = ? WHERE id = ?", (novo_status, indice))
        self.conexao.commit()

    def mostrar_favoritos(self):
        self.cursor.execute("SELECT * FROM contatos WHERE favorito = 1")
        return self.cursor.fetchall()

    def apagar_contato(self, indice):
        self.cursor.execute("DELETE FROM contatos WHERE id = ?", (indice,))
        self.conexao.commit()

class CustomDialog(tk.Toplevel):
    def __init__(self, parent, title=None, prompt=""):
        super().__init__(parent)
        self.transient(parent)
        if title:
            self.title(title)
        self.result = None
        self.geometry("300x150")
        self.resizable(False, False)

        self.label = tk.Label(self, text=prompt, pady=10)
        self.label.pack()

        self.entry = tk.Entry(self, width=30)
        self.entry.pack(pady=5)

        self.buttonbox = tk.Frame(self)
        self.buttonbox.pack(pady=10)

        self.ok_button = tk.Button(self.buttonbox, text="OK", width=10, command=self.on_ok)
        self.ok_button.pack(side=tk.LEFT, padx=5)

        self.cancel_button = tk.Button(self.buttonbox, text="Cancel", width=10, command=self.on_cancel)
        self.cancel_button.pack(side=tk.RIGHT, padx=5)

        self.entry.focus_set()
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.on_cancel)
        self.wait_window(self)

    def on_ok(self, event=None):
        self.result = self.entry.get()
        self.destroy()

    def on_cancel(self, event=None):
        self.result = None
        self.destroy()

class App:
    def __init__(self, root):
        self.agenda = Agenda()
        self.root = root
        self.root.title("Agenda de Contatos")
        
        self.menu_frame = tk.Frame(root, padx=10, pady=10)
        self.menu_frame.pack(padx=10, pady=10)

        self.label = tk.Label(self.menu_frame, text="Menu", font=("Roboto", 14, "bold"))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        button_font = ("Roboto", 12)
        button_padx = 20
        button_pady = 5

        self.add_button = tk.Button(self.menu_frame, text="Adicionar contato", command=self.adicionar_contato, font=button_font, padx=button_padx, pady=button_pady)
        self.add_button.grid(row=1, column=0, pady=5)

        self.view_button = tk.Button(self.menu_frame, text="Visualizar lista de contatos", command=self.mostrar_contatos, font=button_font, padx=button_padx, pady=button_pady)
        self.view_button.grid(row=1, column=1, pady=5)

        self.edit_button = tk.Button(self.menu_frame, text="Editar contato", command=self.editar_contato, font=button_font, padx=button_padx, pady=button_pady)
        self.edit_button.grid(row=2, column=0, pady=5)

        self.favorite_button = tk.Button(self.menu_frame, text="Marcar/Desmarcar favorito", command=self.marcar_favorito, font=button_font, padx=button_padx, pady=button_pady)
        self.favorite_button.grid(row=2, column=1, pady=5)

        self.view_favorites_button = tk.Button(self.menu_frame, text="Ver favoritos", command=self.mostrar_favoritos, font=button_font, padx=button_padx, pady=button_pady)
        self.view_favorites_button.grid(row=3, column=0, pady=5)

        self.delete_button = tk.Button(self.menu_frame, text="Apagar contato", command=self.apagar_contato, font=button_font, padx=button_padx, pady=button_pady)
        self.delete_button.grid(row=3, column=1, pady=5)

    def adicionar_contato(self):
        nome = CustomDialog(self.root, title="Adicionar Contato", prompt="Nome do contato:").result
        telefone = CustomDialog(self.root, title="Adicionar Contato", prompt="Telefone do contato:").result
        email = CustomDialog(self.root, title="Adicionar Contato", prompt="Email do contato:").result
        if nome and telefone and email:
            self.agenda.adicionar_contato(Contato(nome, telefone, email))
            messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")

    def mostrar_contatos(self):
        contatos = self.agenda.obter_contatos()
        if not contatos:
            contatos_str = "Não há contatos cadastrados."
        else:
            contatos_str = ""
            for i, contato in enumerate(contatos, start=1):
                contatos_str += f"{i}. {contato[1]} - {contato[2]} - {contato[3]} - {'Favorito' if contato[4] else ''}\n"
        messagebox.showinfo("Lista de Contatos", contatos_str)

    def editar_contato(self):
        indice = CustomDialog(self.root, title="Editar Contato", prompt="Índice do contato a ser editado:").result
        if indice is not None and indice.isdigit() and 0 < int(indice) <= len(self.agenda.obter_contatos()):
            nome = CustomDialog(self.root, title="Editar Contato", prompt="Novo nome do contato:").result
            telefone = CustomDialog(self.root, title="Editar Contato", prompt="Novo telefone do contato:").result
            email = CustomDialog(self.root, title="Editar Contato", prompt="Novo email do contato:").result
            if nome and telefone and email:
                self.agenda.editar_contato(int(indice), nome, telefone, email)
                messagebox.showinfo("Sucesso", "Contato editado com sucesso!")
            else:
                messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
        else:
            messagebox.showerror("Erro", "Índice inválido.")

    def marcar_favorito(self):
        indice = CustomDialog(self.root, title="Marcar/Desmarcar Favorito", prompt="Índice do contato a ser marcado/desmarcado como favorito:").result
        if indice is not None and indice.isdigit() and 0 < int(indice) <= len(self.agenda.obter_contatos()):
            self.agenda.marcar_desmarcar_favorito(int(indice))
            messagebox.showinfo("Sucesso", "Contato marcado/desmarcado como favorito com sucesso!")
        else:
            messagebox.showerror("Erro", "Índice inválido.")

    def mostrar_favoritos(self):
        favoritos = self.agenda.mostrar_favoritos()
        if not favoritos:
            favoritos_str = "Não há contatos favoritos."
        else:
            favoritos_str = ""
            for i, contato in enumerate(favoritos, start=1):
                favoritos_str += f"{i}. {contato[1]} - {contato[2]} - {contato[3]}\n"
        messagebox.showinfo("Contatos Favoritos", favoritos_str)

    def apagar_contato(self):
        indice = CustomDialog(self.root, title="Apagar Contato", prompt="Índice do contato a ser apagado:").result
        if indice is not None and indice.isdigit() and 0 < int(indice) <= len(self.agenda.obter_contatos()):
            self.agenda.apagar_contato(int(indice))
            messagebox.showinfo("Sucesso", "Contato apagado com sucesso!")
        else:
            messagebox.showerror("Erro", "Índice inválido.")

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
