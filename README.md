# Projeto da API de boletos do Banco do Brasil
Estou desenvolvendo uma solução, onde com python, será passado os parâmetros pelo terminal e ele fará as requisições para API do Banco do Brasil e o script retornará o retorno da API (preciso melhorar esse texto)
A ideia ocorreu devido a um código legado onde em laravel o sistema está todo funcionando mas as requisições de edição do boleto e baixa de boleto estão retornando um string vazia sem código de erro e ficamos travados neste problema, eu tive a opção de refazer o código em php no próprio servidor ou refazer o código para rodar direto no programa de gestão da versátil e escolhi a segunda opção.

O que estamos usando na criação do script:
 - Python 3.9
 - biblioteca sys
 - biblioteca json
 - biblioteca requests
 - biblioteca decouple

A biblioteca sys estamos usando para receber parâmetros externos direto no terminal quando chamamos o script
A biblioteca json estamos usando para tratar o retorno da Api do Bando do Brasil
A biblioteca requests estamos usando para fazer as requisições para a Api do Banco do Brasil
A biblioteca decouple estamaos usando para ter as informações sensíveis em um arquivo .env e assim não correr risco de enviar por engano para o repositório público.

Todas as bibliotecas e versões estão em requirements.txt

Para instalar tudo automaticamente use 
`pip install -r requirements.txt`

Você precisará criar um arquivo .env e neste arquivo você colocará as informações da seguinte forma:

```
BASIC_CODE_TOKEN_APP_DEFAULT=lorem ipsun
GW_DEV_APP_KEY=lorem ipsun
CLIENT_ID=lorem ipsun
CLIENT_SECRET=lorem ipsun
```


Troque o lorem ipsun por as informações do site do sistema do Banco do Brasil, as informações não devem usar aspas e a primeira palavra deve estar colada com o = assim como no exemplo, sem espaço
O script está em desenvolvimento e qualquer dica, pedido de modificação e etc eu responderei o mais rápido possível

Neste momento estamos com erro 500 e aguardando retorno do Banco do Brasil