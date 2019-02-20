# Relatório

## Principais Dificuldades

Inicialmente, analisando o fluxo de obtenção do pdf do diário a partir da data, minha principal preocupação foi como encontrar uma forma de "passar" pela validação de Captcha que era exigida para o download do pdf. Estudando mais profundamente a função JS que fazia a chamada do Captcha e posteriormente download do pdf, percebi que o download era acionado por um form (formDocumentoDownload) com paramêtros passados via POST, e que configurando os campos do formulário e acionando o submit() o download era iniciado sem problemas.

Meu primeiro pensamento foi injetar um script JS que acionava o form da página:
```
document.getElementById("id").value = 86737; //id do pdf
document.getElementById("tribunal").value = 'TSE';
document.getElementById("captchaValidacao").value = 'ok';
document.getElementById("formDocumentoDownload").submit();
```

Scripts podem ser inseridos na página de requisição através da API WebDriver do [Selenium](https://intoli.com/blog/javascript-injection/). Entretanto, há um problema com essa abordagem, nem todos os métodos de injeção JavaScript se comportam adequadamente. Alguns executam seu código JavaScript antes que a página seja analisada pelo navegador, enquanto outros aguardam até que os eventos DOMContentLoaded ou de carregamento sejam acionados. Sendo que, o último comportamento pode ser muito problemático em situações em que é importante que seu código seja executado antes de qualquer JavaScript incluído em uma página.

Perdi um tempo precioso tentando fazer a injeção do meu JS funcionar através do webdriver com Selenium, sem sucesso :cry:. Depois de muitas horas tentando, comecei a pensar em outras formas de fazer a requisição do pdf. Dado que é um formulário de download do pdf é submetido via post comecei a pesquisar como fazer isso, e finalmente cheguei até o método post do requests :sunglasses:. Depois que consegui fazer o download do pdf usando o requests com post foi só alegria, e a partir dai as demais etapas do projeto fluíram legal.

Optei por receber um valor do tipo data na função principal, e depois transformá-lo na string a ser utilizada pela url da página, assumindo que o tratamento de erros neste caso se dá de forma mais adequada.

## Fontes Úteis

Tive que pesquisar bastante coisa pra me certificar de como usar tudo que eu precisava pra fazer o projeto funcionar. Segue as minhas fontes:

1. [Funcionamento do BeautifulSoup](https://imasters.com.br/back-end/aprendendo-sobre-web-scraping-em-python-utilizando-beautifulsoup)

2. [Request com POST](https://code.tutsplus.com/tutorials/how-to-download-files-in-python--cms-30099)

3. [Manipulação de String necessária para extrair o id dos pdfs](https://wiki.python.org.br/ManipulandoStringsComPython)

3. [Hash MD5](https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file)

4. [Gravando arquivo CSV](https://pt.stackoverflow.com/questions/302281/salvar-dados-em-um-arquivo-csv)

5. [Path genérico para salvar os resultados](http://www.devfuria.com.br/python/os-path/)

6. [Formatação de data](https://pythonhelp.wordpress.com/2012/07/10/trabalhando-com-datas-e-horas-em-python-datetime/)


## Melhorias

Acredito que faltou ampliar a quantidade de testes, o tempo que tive acabou sendo mal aproveitado, consequentemente deixei a automatização dos testes para o final do projeto.
