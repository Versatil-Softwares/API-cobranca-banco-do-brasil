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

  payload = "{\n    \"numeroConvenio\": "+numeroConvenio+",\n    \"dataVencimento\": \""+dataVencimento+"\",\n    \"valorOriginal\": "+valorOriginal+",\n    \"numeroCarteira\": "+numeroCarteira+",\n    \"numeroVariacaoCarteira\": "+numeroVariacaoCarteira+",\n    \"codigoModalidade\": "+codigoModalidade+",\n    \"dataEmissao\": \""+dataEmissao+"\",\n    \"valorAbatimento\": "+valorAbatimento+",\n    \"quantidadeDiasProtesto\": "+quantidadeDiasProtesto+",\n    \"quantidadeDiasNegativacao\": "+quantidadeDiasNegativacao+",\n    \"orgaoNegativador\": "+orgaoNegativador+",\n    \"indicadorAceiteTituloVencido\": \""+indicadorAceiteTituloVencido+"\",\n    \"numeroDiasLimiteRecebimento\": "+numeroDiasLimiteRecebimento+",\n    \"codigoAceite\": \""+codigoAceite+"\",\n    \"codigoTipoTitulo\": "+codigoTipoTitulo+",\n    \"descricaoTipoTitulo\": \""+descricaoTipoTitulo+"\",\n    \"indicadorPermissaoRecebimentoParcial\": \""+indicadorPermissaoRecebimentoParcial+"\",\n    \"numeroTituloBeneficiario\": \""+numeroTituloBeneficiario+"\",\n    \"campoUtilizacaoBeneficiario\": \""+campoUtilizacaoBeneficiario+"\",\n    \"numeroTituloCliente\": \""+numeroTituloCliente+"\",\n    \"mensagemBloquetoOcorrencia\": \""+mensagemBloquetoOcorrencia+"\",\n    \"desconto\": {\n        \"tipo\": "+tipodesconto+",\n        \"dataExpiracao\": \""+dataExpiracaodesconto+"\",\n        \"porcentagem\": "+porcentagemdesconto+",\n        \"valor\": "+valordesconto+"\n    },\n    \"segundoDesconto\": {\n        \"dataExpiracao\": \"sit\",\n        \"porcentagem\": 0,\n        \"valor\": 0\n    },\n    \"terceiroDesconto\": {\n        \"dataExpiracao\": \"est fugiat Ut ipsum\",\n        \"porcentagem\": 0,\n        \"valor\": 0\n    },\n    \"jurosMora\": {\n        \"tipo\": "+tipojurosmora+",\n        \"porcentagem\": "+porcentagemjurosmora+",\n        \"valor\": "+valorjurosmora+"\n    },\n    \"multa\": {\n        \"tipo\": "+tipomulta+",\n        \"data\": \""+datamulta+"\",\n        \"porcentagem\": "+porcentagemmulta+",\n        \"valor\": "+valormulta+"\n    },\n    \"pagador\": {\n        \"tipoInscricao\": "+tipoInscricaopagador+",\n        \"numeroInscricao\": "+numeroInscricaopagador+",\n        \"nome\": \""+nomepagador+"\",\n        \"endereco\": \""+enderecopagador+"\",\n        \"cep\": "+ceppagador+",\n        \"cidade\": \""+cidadepagador+"\",\n        \"bairro\": \""+bairropagador+"\",\n        \"uf\": \""+ufpagador+"\",\n        \"telefone\": \""+telefonepagador+"\"\n    },\n    \"beneficiarioFinal\": {\n        \"tipoInscricao\": "+tipoInscricaobeneficiarioFinal+",\n        \"numeroInscricao\": "+numeroInscricaobeneficiarioFinal+",\n        \"nome\": \""+nomebeneficiarioFinal+"\"\n    },\n    \"indicadorPix\": \""+indicadorPix+"\"\n}"
  headers = {
    'Authorization' : "Bearer "+token,
    "Content-Type" : "application/json",
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print("##############  "+url+"  ########################")
  print(response.text)
  return(response.text)

######################################################################################
#Função para editar dados do boleto já criado
def Editar(id, numeroConvenio, mudarVencimento, novaDataVencimento):
  url = url_base+"/"+id+"?gw-dev-app-key="+GW_DEV_APP_KEY

 
  payload = "{\n    \"indicadorCancelarAbatimento\": \"N\",\n    \"indicadorAlterarDataDesconto\": \"N\",\n    \"indicadorAlterarDesconto\": \"N\",\n    \"indicadorAlterarEnderecoPagador\": \"N\",\n    \"indicadorAlterarPrazoBoletoVencido\": \"N\",\n    \"indicadorAlterarSeuNumero\": \"N\",\n    \"indicadorAtribuirDesconto\": \"N\",\n    \"indicadorCancelarProtesto\": \"N\",\n    \"indicadorCobrarJuros\": \"N\",\n    \"indicadorCobrarMulta\": \"N\",\n    \"indicadorDispensarJuros\": \"N\",\n    \"indicadorDispensarMulta\": \"N\",\n    \"indicadorIncluirAbatimento\": \"N\",\n    \"indicadorNegativar\": \"N\",\n    \"indicadorNovaDataVencimento\": \""+mudarVencimento+"\",\n    \"indicadorProtestar\": \"N\",\n    \"indicadorSustacaoProtesto\": \"N\",\n    \"numeroConvenio\": "+numeroConvenio+",\n    \"alteracaoData\": {\n        \"novaDataVencimento\": \""+novaDataVencimento+"\"\n    },\n    \"desconto\": {\n        \"tipoPrimeiroDesconto\": 0,\n        \"valorPrimeiroDesconto\": 0,\n        \"percentualPrimeiroDesconto\": 0,\n        \"dataPrimeiroDesconto\": \"0\",\n        \"tipoSegundoDesconto\": 0,\n        \"valorSegundoDesconto\": 0,\n        \"percentualSegundoDesconto\": 0,\n        \"dataSegundoDesconto\": \"0\",\n        \"tipoTerceiroDesconto\": 0,\n        \"valorTerceiroDesconto\": 0,\n        \"percentualTerceiroDesconto\": 0,\n        \"dataTerceiroDesconto\": \"0\"\n    },\n    \"alteracaoDesconto\": {\n        \"tipoPrimeiroDesconto\": 0,\n        \"novoValorPrimeiroDesconto\": 0,\n        \"novoPercentualPrimeiroDesconto\": 0,\n        \"novaDataLimitePrimeiroDesconto\": \"0\",\n        \"tipoSegundoDesconto\": 0,\n        \"novoValorSegundoDesconto\": 0,\n        \"novoPercentualSegundoDesconto\": 0,\n        \"novaDataLimiteSegundoDesconto\": \"0\",\n        \"tipoTerceiroDesconto\": 0,\n        \"novoValorTerceiroDesconto\": 0,\n        \"novoPercentualTerceiroDesconto\": 0,\n        \"novaDataLimiteTerceiroDesconto\": \"0\"\n    },\n    \"alteracaoDataDesconto\": {\n        \"novaDataLimitePrimeiroDesconto\": \"0\",\n        \"novaDataLimiteSegundoDesconto\": \"0\",\n        \"novaDataLimiteTerceiroDesconto\": \"0\"\n    },\n    \"protesto\": {\n        \"quantidadeDiasProtesto\": 0\n    },\n    \"abatimento\": {\n        \"valorAbatimento\": 0\n    },\n    \"alteracaoAbatimento\": {\n        \"novoValorAbatimento\": 0\n    },\n    \"juros\": {\n        \"tipoJuros\": 0,\n        \"valorJuros\": 0,\n        \"taxaJuros\": 0\n    },\n    \"multa\": {\n        \"tipoMulta\": 0,\n        \"valorMulta\": 0,\n        \"dataInicioMulta\": \"0\",\n        \"taxaMulta\": 0\n    },\n    \"negativacao\": {\n        \"quantidadeDiasNegativacao\": 0,\n        \"tipoNegativacao\": 0\n    },\n    \"alteracaoSeuNumero\": {\n        \"codigoSeuNumero\": \"0\"\n    },\n    \"alteracaoEndereco\": {\n        \"enderecoPagador\": \"lorem\",\n        \"bairroPagador\": \"lorem\",\n        \"cidadePagador\": \"lorem\",\n        \"UFPagador\": \"lorem\",\n        \"CEPPagador\": 0\n    },\n    \"alteracaoPrazo\": {\n        \"quantidadeDiasAceite\": 0\n    }\n}"
  headers = {
  "Authorization" : "Bearer "+token,
  "Content-Type" : "application/json",
  }
  
  response = requests.request("PATCH", url, headers=headers, data=payload)
  
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
  "Authorization" : "Bearer "+token,
  "Content-Type" : "application/json",
}
  #faço a requisição e guardo o retorno na vairavel response
  response = requests.request("POST", url_requisicao, headers=headers, data=payload)
 
  print(response.text)
  print(response.headers)
  print(response.url)
  return(response.text)


