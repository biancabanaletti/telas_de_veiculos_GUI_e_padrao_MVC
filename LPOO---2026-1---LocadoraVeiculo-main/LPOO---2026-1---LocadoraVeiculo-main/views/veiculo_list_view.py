import tkinter as tk
from tkinter import ttk, messagebox
from model.VeiculoFactory import VeiculoFactory 

class VeiculoListView:
    def __init__(self, root):
        self.root = root
        self.root.title("Painel de Veículos - Locadora") 
        self.root.geometry("900x450") 
        
        self.lista_objetos_veiculos = [] #lista que armazena os objetos veículo (camada model)

        self.lbl_titulo = tk.Label(self.root, text="Veículos Cadastrados", font=("Arial", 12, "bold"), pady=10) 
        self.lbl_titulo.pack() 

        self.colunas = ("placa", "tipo", "categoria", "taxa")
        self.tabela = ttk.Treeview(self.root, columns=self.colunas, show='headings') #tabela para exibir os veículos cadastrados (view)
        
        self.tabela.heading("placa", text="Placa")
        self.tabela.heading("tipo", text="Tipo")
        self.tabela.heading("categoria", text="Categoria")
        self.tabela.heading("taxa", text="Taxa Diária (R$)")
        self.tabela.pack(fill=tk.BOTH, expand=True, padx=10)

        self.frame_botoes = tk.Frame(self.root, pady=15)
        self.frame_botoes.pack(side=tk.BOTTOM)

        tk.Button(self.frame_botoes, text="Novo", width=12, command=self.abrir_tela_cadastro).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_botoes, text="Ver Informações", width=15, command=self.detalhar_veiculo).pack(side=tk.LEFT, padx=5)       
        tk.Button(self.frame_botoes, text="Remover", width=12, bg="red", fg="white", command=self.excluir_veiculo).pack(side=tk.LEFT, padx=5)

    def detalhar_veiculo(self):
        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showwarning("Seleção", "Selecione um veículo na tabela!")
            return
        
        item_index = self.tabela.index(selecionado)
        veiculo_obj = self.lista_objetos_veiculos[item_index]

        mensagem = veiculo_obj.exibir_dados()
        messagebox.showinfo("Dados do Veículo", mensagem) 

    def excluir_veiculo(self):
        selecionado = self.tabela.selection()
        if selecionado:
            index = self.tabela.index(selecionado)
            self.lista_objetos_veiculos.pop(index) #remove do model
            self.tabela.delete(selecionado) #remove do view
            messagebox.showinfo("Sucesso", "Veículo removido!")

    def abrir_tela_cadastro(self): #cria uma nova janela para cadastro de veículo e essa janela é independente da principal
        self.janela_cad = tk.Toplevel(self.root) #janela secundária
        self.janela_cad.title("Cadastro de Novo Veículo")
        self.janela_cad.geometry("350x450")
        self.janela_cad.grab_set()

        #componentes do formulário
        tk.Label(self.janela_cad, text="Placa:").pack(pady=5)
        self.input_placa = tk.Entry(self.janela_cad) 
        self.input_placa.pack()

        tk.Label(self.janela_cad, text="Tipo do Veículo:").pack(pady=5)
        self.combo_tipo = ttk.Combobox(self.janela_cad, values=["Carro", "Motorhome"], state="readonly") 
        self.combo_tipo.pack()

        tk.Label(self.janela_cad, text="Categoria:").pack(pady=5)
        self.combo_cat = ttk.Combobox(self.janela_cad, values=["ECONOMICO", "EXECUTIVO"], state="readonly") 
        self.combo_cat.pack()

        tk.Label(self.janela_cad, text="Taxa Diária:").pack(pady=5)
        self.input_taxa = tk.Entry(self.janela_cad)
        self.input_taxa.pack()

        #botão de salvar
        tk.Button(self.janela_cad, text="Salvar Veículo", bg="green", fg="white", 
                  command=self.processar_cadastro).pack(pady=20)

    def processar_cadastro(self):
        #captura via .get()
        p = self.input_placa.get()
        t = self.combo_tipo.get().lower()
        c = self.combo_cat.get()
        tx = self.input_taxa.get()

        if not (p and t and c and tx):
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        try:
            taxa_num = float(tx)
 
            novo_v = VeiculoFactory.criar_veiculo(t, p, c, taxa_num, 0.0)

            #att sistema e tela
            self.lista_objetos_veiculos.append(novo_v)
            self.tabela.insert("", tk.END, values=(p, t.capitalize(), c, f"{taxa_num:.2f}"))

            self.janela_cad.destroy() #fecha tela
            messagebox.showinfo("Sucesso", "Veículo cadastrado!")

        except ValueError: #garante que a taxa seja numérica
            messagebox.showerror("Erro", "Taxa deve ser um número!")

if __name__ == "__main__":
    root = tk.Tk()
    app = VeiculoListView(root)
    root.mainloop()

#view: tela de listagem de veículos
#responsável pela interface gráfica (Tkinter)
#interage com a camada model através da VeiculoFactory
#padrão utilizado: MVC (Model-View-Controller)