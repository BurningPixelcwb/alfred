from ctypes import get_last_error
import libs
import functions.queries


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


# INSERE A URL DA NOTA FISCAL
print('######## AGORA QUE ESTÁ TUDO CERTO, BASTA COLAR O LINK DO TICKET! ########\n')
print('Insira a URL da nota fiscal eletronica:')
url_nfe = input()
nav = libs.webdriver.Chrome(service=libs.service)

##Pandas

##Series para lista de compra
df_cod_prod = libs.pd.Series([])
df_item_comprado = libs.pd.Series([])
df_quantidade = libs.pd.Series([])
df_medida = libs.pd.Series([])
df_preco = libs.pd.Series([])
df_valor_total = libs.pd.Series([])

#Series para: Local da compra
df_local_compra = libs.pd.Series([])

#Series para: Consumidor

#Series para: Info Gerais

transacao = libs.pd.DataFrame()

ticket = libs.pd.DataFrame()

nav.get(url_nfe)

dt_ticket = nav.find_elements(libs.By.XPATH,'//*[@id="infos"]/div[1]/div/ul/li')



#resolvendo a da e hora do ticket
arr_elements = len(dt_ticket)

for i in range(arr_elements):
    dt_ticket = dt_ticket[i].text
    dt_ticket = dt_ticket.splitlines()
    dt_ticket = dt_ticket[2]
    dt_ticket = dt_ticket.split()
    
    data_ticket = dt_ticket[5]
    hora_ticket = dt_ticket[6]

data_ticket = data_ticket.split('/')
data_ticket = data_ticket[2] + '-' + data_ticket[1] + '-' + data_ticket[0] + ' ' + hora_ticket


#resolvendo estabelecimento
arr_estabelecimento = nav.find_elements(libs.By.XPATH, '//*[@id="u20"]')

arr_elements = len(arr_estabelecimento)

for i in range(arr_elements):
    estabelecimento = arr_estabelecimento[i].text

#definindo data do lançamento do ticket
dt_lancamento = libs.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

#resolvendo local da compra
local_compra = nav.find_elements(libs.By.XPATH, '//div[@class="txtTopo"]')
endereco_compra = nav.find_elements(libs.By.XPATH, '//div[@class="text"]')
arr_elements = len(endereco_compra)

for i in range(arr_elements):
    endereco = endereco_compra[i].text

#recuperando informações da compra
item_comprado = nav.find_elements(libs.By.XPATH, '//span[@class="txtTit2"]')

cod_produto = nav.find_elements(libs.By.XPATH, '//span[@class="RCod"]')

quantidade = nav.find_elements(libs.By.XPATH, '//span[@class="Rqtd"]')

medida = nav.find_elements(libs.By.XPATH, '//span[@class="RUN"]')

preco = nav.find_elements(libs.By.XPATH, '//span[@class="RvlUnit"]')

valor_total = nav.find_elements(libs.By.XPATH, '//span[@class="valor"]')

compras = len(item_comprado)

for i in range(compras):
    #print(cod_produto[i].text + " : " + item_comprado[i].text + " : " +  quantidade[i].text + " : " +  medida[i].text + " : " + qntXmedida[i].text + " : " + valor_total[i].text)
    
    df_cod_prod[i] = cod_produto[i].text
    
    df_item_comprado[i] = item_comprado[i].text

    df_quantidade[i] = quantidade[i].text

    df_medida[i] = medida[i].text

    df_preco[i] = preco[i].text

    df_valor_total[i] = valor_total[i].text

nav.close()

#Cria um data frame
ticket_lancamento = {
    'fk_id_conta': escolha_id_conta
    , 'fk_id_tp_transacao': escolha_id_tipo_transacao
    , 'fk_id_sub_categoria': [escolha_id_sub_categoria]
    , 'url_nfe': url_nfe
    , 'estabelecimento': estabelecimento
    , 'endereco_compra': endereco
    , 'dt_ticket': data_ticket
    , 'dt_lancamento': dt_lancamento
}
df_transacao = libs.pd.DataFrame(data=ticket_lancamento)

##insere lancamento
functions.queries.insert_trancao(df_transacao)

##Resgata as contas registradas em BD
url_cara = functions.queries.get_last_transacao()
fk_id_transacao = url_cara.at[0,'id_transacao']

#criando DataFrame de ticket
ticket.insert(0, "cod_prod", df_cod_prod)
ticket.insert(1, "item_comprado", df_item_comprado)
ticket.insert(2, "quantidade", df_quantidade)
ticket.insert(3, "medida", df_medida)
ticket.insert(4, "preco", df_preco)
ticket.insert(5, "valor_total", df_valor_total)
ticket.insert(6, "fk_id_transacao", fk_id_transacao)

#Limpando coluna: cod_prod
ticket['cod_prod'] = ticket['cod_prod'].str.replace('Código: ', '')
ticket['cod_prod'] = ticket['cod_prod'].str.replace('(', '')
ticket['cod_prod'] = ticket['cod_prod'].str.replace(')', '')


#Limpando coluna: quantidade
ticket['quantidade'] = ticket['quantidade'].str.replace('Qtde.:', '')
ticket['quantidade'] = ticket['quantidade'].str.replace(',', '.')


#Limpando coluna: medida
ticket['medida'] = ticket['medida'].str.replace('UN: ', '')


#Limpando coluna: preco
ticket['preco'] = ticket['preco'].str.replace('Vl. Unit.: ', '')
ticket['preco'] = ticket['preco'].str.replace(',', '.')


#Limpando coluna: valor_total
ticket['valor_total'] = ticket['valor_total'].str.replace(',', '.')

functions.queries.set_ticket(ticket)