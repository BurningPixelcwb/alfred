import libs
import functions.queries
import classification

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
    'fk_id_conta': classification.escolha_id_conta
    , 'fk_id_tp_transacao': classification.escolha_id_tipo_transacao
    , 'fk_id_sub_categoria': [classification.escolha_id_sub_categoria]
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