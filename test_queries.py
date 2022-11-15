import libs
db_connection_str = 'mysql+pymysql://root:@localhost:3306/alfred_db'
db_connection = libs.create_engine(db_connection_str)

query = "SELECT id_conta, nome_conta FROM conta WHERE situacao = 'A';"
df_contas = libs.pd.read_sql(query, con=db_connection)

print(df_contas)