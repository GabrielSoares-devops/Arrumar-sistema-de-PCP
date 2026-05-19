import tkinter as tk
from tkinter import ttk

def criar_interface_com_abas():
    # Define mock classes to use in headless environments
    class MockRoot:
        def title(self, x): pass
        def geometry(self, x): pass
        def mainloop(self): pass
        def pack(self, **kw): pass
        def destroy(self, *args): pass # Added *args to destroy
        def withdraw(self): pass
        def update_idletasks(self): pass
        def update(self): pass

    class MockNotebook:
        def __init__(self, parent): pass
        def pack(self, expand=False, fill='both'): pass
        def add(self, frame, text): pass

    class MockFrame:
        def __init__(self, parent): pass
        def pack(self, fill='both', expand=False): pass
        def grid_columnconfigure(self, col, weight): pass
        def grid_rowconfigure(self, row, weight): pass

    class MockLabel:
        def __init__(self, parent, **kwargs): pass
        def pack(self, **kw): pass

    _root = None
    _notebook_class = ttk.Notebook
    _frame_class = ttk.Frame
    _label_class = tk.Label
    _mock_mode = False # Flag to indicate if we are in mock mode

    try:
        _root = tk.Tk()
        _root.withdraw() # Hide the main window for headless environments if it tries to pop up
    except tk.TclError:
        # Handle case where Tkinter cannot initialize (e.g., no display)
        print("Tkinter.Tk() could not be initialized. Running in headless mode simulation.")
        _root = MockRoot() # Assign a mock instance to _root
        _notebook_class = MockNotebook # Assign mock class to _notebook_class
        _frame_class = MockFrame     # Assign mock class to _frame_class
        _label_class = MockLabel     # Assign mock class to _label_class
        _mock_mode = True # Set mock mode to True

    root = _root # Use the actual or mock root instance
    root.title("Sistema de Gerenciamento de Produção e Estoque")
    root.geometry("800x600")

    # 2. Cria uma instância de ttk.Notebook (or MockNotebook)
    notebook = _notebook_class(root)
    notebook.pack(expand=True, fill='both')

    # 3. Cria os frames para cada aba (or MockFrame)
    frame_ordens = _frame_class(notebook)
    frame_pecas = _frame_class(notebook)
    frame_estoque = _frame_class(notebook)
    frame_relatorios = _frame_class(notebook)

    # Empacota os frames para que preencham o notebook
    frame_ordens.pack(fill='both', expand=True)
    frame_pecas.pack(fill='both', expand=True)
    frame_estoque.pack(fill='both', expand=True)
    frame_relatorios.pack(fill='both', expand=True)

    # 4. Adiciona cada frame ao ttk.Notebook como uma aba
    notebook.add(frame_ordens, text='Ordens de Produção')
    notebook.add(frame_pecas, text='Peças/DXF')
    notebook.add(frame_estoque, text='Estoque de Chapas')
    notebook.add(frame_relatorios, text='Relatórios e Exportação')

    # 5. Adiciona um Label simples a cada frame para visualização
    # Call criar_aba_ordens_producao to populate frame_ordens
    criar_aba_ordens_producao(frame_ordens, mock_mode=_mock_mode)
    # Call criar_aba_pecas_dxf to populate frame_pecas
    criar_aba_pecas_dxf(frame_pecas, mock_mode=_mock_mode)
    # Call criar_aba_estoque_chapas to populate frame_estoque
    criar_aba_estoque_chapas(frame_estoque, mock_mode=_mock_mode)
    _label_class(frame_relatorios, text="Conteúdo da Aba de Relatórios e Exportação").pack(pady=20, padx=20)

    return root

# Chama a função para configurar a interface
janela_principal = criar_interface_com_abas()

# Comenta a linha root.mainloop() pois estamos em um ambiente headless (sem display)
# Se você estivesse executando em um ambiente gráfico, descomentaria a linha abaixo:
# if janela_principal and isinstance(janela_principal, tk.Tk):
#     janela_principal.mainloop()

print("A estrutura da interface com abas Tkinter foi criada e estaria pronta para execução em um ambiente gráfico. \n`root.mainloop()` foi comentado para evitar erros em ambientes sem display.")


import tkinter as tk

def configurar_janela_principal():
    # 1. Cria a janela principal (esta linha causaria um erro em ambientes sem display)
    # Em um ambiente com display, você faria:
    # root = tk.Tk()
    # E então configuraria a janela.

    print("Função configurar_janela_principal definida. Note que tk.Tk() não pode ser instanciado e exibido diretamente em ambientes headless (sem display) como este.")
    print("Para testar visualmente, este código precisaria ser executado em um ambiente com servidor X ou ser adaptado para ferramentas como `Xvfb`.")

    # Apenas para demonstrar a estrutura da configuração da janela:
    # Se 'root' existisse, você definiria:
    # root.title("Sistema de Gerenciamento de Produção e Estoque")
    # root.geometry("800x600")
    # return root

    # Retorna None pois a janela não pode ser criada neste ambiente
    return None

# Chama a função para configurar a janela.
# Comentado para evitar o TclError em ambientes headless (sem display).
# Em um ambiente com display, você descomentaria esta linha e, opcionalmente, root.mainloop().
# janela_principal = configurar_janela_principal()

print("A estrutura básica da função de configuração da janela Tkinter foi definida, mas a execução direta foi prevenida devido à falta de um display gráfico.")


