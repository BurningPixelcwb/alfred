import libs
db_connection_str = 'mysql+pymysql://root:@localhost:3306/alfred_db'
db_connection = libs.create_engine(db_connection_str)

def get_contas():
    query = "SELECT id_conta, nome_conta FROM conta WHERE situacao = 'A';"
    df_contas = libs.pd.read_sql(query, con=db_connection)

    return df_contas#.to_string(index=False)

def get_tipo_transacao():
    query = "SELECT id_tp_transacao, nome_tp_transacao FROM tipo_transacao;"
    df_tipo_transacao = libs.pd.read_sql(query, con=db_connection)

    return df_tipo_transacao

def get_categoria():
    query = "SELECT id_categoria, nome_categoria FROM categoria;"
    df_categoria = libs.pd.read_sql(query, con=db_connection)

    return df_categoria

def get_subcategoria(categoria):
    query = "SELECT id_subcategoria, nome_subcategoria FROM `subcategoria` WHERE fk_id_categoria = " + str(categoria) + ";"
    df_sub_categoria = libs.pd.read_sql(query, con=db_connection)

    return df_sub_categoria

def insert_trancao(df_transacao):
    df_transacao.to_sql('transacao', db_connection, if_exists='append', index = False)

    return True

def get_last_transacao():
    query = "SELECT * FROM transacao ORDER BY id_transacao DESC LIMIT 1;"
    url_cara = libs.pd.read_sql(query, con=db_connection)

    return url_cara

def set_ticket(ticket):
    ticket.to_sql('ticket', db_connection, if_exists='append', index = False)

    return True