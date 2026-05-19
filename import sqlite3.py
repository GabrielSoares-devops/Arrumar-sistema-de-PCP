import sqlite3

def inicializar_banco():
    # Conecta ao arquivo do banco de dados (se não existir, o Python cria na hora)
    conexao = sqlite3.connect('oxicorte_pcp.db')
    cursor = conexao.cursor()

    # Habilita o suporte a chaves estrangeiras (importante para integridade)
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Criando a tabela de Ordens de Produção
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ordens_producao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_op TEXT NOT NULL,
            numero_pedido TEXT NOT NULL,
            cliente TEXT NOT NULL,
            material TEXT NOT NULL,
            espessura REAL NOT NULL,
            quantidade_pedida INTEGER NOT NULL,
            status TEXT DEFAULT 'Pendente'
        )
    ''')

    # 2. Criando a tabela de Peças e Desenhos DXF
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pecas_dxf (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            op_id INTEGER NOT NULL,
            tipo_geometrico TEXT CHECK(tipo_geometrico IN ('PARAMETRICA', 'ARQUIVO_DXF')),
            diametro_externo REAL,
            diametro_interno REAL,
            caminho_arquivo_dxf TEXT,
            perimetro_corte REAL,
            quantidade_furos INTEGER,
            FOREIGN KEY (op_id) REFERENCES ordens_producao(id) ON DELETE CASCADE
        )
    ''')

    # 3. Criando a tabela de Estoque de Chapas e Retalhos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estoque_chapas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo_rastreio TEXT UNIQUE NOT NULL,
            tipo_material TEXT NOT NULL,
            espessura REAL NOT NULL,
            comprimento REAL NOT NULL,
            largura REAL NOT NULL,
            eh_retalho INTEGER CHECK(eh_retalho IN (0, 1)),
            geometria_irregular_dxf TEXT,
            caminho_imagem_preview TEXT,
            status TEXT DEFAULT 'Disponível' CHECK(status IN ('Disponível', 'Reservado', 'Consumido'))
        )
    ''')

    # 4. Criando a tabela de Histórico de Consumo/Nesting
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historico_consumo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chapa_id INTEGER NOT NULL,
            op_id INTEGER NOT NULL,
            data_corte TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (chapa_id) REFERENCES estoque_chapas(id),
            FOREIGN KEY (op_id) REFERENCES ordens_producao(id)
        )
    ''')

    # Salva as alterações e fecha a conexão
    conexao.commit()
    conexao.close()
    print("Banco de dados 'oxicorte_pcp.db' e tabelas criados com sucesso!")

if __name__ == '__main__':
    inicializar_banco()