import tkinter as tk
from tkinter import ttk

def criar_aba_pecas_dxf(parent_frame, mock_mode=False):
    # Mock classes for headless environment
    class MockEntry:
        def __init__(self, parent, textvariable=None, **kwargs):
            self.textvariable = textvariable
            self.value = ""
        def get(self): return self.textvariable.get() if self.textvariable else self.value
        def grid(self, **kwargs): pass

    class MockButton:
        def __init__(self, parent, text, command, **kwargs): pass
        def grid(self, **kwargs): pass

    class MockText:
        def __init__(self, parent, **kwargs):
            self.content = ""
            self.state = 'normal'
        def grid(self, **kwargs): pass
        def insert(self, index, text): self.content += text
        def delete(self, index1, index2): self.content = ""
        def configure(self, state=None): self.state = state

    class MockListbox:
        def __init__(self, parent, **kwargs): pass
        def grid(self, **kwargs): pass
        def insert(self, index, item): pass
        def yview_set(self, *args): pass
        def yview(self, *args): pass
        def config(self, **kwargs): pass

    class MockScrollbar:
        def __init__(self, parent, command=None, **kwargs): pass
        def grid(self, **kwargs): pass
        def config(self, command=None): pass
        def set(self, *args): pass # Added set method

    class MockStringVar:
        def __init__(self, value=""): self._value = value
        def get(self): return self._value
        def set(self, value): self._value = value

    class MockLabel:
        def __init__(self, parent, **kwargs): pass
        def grid(self, **kwargs): pass

    # Conditional assignment of Tkinter widgets or their mock counterparts
    Entry = tk.Entry if not mock_mode else MockEntry
    Button = tk.Button if not mock_mode else MockButton
    Text = tk.Text if not mock_mode else MockText
    Listbox = tk.Listbox if not mock_mode else MockListbox
    Scrollbar = ttk.Scrollbar if not mock_mode else MockScrollbar
    StringVar = tk.StringVar if not mock_mode else MockStringVar
    Label = tk.Label if not mock_mode else MockLabel # Add Label to conditional assignment

    # Input variables
    op_id_var = StringVar()
    nome_peca_var = StringVar()
    caminho_dxf_var = StringVar()
    quantidade_var = StringVar()

    # Feedback text widget
    feedback_text_widget = None

    def inserir_peca_dxf_action():
        op_id = op_id_var.get()
        nome_peca = nome_peca_var.get()
        caminho_dxf = caminho_dxf_var.get()
        quantidade = quantidade_var.get()

        if feedback_text_widget:
            feedback_text_widget.configure(state='normal')
            feedback_text_widget.delete('1.0', tk.END) # Clear previous messages

        print(f"Tentando inserir peça: OP ID={op_id}, Nome='{nome_peca}', DXF='{caminho_dxf}', Qtd={quantidade}")
        # Placeholder for actual database insertion logic from `inserir_peca_dxf`
        if not mock_mode and feedback_text_widget:
            feedback_text_widget.insert(tk.END, f"Peça '{nome_peca}' simulada para OP ID {op_id}.\n")
        elif mock_mode:
            print(f"[Mock Mode] Peça '{nome_peca}' simulada para OP ID {op_id}.\n")

        if feedback_text_widget:
            feedback_text_widget.configure(state='disabled')

        # Clear input fields (optional)
        op_id_var.set("")
        nome_peca_var.set("")
        caminho_dxf_var.set("")
        quantidade_var.set("")


    # --- Widgets for 'Peças/DXF' Tab ---
    row_idx = 0

    Label(parent_frame, text="ID da Ordem de Produção:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=op_id_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Nome da Peça:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=nome_peca_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Caminho do DXF:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=caminho_dxf_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Quantidade:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=quantidade_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Button(parent_frame, text="Inserir Peça/DXF", command=inserir_peca_dxf_action).grid(row=row_idx, column=0, columnspan=2, pady=10)
    row_idx += 1

    # Feedback Area
    feedback_text_widget = Text(parent_frame, height=5, width=60, state='disabled')
    feedback_text_widget.grid(row=row_idx, column=0, columnspan=2, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Peças Cadastradas:").grid(row=row_idx, column=0, columnspan=2, padx=5, pady=5, sticky='w')
    row_idx += 1

    # Listbox for registered pieces
    listbox_pecas = Listbox(parent_frame, height=10, width=60)
    listbox_pecas.grid(row=row_idx, column=0, columnspan=1, padx=5, pady=5, sticky='nsew')

    scrollbar_pecas = Scrollbar(parent_frame, orient="vertical", command=listbox_pecas.yview)
    scrollbar_pecas.grid(row=row_idx, column=1, padx=(0,5), pady=5, sticky='ns')
    listbox_pecas.config(yscrollcommand=scrollbar_pecas.set)

    # Configure grid weights to allow widgets to resize
    parent_frame.grid_columnconfigure(1, weight=1)
    parent_frame.grid_rowconfigure(row_idx, weight=1)

    print("Função `criar_aba_pecas_dxf` definida e componentes da aba 'Peças/DXF' configurados (ou simulados em modo headless).")


# --- Teste da função em modo headless --- (para demonstração)
# Assumindo que 'janela_principal' e seus frames já foram criados pelo passo anterior.
# Em um ambiente real com display, você passaria o frame correto do notebook.

# Simulate parent_frame for testing in headless environment
class MockFrameForTab:
    def __init__(self, master=None):
        # Add a mock tk attribute to avoid AttributeError when real tk widgets are instantiated
        # However, the preferred fix is to mock the tk.Label itself.
        pass
    def grid(self, **kwargs): pass
    def grid_columnconfigure(self, col, weight):
        print(f"[MockFrame] Configurando coluna {col} com peso {weight}")
    def grid_rowconfigure(self, row, weight):
        print(f"[MockFrame] Configurando linha {row} com peso {weight}")


mock_tab_frame = MockFrameForTab()

criar_aba_pecas_dxf(mock_tab_frame, mock_mode=True)

import tkinter as tk
from tkinter import ttk
import sqlite3
import pandas as pd

def criar_aba_estoque_chapas(parent_frame, mock_mode=False):
    # Mock classes for headless environment (copied for self-containment of this function)
    class MockEntry:
        def __init__(self, parent, textvariable=None, **kwargs):
            self.textvariable = textvariable
            self.value = ""
        def get(self): return self.textvariable.get() if self.textvariable else self.value
        def grid(self, **kwargs): pass

    class MockButton:
        def __init__(self, parent, text, command, **kwargs): pass
        def grid(self, **kwargs): pass

    class MockText:
        def __init__(self, parent, **kwargs):
            self.content = ""
            self.state = 'normal'
        def grid(self, **kwargs): pass
        def insert(self, index, text): self.content += text
        def delete(self, index1, index2): self.content = ""
        def configure(self, state=None): self.state = state

    class MockListbox:
        def __init__(self, parent, **kwargs): pass
        def grid(self, **kwargs): pass
        def insert(self, index, item): pass
        def delete(self, first, last=None): pass # Added delete for listbox clearing
        def yview_set(self, *args): pass
        def yview(self, *args): pass
        def config(self, **kwargs): pass

    class MockScrollbar:
        def __init__(self, parent, command=None, **kwargs): pass
        def grid(self, **kwargs): pass
        def config(self, command=None): pass
        def set(self, *args): pass

    class MockStringVar:
        def __init__(self, value=""): self._value = value
        def get(self): return self._value
        def set(self, value): self._value = value

    class MockLabel:
        def __init__(self, parent, **kwargs): pass
        def grid(self, **kwargs): pass

    # Conditional assignment of Tkinter widgets or their mock counterparts
    Entry = tk.Entry if not mock_mode else MockEntry
    Button = tk.Button if not mock_mode else MockButton
    Text = tk.Text if not mock_mode else MockText
    Listbox = tk.Listbox if not mock_mode else MockListbox
    Scrollbar = ttk.Scrollbar if not mock_mode else MockScrollbar
    StringVar = tk.StringVar if not mock_mode else MockStringVar
    Label = tk.Label if not mock_mode else MockLabel

    # Input variables
    codigo_var = StringVar()
    material_var = StringVar()
    espessura_var = StringVar()
    comprimento_var = StringVar()
    largura_var = StringVar()
    quantidade_disponivel_var = StringVar()

    # Feedback text widget
    feedback_text_widget = None
    listbox_chapas = None

    def adicionar_chapa_action():
        nonlocal feedback_text_widget, listbox_chapas
        codigo = codigo_var.get()
        material = material_var.get()
        espessura_str = espessura_var.get()
        comprimento_str = comprimento_var.get()
        largura_str = largura_var.get()
        quantidade_disponivel_str = quantidade_disponivel_var.get()

        if feedback_text_widget:
            feedback_text_widget.configure(state='normal')
            feedback_text_widget.delete('1.0', tk.END)

        if not codigo:
            if feedback_text_widget:
                feedback_text_widget.insert(tk.END, "Erro: O campo 'Código' não pode ser vazio.\n")
            print("Erro: O campo 'Código' não pode ser vazio.")
            if feedback_text_widget:
                feedback_text_widget.configure(state='disabled')
            return

        espessura = None
        comprimento = None
        largura = None
        quantidade_disponivel = None

        try:
            if espessura_str: espessura = float(espessura_str.replace(',', '.')) # Handle comma as decimal separator
            if comprimento_str: comprimento = float(comprimento_str.replace(',', '.'))
            if largura_str: largura = float(largura_str.replace(',', '.'))
            if quantidade_disponivel_str: quantidade_disponivel = int(quantidade_disponivel_str)
        except ValueError:
            if feedback_text_widget:
                feedback_text_widget.insert(tk.END, "Erro: Por favor, insira valores numéricos válidos.\n")
            print("Erro: Por favor, insira valores numéricos válidos.")
            if feedback_text_widget:
                feedback_text_widget.configure(state='disabled')
            return

        db_name = 'producao.db'
        conn = None
        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO chapas_estoque (
                    codigo, material, espessura, comprimento, largura, quantidade_disponivel
                )
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                codigo, material, espessura, comprimento, largura, quantidade_disponivel
            ))

            conn.commit()
            message = f"Chapa com código '{codigo}' adicionada ao estoque com sucesso!\n"
            if feedback_text_widget:
                feedback_text_widget.insert(tk.END, message)
            print(message.strip())

            # Clear input fields
            codigo_var.set("")
            material_var.set("")
            espessura_var.set("")
            comprimento_var.set("")
            largura_var.set("")
            quantidade_disponivel_var.set("")

            # Update the listbox with new data
            atualizar_listbox_chapas()

        except sqlite3.IntegrityError as e:
            message = f"Erro de integridade: o código '{codigo}' já existe.\n"
            if feedback_text_widget:
                feedback_text_widget.insert(tk.END, message)
            print(message.strip())
        except sqlite3.Error as e:
            message = f"Erro no banco de dados: {e}\n"
            if feedback_text_widget:
                feedback_text_widget.insert(tk.END, message)
            print(message.strip())
        except Exception as e:
            message = f"Erro inesperado: {e}\n"
            if feedback_text_widget:
                feedback_text_widget.insert(tk.END, message)
            print(message.strip())
        finally:
            if conn:
                conn.close()

        if feedback_text_widget:
            feedback_text_widget.configure(state='disabled')

    def atualizar_listbox_chapas():
        if listbox_chapas:
            listbox_chapas.delete(0, tk.END) # Clear existing items

            db_name = 'producao.db'
            conn = None
            try:
                conn = sqlite3.connect(db_name)
                df_chapas = pd.read_sql_query("SELECT id, codigo, material, espessura, comprimento, largura, quantidade_disponivel FROM chapas_estoque", conn)

                if not df_chapas.empty:
                    for index, row in df_chapas.iterrows():
                        # Format the display string for each sheet
                        display_str = (
                            f"ID: {row['id']} | Cód: {row['codigo']} | Mat: {row['material']} | "
                            f"Esp: {row['espessura']:.2f} | Comp: {row['comprimento']:.0f} | Larg: {row['largura']:.0f} | Qtd: {row['quantidade_disponivel']}"
                        )
                        if listbox_chapas:
                            listbox_chapas.insert(tk.END, display_str)

            except Exception as e:
                print(f"Erro ao carregar chapas para o listbox: {e}")
            finally:
                if conn:
                    conn.close()


    # --- Widgets for 'Estoque de Chapas' Tab ---
    row_idx = 0

    Label(parent_frame, text="Código:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=codigo_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Material:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=material_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Espessura (mm):").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=espessura_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Comprimento (mm):").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=comprimento_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Largura (mm):").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=largura_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Quantidade Disponível:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=quantidade_disponivel_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Button(parent_frame, text="Adicionar Chapa", command=adicionar_chapa_action).grid(row=row_idx, column=0, columnspan=2, pady=10)
    row_idx += 1

    # Feedback Area
    feedback_text_widget = Text(parent_frame, height=5, width=60, state='disabled')
    feedback_text_widget.grid(row=row_idx, column=0, columnspan=2, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Chapas em Estoque:").grid(row=row_idx, column=0, columnspan=2, padx=5, pady=5, sticky='w')
    row_idx += 1

    # Listbox for registered sheets
    listbox_chapas = Listbox(parent_frame, height=10, width=60)
    listbox_chapas.grid(row=row_idx, column=0, columnspan=1, padx=5, pady=5, sticky='nsew')

    scrollbar_chapas = Scrollbar(parent_frame, orient="vertical", command=listbox_chapas.yview)
    scrollbar_chapas.grid(row=row_idx, column=1, padx=(0,5), pady=5, sticky='ns')
    listbox_chapas.config(yscrollcommand=scrollbar_chapas.set)

    # Configure grid weights to allow widgets to resize
    parent_frame.grid_columnconfigure(1, weight=1)
    parent_frame.grid_rowconfigure(row_idx, weight=1)

    # Initial load of sheets into the listbox
    atualizar_listbox_chapas()

    print("Função `criar_aba_estoque_chapas` definida e componentes da aba 'Estoque de Chapas' configurados (ou simulados em modo headless).")


# --- Teste da função em modo headless --- (para demonstração)
# Simulate parent_frame for testing in headless environment
class MockFrameForStockTab:
    def __init__(self, master=None): pass
    def grid(self, **kwargs): pass
    def grid_columnconfigure(self, col, weight):
        print(f"[MockFrameForStockTab] Configurando coluna {col} com peso {weight}")
    def grid_rowconfigure(self, row, weight):
        print(f"[MockFrameForStockTab] Configurando linha {row} com peso {weight}")

mock_stock_tab_frame = MockFrameForStockTab()
criar_aba_estoque_chapas(mock_stock_tab_frame, mock_mode=True)


import tkinter as tk
from tkinter import ttk
import sqlite3
import pandas as pd

def criar_aba_ordens_producao(parent_frame, mock_mode=False):
    # Mock classes for headless environment (copied for self-containment of this function)
    class MockEntry:
        def __init__(self, parent, textvariable=None, **kwargs):
            self.textvariable = textvariable
            self.value = ""
        def get(self): return self.textvariable.get() if self.textvariable else self.value
        def grid(self, **kwargs): pass

    class MockButton:
        def __init__(self, parent, text, command, **kwargs): pass
        def grid(self, **kwargs): pass

    class MockText:
        def __init__(self, parent, **kwargs):
            self.content = ""
            self.state = 'normal'
        def grid(self, **kwargs): pass
        def insert(self, index, text): self.content += text
        def delete(self, index1, index2): self.content = ""
        def configure(self, state=None): self.state = state

    class MockListbox:
        def __init__(self, parent, **kwargs): pass
        def grid(self, **kwargs): pass
        def insert(self, index, item): pass
        def delete(self, first, last=None): pass
        def yview_set(self, *args): pass
        def yview(self, *args): pass
        def config(self, **kwargs): pass

    class MockScrollbar:
        def __init__(self, parent, command=None, **kwargs): pass
        def grid(self, **kwargs): pass
        def config(self, command=None): pass
        def set(self, *args): pass

    class MockStringVar:
        def __init__(self, value=""): self._value = value
        def get(self): return self._value
        def set(self, value): self._value = value

    class MockLabel:
        def __init__(self, parent, **kwargs): pass
        def grid(self, **kwargs): pass

    # Conditional assignment of Tkinter widgets or their mock counterparts
    Entry = tk.Entry if not mock_mode else MockEntry
    Button = tk.Button if not mock_mode else MockButton
    Text = tk.Text if not mock_mode else MockText
    Listbox = tk.Listbox if not mock_mode else MockListbox
    Scrollbar = ttk.Scrollbar if not mock_mode else MockScrollbar
    StringVar = tk.StringVar if not mock_mode else MockStringVar
    Label = tk.Label if not mock_mode else MockLabel

    # Input variables
    pedido_var = StringVar()
    data_emissao_var = StringVar()
    cliente_var = StringVar()
    descricao_var = StringVar()
    vendedor_var = StringVar()
    peso_var = StringVar()
    pecas_var = StringVar()
    espessura_var = StringVar()
    qualidade_var = StringVar()
    maquina_var = StringVar()
    tempo_estimado_var = StringVar()
    hr_progm_var = StringVar()
    desenho_var = StringVar()
    corte_var = StringVar()
    status_var = StringVar()
    prog_var = StringVar()

    # Feedback text widget and listbox reference
    feedback_text_widget = None
    listbox_ordens = None

    def inserir_ordem_producao_action():
        nonlocal feedback_text_widget, listbox_ordens
        pedido = pedido_var.get()
        data_emissao = data_emissao_var.get()
        cliente = cliente_var.get()
        descricao = descricao_var.get()
        vendedor = vendedor_var.get()
        peso_str = peso_var.get()
        pecas_str = pecas_var.get()
        espessura_str = espessura_var.get()
        qualidade = qualidade_var.get()
        maquina = maquina_var.get()
        tempo_estimado_str = tempo_estimado_var.get()
        hr_progm_str = hr_progm_var.get()
        desenho = desenho_var.get()
        corte = corte_var.get()
        status = status_var.get()
        prog = prog_var.get()

        if feedback_text_widget:
            feedback_text_widget.configure(state='normal')
            feedback_text_widget.delete('1.0', tk.END)

        if not pedido:
            message = "Erro: O campo 'Pedido' não pode ser vazio.\n"
            if feedback_text_widget: feedback_text_widget.insert(tk.END, message)
            print(message.strip())
            if feedback_text_widget: feedback_text_widget.configure(state='disabled')
            return

        peso = None
        pecas = None
        espessura = None
        tempo_estimado = None
        hr_progm = None

        try:
            if peso_str: peso = float(peso_str.replace(',', '.'))
            if pecas_str: pecas = int(pecas_str)
            if espessura_str: espessura = float(espessura_str.replace(',', '.'))
            if tempo_estimado_str: tempo_estimado = float(tempo_estimado_str.replace(',', '.'))
            if hr_progm_str: hr_progm = float(hr_progm_str.replace(',', '.'))
        except ValueError:
            message = "Erro: Por favor, insira valores numéricos válidos para Peso, Peças, Espessura, Tempo Estimado e HR Progm.\n"
            if feedback_text_widget: feedback_text_widget.insert(tk.END, message)
            print(message.strip())
            if feedback_text_widget: feedback_text_widget.configure(state='disabled')
            return

        db_name = 'producao.db'
        conn = None
        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO ordens_producao (
                    pedido, data_emissao, cliente, descricao, vendedor, peso,
                    pecas, espessura, qualidade, maquina, tempo_estimado,
                    hr_progm, desenho, corte, status, prog
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                pedido, data_emissao, cliente, descricao, vendedor, peso,
                pecas, espessura, qualidade, maquina, tempo_estimado,
                hr_progm, desenho, corte, status, prog
            ))

            conn.commit()
            message = f"Ordem de Produção '{pedido}' inserida com sucesso!\n"
            if feedback_text_widget: feedback_text_widget.insert(tk.END, message)
            print(message.strip())

            # Clear input fields
            pedido_var.set("")
            data_emissao_var.set("")
            cliente_var.set("")
            descricao_var.set("")
            vendedor_var.set("")
            peso_var.set("")
            pecas_var.set("")
            espessura_var.set("")
            qualidade_var.set("")
            maquina_var.set("")
            tempo_estimado_var.set("")
            hr_progm_var.set("")
            desenho_var.set("")
            corte_var.set("")
            status_var.set("")
            prog_var.set("")

            # Update the listbox with new data
            atualizar_listbox_ordens()

        except sqlite3.IntegrityError as e:
            message = f"Erro de integridade: o pedido '{pedido}' já existe.\n"
            if feedback_text_widget: feedback_text_widget.insert(tk.END, message)
            print(message.strip())
        except sqlite3.Error as e:
            message = f"Erro no banco de dados: {e}\n"
            if feedback_text_widget: feedback_text_widget.insert(tk.END, message)
            print(message.strip())
        except Exception as e:
            message = f"Erro inesperado: {e}\n"
            if feedback_text_widget: feedback_text_widget.insert(tk.END, message)
            print(message.strip())
        finally:
            if conn:
                conn.close()

        if feedback_text_widget: feedback_text_widget.configure(state='disabled')

    def atualizar_listbox_ordens():
        if listbox_ordens:
            listbox_ordens.delete(0, tk.END) # Clear existing items

            db_name = 'producao.db'
            conn = None
            try:
                conn = sqlite3.connect(db_name)
                df_ordens = pd.read_sql_query("SELECT id, pedido, cliente, status FROM ordens_producao", conn)

                if not df_ordens.empty:
                    for index, row in df_ordens.iterrows():
                        display_str = (
                            f"ID: {row['id']} | Pedido: {row['pedido']} | Cliente: {row['cliente']} | Status: {row['status']}"
                        )
                        if listbox_ordens:
                            listbox_ordens.insert(tk.END, display_str)

            except Exception as e:
                print(f"Erro ao carregar ordens de produção para o listbox: {e}")
            finally:
                if conn:
                    conn.close()


    # --- Widgets for 'Ordens de Produção' Tab ---
    row_idx = 0

    Label(parent_frame, text="Pedido:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=pedido_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Data de Emissão:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=data_emissao_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Cliente:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=cliente_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Descrição:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=descricao_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Vendedor:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=vendedor_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Peso (kg):").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=peso_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Peças:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=pecas_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Espessura (mm):").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=espessura_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Qualidade:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=qualidade_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Máquina:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=maquina_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Tempo Estimado (h):").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=tempo_estimado_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="HR Progm. (h):").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=hr_progm_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Desenho:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=desenho_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Corte:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=corte_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Status:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=status_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Prog:").grid(row=row_idx, column=0, padx=5, pady=5, sticky='w')
    Entry(parent_frame, textvariable=prog_var, width=40).grid(row=row_idx, column=1, padx=5, pady=5, sticky='we')
    row_idx += 1

    Button(parent_frame, text="Inserir Ordem de Produção", command=inserir_ordem_producao_action).grid(row=row_idx, column=0, columnspan=2, pady=10)
    row_idx += 1

    # Feedback Area
    feedback_text_widget = Text(parent_frame, height=5, width=60, state='disabled')
    feedback_text_widget.grid(row=row_idx, column=0, columnspan=2, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Ordens de Produção Cadastradas:").grid(row=row_idx, column=0, columnspan=2, padx=5, pady=5, sticky='w')
    row_idx += 1

    # Listbox for registered orders
    listbox_ordens = Listbox(parent_frame, height=10, width=60)
    listbox_ordens.grid(row=row_idx, column=0, columnspan=1, padx=5, pady=5, sticky='nsew')

    scrollbar_ordens = Scrollbar(parent_frame, orient="vertical", command=listbox_ordens.yview)
    scrollbar_ordens.grid(row=row_idx, column=1, padx=(0,5), pady=5, sticky='ns')
    listbox_ordens.config(yscrollcommand=scrollbar_ordens.set)

    # Configure grid weights to allow widgets to resize
    parent_frame.grid_columnconfigure(1, weight=1)
    parent_frame.grid_rowconfigure(row_idx, weight=1)

    # Initial load of orders into the listbox
    atualizar_listbox_ordens()

    print("Função `criar_aba_ordens_producao` definida e componentes da aba 'Ordens de Produção' configurados (ou simulados em modo headless).")


# --- Teste da função em modo headless --- (para demonstração)
class MockFrameForOPTab:
    def __init__(self, master=None): pass
    def grid(self, **kwargs): pass
    def grid_columnconfigure(self, col, weight):
        print(f"[MockFrameForOPTab] Configurando coluna {col} com peso {weight}")
    def grid_rowconfigure(self, row, weight):
        print(f"[MockFrameForOPTab] Configurando linha {row} com peso {weight}")

mock_op_tab_frame = MockFrameForOPTab()
criar_aba_ordens_producao(mock_op_tab_frame, mock_mode=True)

import tkinter as tk
from tkinter import ttk
import pandas as pd
import sqlite3

# Assuming these functions are defined elsewhere in the notebook
# from your previous steps.
# If they are not in scope, they would need to be imported or re-defined.

# Placeholder for gerar_relatorio_cortes_por_chapa if not in global scope
def gerar_relatorio_cortes_por_chapa_mock():
    print("Mock: Gerando relatório de cortes por chapa.")
    # Simulate some data for headless testing
    data = {'espessura': [10.0, 12.0], 'qualidade': ['A36', 'A572'], 'total_quantidade_utilizada': [5, 3]}
    return pd.DataFrame(data)

# Placeholder for gerar_relatorio_sucata if not in global scope
def gerar_relatorio_sucata_mock():
    print("Mock: Gerando relatório de sucata.")
    return 15.75 # Simulate a value

# Placeholder for exportar_para_excel if not in global scope
def exportar_para_excel_mock(table_name, filename):
    print(f"Mock: Exportando tabela '{table_name}' para '{filename}'.")
    return f"Dados da tabela '{table_name}' exportados com sucesso para '{filename}'."


def criar_aba_relatorios_exportacao(parent_frame, mock_mode=False):
    # Mock classes for headless environment
    class MockButton:
        def __init__(self, parent, text, command, **kwargs): pass
        def grid(self, **kwargs): pass

    class MockText:
        def __init__(self, parent, **kwargs):
            self.content = ""
            self.state = 'normal'
        def grid(self, **kwargs): pass
        def insert(self, index, text): self.content += text
        def delete(self, index1, index2): self.content = ""
        def configure(self, state=None): self.state = state

    class MockLabel:
        def __init__(self, parent, **kwargs): pass
        def grid(self, **kwargs): pass

    # Conditional assignment of Tkinter widgets or their mock counterparts
    Button = tk.Button if not mock_mode else MockButton
    Text = tk.Text if not mock_mode else MockText
    Label = tk.Label if not mock_mode else MockLabel

    # Feedback text widget
    feedback_text_widget = None
    relatorio_cortes_text = None
    relatorio_sucata_text = None

    def exibir_relatorios_action():
        nonlocal feedback_text_widget, relatorio_cortes_text, relatorio_sucata_text

        if feedback_text_widget:
            feedback_text_widget.configure(state='normal')
            feedback_text_widget.delete('1.0', tk.END)

        if relatorio_cortes_text:
            relatorio_cortes_text.configure(state='normal')
            relatorio_cortes_text.delete('1.0', tk.END)

        if relatorio_sucata_text:
            relatorio_sucata_text.configure(state='normal')
            relatorio_sucata_text.delete('1.0', tk.END)

        # Get reports
        if not mock_mode and 'gerar_relatorio_cortes_por_chapa' in globals():
            df_cortes = gerar_relatorio_cortes_por_chapa()
            total_sucata = gerar_relatorio_sucata()
        else:
            df_cortes = gerar_relatorio_cortes_por_chapa_mock()
            total_sucata = gerar_relatorio_sucata_mock()

        # Display cortes report
        if not df_cortes.empty:
            cortes_str = "Relatório de Cortes por Chapa:\n" + df_cortes.to_string(index=False)
            if relatorio_cortes_text: relatorio_cortes_text.insert(tk.END, cortes_str)
            print(cortes_str)
        else:
            cortes_str = "Nenhum dado encontrado para o relatório de cortes por chapa.\n"
            if relatorio_cortes_text: relatorio_cortes_text.insert(tk.END, cortes_str)
            print(cortes_str)

        # Display sucata report
        sucata_str = f"Total de Sucata Gerada: {total_sucata:.2f} kg\n"
        if relatorio_sucata_text: relatorio_sucata_text.insert(tk.END, sucata_str)
        print(sucata_str)

        if feedback_text_widget: feedback_text_widget.insert(tk.END, "Relatórios atualizados com sucesso.\n")

        if feedback_text_widget: feedback_text_widget.configure(state='disabled')
        if relatorio_cortes_text: relatorio_cortes_text.configure(state='disabled')
        if relatorio_sucata_text: relatorio_sucata_text.configure(state='disabled')

    def exportar_dados_action():
        nonlocal feedback_text_widget
        if feedback_text_widget:
            feedback_text_widget.configure(state='normal')
            feedback_text_widget.delete('1.0', tk.END)

        tables_to_export = ['ordens_producao', 'chapas_estoque', 'pecas_dxf', 'historico_corte']
        results = []
        for table in tables_to_export:
            filename = f'{table}.xlsx'
            if not mock_mode and 'exportar_para_excel' in globals():
                res = exportar_para_excel(table, filename)
            else:
                res = exportar_para_excel_mock(table, filename)
            results.append(res)
            if feedback_text_widget: feedback_text_widget.insert(tk.END, res + "\n")

        if feedback_text_widget: feedback_text_widget.configure(state='disabled')
        print("Processo de exportação concluído.")

    # --- Widgets for 'Relatórios e Exportação' Tab ---
    row_idx = 0

    Label(parent_frame, text="Relatórios de Produção e Estoque", font=("Arial", 14, "bold")).grid(row=row_idx, column=0, columnspan=2, pady=10)
    row_idx += 1

    # Button to generate and display reports
    Button(parent_frame, text="Gerar Relatórios", command=exibir_relatorios_action).grid(row=row_idx, column=0, columnspan=2, pady=5)
    row_idx += 1

    Label(parent_frame, text="Relatório de Cortes por Chapa:").grid(row=row_idx, column=0, columnspan=2, padx=5, pady=5, sticky='w')
    row_idx += 1
    relatorio_cortes_text = Text(parent_frame, height=8, width=70, state='disabled')
    relatorio_cortes_text.grid(row=row_idx, column=0, columnspan=2, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Relatório de Sucata:").grid(row=row_idx, column=0, columnspan=2, padx=5, pady=5, sticky='w')
    row_idx += 1
    relatorio_sucata_text = Text(parent_frame, height=2, width=70, state='disabled')
    relatorio_sucata_text.grid(row=row_idx, column=0, columnspan=2, padx=5, pady=5, sticky='we')
    row_idx += 1

    Label(parent_frame, text="Exportação de Dados para Excel", font=("Arial", 12, "bold")).grid(row=row_idx, column=0, columnspan=2, pady=10)
    row_idx += 1

    Button(parent_frame, text="Exportar Todas as Tabelas para Excel", command=exportar_dados_action).grid(row=row_idx, column=0, columnspan=2, pady=5)
    row_idx += 1

    # Feedback Area for export
    feedback_text_widget = Text(parent_frame, height=5, width=70, state='disabled')
    feedback_text_widget.grid(row=row_idx, column=0, columnspan=2, padx=5, pady=5, sticky='we')
    row_idx += 1

    # Configure grid weights to allow widgets to resize
    parent_frame.grid_columnconfigure(0, weight=1)
    parent_frame.grid_columnconfigure(1, weight=1)
    parent_frame.grid_rowconfigure(row_idx, weight=1) # Last row of content to expand

    # Call initial report generation on load
    exibir_relatorios_action()

    print("Função `criar_aba_relatorios_exportacao` definida e componentes da aba 'Relatórios e Exportação' configurados (ou simulados em modo headless).")

# --- Teste da função em modo headless --- (para demonstração)
class MockFrameForReportsTab:
    def __init__(self, master=None): pass
    def grid(self, **kwargs): pass
    def grid_columnconfigure(self, col, weight):
        print(f"[MockFrameForReportsTab] Configurando coluna {col} com peso {weight}")
    def grid_rowconfigure(self, row, weight):
        print(f"[MockFrameForReportsTab] Configurando linha {row} com peso {weight}")

mock_reports_tab_frame = MockFrameForReportsTab()
criar_aba_relatorios_exportacao(mock_reports_tab_frame, mock_mode=True)

import tkinter as tk
from tkinter import ttk

def criar_interface_com_abas():
    # Define mock classes to use in headless environments
    class MockRoot:
        def title(self, x): pass 
        def geometry(self, x): pass
        def mainloop(self): pass
        def pack(self, **kw): pass
        def destroy(self, *args): pass # Added *args to destroy
        def withdraw(self): pass
        def update_idletasks(self): pass
        def update(self): pass

    class MockNotebook:
        def __init__(self, parent): pass
        def pack(self, expand=False, fill='both'): pass
        def add(self, frame, text): pass

    class MockFrame:
        def __init__(self, parent): pass
        def pack(self, fill='both', expand=False): pass
        def grid_columnconfigure(self, col, weight): pass
        def grid_rowconfigure(self, row, weight): pass

    class MockLabel:
        def __init__(self, parent, **kwargs): pass
        def pack(self, **kw): pass

    _root = None
    _notebook_class = ttk.Notebook
    _frame_class = ttk.Frame
    _label_class = tk.Label
    _mock_mode = False # Flag to indicate if we are in mock mode

    try:
        _root = tk.Tk()
        _root.withdraw() # Hide the main window for headless environments if it tries to pop up
    except tk.TclError:
        # Handle case where Tkinter cannot initialize (e.g., no display)
        print("Tkinter.Tk() could not be initialized. Running in headless mode simulation.")
        _root = MockRoot() # Assign a mock instance to _root
        _notebook_class = MockNotebook # Assign mock class to _notebook_class
        _frame_class = MockFrame     # Assign mock class to _frame_class
        _label_class = MockLabel     # Assign mock class to _label_class
        _mock_mode = True # Set mock mode to True

    root = _root # Use the actual or mock root instance
    root.title("Sistema de Gerenciamento de Produção e Estoque")
    root.geometry("800x600")

    # 2. Cria uma instância de ttk.Notebook (or MockNotebook)
    notebook = _notebook_class(root)
    notebook.pack(expand=True, fill='both')

    # 3. Cria os frames para cada aba (or MockFrame)
    frame_ordens = _frame_class(notebook)
    frame_pecas = _frame_class(notebook)
    frame_estoque = _frame_class(notebook)
    frame_relatorios = _frame_class(notebook)

    # Empacota os frames para que preencham o notebook
    frame_ordens.pack(fill='both', expand=True)
    frame_pecas.pack(fill='both', expand=True)
    frame_estoque.pack(fill='both', expand=True)
    frame_relatorios.pack(fill='both', expand=True)

    # 4. Adiciona cada frame ao ttk.Notebook como uma aba
    notebook.add(frame_ordens, text='Ordens de Produção')
    notebook.add(frame_pecas, text='Peças/DXF')
    notebook.add(frame_estoque, text='Estoque de Chapas')
    notebook.add(frame_relatorios, text='Relatórios e Exportação')

    # 5. Adiciona um Label simples a cada frame para visualização
    # Call criar_aba_ordens_producao to populate frame_ordens
    criar_aba_ordens_producao(frame_ordens, mock_mode=_mock_mode)
    # Call criar_aba_pecas_dxf to populate frame_pecas
    criar_aba_pecas_dxf(frame_pecas, mock_mode=_mock_mode)
    # Call criar_aba_estoque_chapas to populate frame_estoque
    criar_aba_estoque_chapas(frame_estoque, mock_mode=_mock_mode)
    # Call criar_aba_relatorios_exportacao to populate frame_relatorios
    criar_aba_relatorios_exportacao(frame_relatorios, mock_mode=_mock_mode)

    return root

# Chama a função para configurar a interface
janela_principal = criar_interface_com_abas()

# Comenta a linha root.mainloop() pois estamos em um ambiente headless (sem display)
# Se você estivesse executando em um ambiente gráfico, descomentaria a linha abaixo:
# if janela_principal and isinstance(janela_principal, tk.Tk):
#     janela_principal.mainloop()

print("A estrutura da interface com abas Tkinter foi criada e estaria pronta para execução em um ambiente gráfico. \n`root.mainloop()` foi comentado para evitar erros em ambientes sem display.")
