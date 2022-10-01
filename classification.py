import libs
import functions.queries

##Lançamento manual ou nao?
print('\n######## Seu lançamento será manual ou com link NFE? ########\n')
print('######## Digite M para MANUAL e N para nota fiscal eletrônica ########\n')
tp_lancamento = input()


##Resgata as contas registradas em BD
print('\n######## ESCOLHA DE QUAL CONTA QUE SAIRÁ O SEU DINHEIRO ########\n')
df_contas = functions.queries.get_contas()
print(df_contas['nome_conta'])

id_conta = input("\n\nEscolha o ID tipo da Conta: ")
id_conta = libs.pd.to_numeric(id_conta)
escolha_nome_transacao = df_contas.loc[id_conta, 'nome_conta']
escolha_id_conta = df_contas.loc[id_conta, 'id_conta']
print('\n --> Conta escolhida: \n' + str(escolha_nome_transacao) + '\n\n')


##Resgata as contas registradas em BD
print('######## ESCOLHA DO TIPO DE TRANSAÇÃO ########\n')
df_tipo_transacao = functions.queries.get_tipo_transacao()
print(df_tipo_transacao['nome_tp_transacao'])

id_tp_transacao = input("\n\nEscolha o ID tipo de transação: ")
id_tp_transacao = libs.pd.to_numeric(id_tp_transacao)
escolha_nome_tipo_transacao = df_tipo_transacao.loc[id_tp_transacao, 'nome_tp_transacao']
escolha_id_tipo_transacao = df_tipo_transacao.loc[id_tp_transacao, 'id_tp_transacao']
print('\n --> Conta escolhida: \n' + str(escolha_nome_tipo_transacao) + '\n\n')


##Resgata as CATEGORIAS registradas em BD
print('######## ESCOLHA DA CATEGORIA ########\n')
df_categoria = functions.queries.get_categoria()
print(df_categoria['nome_categoria'])

id_categoria = input("\n\nEscolha o ID da Categoria: ")
id_categoria = libs.pd.to_numeric(id_categoria)
escolha_nome_categoria = df_categoria.loc[id_categoria, 'nome_categoria']
escolha_id_categoria = df_categoria.loc[id_categoria, 'id_categoria']
print('\n --> Categoria escolhida: \n' + str(escolha_nome_categoria) + '\n\n')


##Resgata as SUB-CATEGORIAS registradas em BD
print('######## ECOLHA A SUB-CATEGORIA ########\n')
df_sub_categoria = functions.queries.get_subcategoria(escolha_id_categoria)
print(df_sub_categoria['nome_subcategoria'])

id_sub_categoria = input("\n\nEscolha o ID da Subcategoria: ")
id_sub_categoria = libs.pd.to_numeric(id_sub_categoria)
escolha_nome_categoria = df_sub_categoria.loc[id_sub_categoria, 'nome_subcategoria']
escolha_id_sub_categoria = df_sub_categoria.loc[id_sub_categoria, 'id_subcategoria']
print('\n --> Categoria escolhida: \n' + str(escolha_nome_categoria) + '\n\n')