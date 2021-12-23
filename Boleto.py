#!env/Scripts/python.exe

import sys, json, requests
from decouple import config #importa a biblioteca que puxa as informações do arquivo .env


url_base = "https://api.bb.com.br/cobrancas/v2/boletos"

BASIC_CODE_TOKEN_APP_DEFAULT = config('BASIC_CODE_TOKEN_APP_DEFAULT')
GW_DEV_APP_KEY = config('GW_DEV_APP_KEY')
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
######################################################################################
#Função que faz a autenticação no Banco do Brasil, ela envia o código Basic e retorna o token temporário
def Autenticacao():
  headers = {
  'Authorization' : BASIC_CODE_TOKEN_APP_DEFAULT,
}
  url_requisicao = "https://oauth.bb.com.br/oauth/token"
  payload={
    "grant_type" : "client_credentials",
    "scope" : "cobrancas.boletos-info cobrancas.boletos-requisicao"
  }
  requisicao = requests.post(url_requisicao, params=payload, headers=headers )
  # Até a linha de cima, faço a requisição de acordo com as instruções da documentação no postman do BB
  #abaixo eu transformo o retorno em uma lista
  data = json.loads(requisicao.content)
  #print(data['access_token'])
  #abaixo eu retorno o item acces_token da lista e assim posso usar como string
  return data['access_token']

token = Autenticacao()

