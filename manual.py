import libs
import classification
import functions.queries

##Lançamento manual ou nao?
print('\n######## Digite o valor gasto ########\n')
valor_manual = input()

dt_lancamento = libs.datetime.now()

#Cria um data frame
ticket_lancamento = {
    'fk_id_conta': classification.escolha_id_conta
    , 'fk_id_tp_transacao': classification.escolha_id_tipo_transacao
    , 'fk_id_sub_categoria': [classification.escolha_id_sub_categoria]
    , 'url_nfe': ''
    , 'estabelecimento': ''
    , 'endereco_compra': ''
    , 'dt_ticket': ''
    , 'dt_lancamento': dt_lancamento
}
df_transacao = libs.pd.DataFrame(data=ticket_lancamento)

##insere lancamento
functions.queries.insert_trancao(df_transacao)

##Resgata as contas registradas em BD
url_cara = functions.queries.get_last_transacao()
fk_id_transacao = url_cara.at[0,'id_transacao']

ticket = libs.pd.DataFrame({'valor_total':[valor_manual], "fk_id_transacao":[fk_id_transacao]})
ticket['valor_total'] = ticket['valor_total'].str.replace(',', '.')

functions.queries.set_ticket(ticket)