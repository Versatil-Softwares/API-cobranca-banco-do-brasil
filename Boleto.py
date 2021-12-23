#!env/Scripts/python.exe

import sys, json, requests
from decouple import config #importa a biblioteca que puxa as informações do arquivo .env


url_base = "https://api.bb.com.br/cobrancas/v2/boletos/"

BASIC_CODE_TOKEN_APP_DEFAULT = config('BASIC_CODE_TOKEN_APP_DEFAULT')
GW_DEV_APP_KEY = config('GW_DEV_APP_KEY')
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')

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

def Apagar(id, numero_convenio):
  #pego o retorno da função de autenticação
  
  #preparo a requisição como informado na documentação
  url_requisicao = url_base+id+"/baixar?gw-dev-app-key="+GW_DEV_APP_KEY
  payload = "{\n    \"numeroConvenio\": "+numero_convenio+"\n}"
  #payload = '{"numeroConvenio":'+numero_convenio+'}'
  
  headers = {
  'Authorization' : "Bearer "+token,
}
  #faço a requisição e guardo o retorno na vairavel response
  response = requests.request("POST", url_requisicao, headers=headers, data=payload)
 
  #print("   ###   " + url_requisicao + "   ###   ")
  print(response.text)


#Preparo o script para receber um argumento externo
argumentos_externos = sys.argv

def listar(situacao, agencia, conta):
  url = url_base+"?gw-dev-app-key="+GW_DEV_APP_KEY+"&indicadorSituacao="+situacao+"&agenciaBeneficiario="+agencia+"&contaBeneficiario="+conta
 
  payload={}
  headers = {
    'Authorization' : "Bearer "+token,
  }
 
  response = requests.request("GET", url, headers=headers, data=payload)
 
  print(response.text)

try:
  if argumentos_externos[1] == "baixar":
    Apagar(argumentos_externos[2], argumentos_externos[3])
  elif argumentos_externos[1] == "listar":
    Apagar(argumentos_externos[2], argumentos_externos[3])
except: 
  print("Algum erro aconteceu, chame o suporte")