######################################################################################
#Função que cria um novo boleto
def Criar(numeroConvenio, dataVencimento, valorOriginal, numeroCarteira, numeroVariacaoCarteira, codigoModalidade, dataEmissao, valorAbatimento, quantidadeDiasProtesto, quantidadeDiasNegativacao, orgaoNegativador, indicadorAceiteTituloVencido, numeroDiasLimiteRecebimento, codigoAceite, codigoTipoTitulo, descricaoTipoTitulo, indicadorPermissaoRecebimentoParcial, numeroTituloBeneficiario, campoUtilizacaoBeneficiario, numeroTituloCliente, mensagemBloquetoOcorrencia, tipodesconto, dataExpiracaodesconto, porcentagemdesconto, valordesconto, tipojurosmora,  porcentagemjurosmora, valorjurosmora, tipomulta, datamulta, porcentagemmulta, valormulta, tipoInscricaopagador, numeroInscricaopagador, nomepagador, enderecopagador, ceppagador, cidadepagador, bairropagador, ufpagador, telefonepagador, tipoInscricaobeneficiarioFinal, numeroInscricaobeneficiarioFinal, nomebeneficiarioFinal, indicadorPix):
  url = url_base+"?gw-dev-app-key="+GW_DEV_APP_KEY

  payload = "{\n    \"numeroConvenio\": {},\n    \"dataVencimento\": \"{}\",\n    \"valorOriginal\": {},\n    \"numeroCarteira\": {},\n    \"numeroVariacaoCarteira\": {},\n    \"codigoModalidade\": {},\n    \"dataEmissao\": \"{}\",\n    \"valorAbatimento\": {},\n    \"quantidadeDiasProtesto\": {},\n    \"quantidadeDiasNegativacao\": {},\n    \"orgaoNegativador\": {},\n    \"indicadorAceiteTituloVencido\": \"{}\",\n    \"numeroDiasLimiteRecebimento\": {},\n    \"codigoAceite\": \"{}\",\n    \"codigoTipoTitulo\": {},\n    \"descricaoTipoTitulo\": \"{}\",\n    \"indicadorPermissaoRecebimentoParcial\": \"{}\",\n    \"numeroTituloBeneficiario\": \"{}\",\n    \"campoUtilizacaoBeneficiario\": \"{}\",\n    \"numeroTituloCliente\": \"{}\",\n    \"mensagemBloquetoOcorrencia\": \"{}\",\n    \"desconto\": {\n        \"tipo\": {},\n        \"dataExpiracao\": \"{}\",\n        \"porcentagem\": {},\n        \"valor\": {}\n    },\n    \"segundoDesconto\": {\n        \"dataExpiracao\": \"sit\",\n        \"porcentagem\": 0,\n        \"valor\": 0\n    },\n    \"terceiroDesconto\": {\n        \"dataExpiracao\": \"est fugiat Ut ipsum\",\n        \"porcentagem\": 0,\n        \"valor\": 0\n    },\n    \"jurosMora\": {\n        \"tipo\": {},\n        \"porcentagem\": {},\n        \"valor\": {}\n    },\n    \"multa\": {\n        \"tipo\": {},\n        \"data\": \"{}\",\n        \"porcentagem\": {},\n        \"valor\": {}\n    },\n    \"pagador\": {\n        \"tipoInscricao\": {},\n        \"numeroInscricao\": {},\n        \"nome\": \"{}\",\n        \"endereco\": \"{}\",\n        \"cep\": {},\n        \"cidade\": \"{}\",\n        \"bairro\": \"{}\",\n        \"uf\": \"{}\",\n        \"telefone\": \"{}\"\n    },\n    \"beneficiarioFinal\": {\n        \"tipoInscricao\": {},\n        \"numeroInscricao\": {},\n        \"nome\": \"{}\"\n    },\n    \"indicadorPix\": \"{}\"\n}".format(numeroConvenio, dataVencimento, valorOriginal, numeroCarteira, numeroVariacaoCarteira, codigoModalidade, dataEmissao, valorAbatimento, quantidadeDiasProtesto, quantidadeDiasNegativacao, orgaoNegativador, indicadorAceiteTituloVencido, numeroDiasLimiteRecebimento, codigoAceite, codigoTipoTitulo, descricaoTipoTitulo, indicadorPermissaoRecebimentoParcial, numeroTituloBeneficiario, campoUtilizacaoBeneficiario, numeroTituloCliente, mensagemBloquetoOcorrencia, tipodesconto, dataExpiracaodesconto, porcentagemdesconto, valordesconto, tipojurosmora,  porcentagemjurosmora, valorjurosmora, tipomulta, datamulta, porcentagemmulta, valormulta, tipoInscricaopagador, numeroInscricaopagador, nomepagador, enderecopagador, ceppagador, cidadepagador, bairropagador, ufpagador, telefonepagador, tipoInscricaobeneficiarioFinal, numeroInscricaobeneficiarioFinal, nomebeneficiarioFinal, indicadorPix)
  headers = {
    'Authorization' : "Bearer "+token,
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print("##############"+url+"########################")
  print(response.text)

######################################################################################
#Função que faz a requisição de baixa do boleto
def Apagar(id, numero_convenio):
  #pego o retorno da função de autenticação
  
  #preparo a requisição como informado na documentação
  url_requisicao = url_base+"/"+id+"/baixar?gw-dev-app-key="+GW_DEV_APP_KEY
  payload = "{\n    \"numeroConvenio\": "+numero_convenio+"\n}"
  #payload = '{"numeroConvenio":'+numero_convenio+'}'
  
  headers = {
  'Authorization' : "Bearer "+token,
}
  #faço a requisição e guardo o retorno na vairavel response
  response = requests.request("POST", url_requisicao, headers=headers, data=payload)
 
  print("   ###   " + url_requisicao + "   ###   ")
  print(response.text)


######################################################################################
#Função de Listar os boletos que estão ligados a determinada conta, você deve informar se o boleto é A para em aberto ou B para fechado(baixado, pago), a agencia e a conta
def Listar(situacao, agencia, conta):
  url = url_base+"?gw-dev-app-key="+GW_DEV_APP_KEY+"&indicadorSituacao="+situacao+"&agenciaBeneficiario="+agencia+"&contaBeneficiario="+conta

  payload={}
  headers = {
    'Authorization' : "Bearer "+token,
  }
 
  response = requests.get(url, headers=headers, data=payload)
  print("##############"+url+"########################")
  print(response.text)


#Preparo o script para receber argumentos externos
argumentos_externos = sys.argv

#Chama as funções do script com os dados externos na chamada da função

if argumentos_externos[1] == "baixar":
  Apagar(argumentos_externos[2], argumentos_externos[3])
elif argumentos_externos[1] == "gerar":
  Criar(argumentos_externos[2], argumentos_externos[3], argumentos_externos[4], argumentos_externos[5],argumentos_externos[6], argumentos_externos[7], argumentos_externos[8], argumentos_externos[9],argumentos_externos[10], argumentos_externos[11], argumentos_externos[12], argumentos_externos[13],argumentos_externos[14], argumentos_externos[15], argumentos_externos[16], argumentos_externos[17],argumentos_externos[18], argumentos_externos[19], argumentos_externos[20], argumentos_externos[21],argumentos_externos[22], argumentos_externos[23], argumentos_externos[24], argumentos_externos[25],argumentos_externos[26], argumentos_externos[27], argumentos_externos[28], argumentos_externos[29],argumentos_externos[30], argumentos_externos[31], argumentos_externos[32], argumentos_externos[33],argumentos_externos[34], argumentos_externos[35], argumentos_externos[36], argumentos_externos[37],argumentos_externos[38], argumentos_externos[39], argumentos_externos[40], argumentos_externos[41],argumentos_externos[42], argumentos_externos[43], argumentos_externos[44], argumentos_externos[45],argumentos_externos[46] )
elif argumentos_externos[1] == "listar":
  Listar(argumentos_externos[2], argumentos_externos[3], argumentos_externos[4])