######################################################################################
#Função de Listar os boletos que estão ligados a determinada conta, você deve informar se o boleto é A para em aberto ou B para fechado(baixado, pago), a agencia e a conta
def Listar(situacao, agencia, conta):
  url = url_base+"?gw-dev-app-key="+GW_DEV_APP_KEY+"&indicadorSituacao="+situacao+"&agenciaBeneficiario="+agencia+"&contaBeneficiario="+conta

  payload={}
  headers = {
    'Authorization' : "Bearer "+token,
    "Content-Type" : "application/json",
  }
 
  response = requests.get(url, headers=headers, data=payload)
  print("##############  "+url+"  ########################")
  print(response.text)
  return(response.text)


#Preparo o script para receber argumentos externos
argumentos_externos = sys.argv

#Chama as funções do script com os dados externos na chamada da função

if argumentos_externos[1] == "baixar":
  Apagar(argumentos_externos[2], argumentos_externos[3])
elif argumentos_externos[1] == "gerar":
  Criar(argumentos_externos[2], argumentos_externos[3], argumentos_externos[4], argumentos_externos[5],argumentos_externos[6], argumentos_externos[7], argumentos_externos[8], argumentos_externos[9],argumentos_externos[10], argumentos_externos[11], argumentos_externos[12], argumentos_externos[13],argumentos_externos[14], argumentos_externos[15], argumentos_externos[16], argumentos_externos[17],argumentos_externos[18], argumentos_externos[19], argumentos_externos[20], argumentos_externos[21],argumentos_externos[22], argumentos_externos[23], argumentos_externos[24], argumentos_externos[25],argumentos_externos[26], argumentos_externos[27], argumentos_externos[28], argumentos_externos[29],argumentos_externos[30], argumentos_externos[31], argumentos_externos[32], argumentos_externos[33],argumentos_externos[34], argumentos_externos[35], argumentos_externos[36], argumentos_externos[37],argumentos_externos[38], argumentos_externos[39], argumentos_externos[40], argumentos_externos[41],argumentos_externos[42], argumentos_externos[43], argumentos_externos[44], argumentos_externos[45],argumentos_externos[46] )
elif argumentos_externos[1] == "listar":
  Listar(argumentos_externos[2], argumentos_externos[3], argumentos_externos[4])
elif argumentos_externos[1] == "editar":
  Editar(argumentos_externos[2], argumentos_externos[3], argumentos_externos[4], argumentos_externos[5])

