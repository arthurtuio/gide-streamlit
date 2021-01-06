# GIDE Streamlit Webpage #

Este repo contém o código necessário para de uma interface web para a GIDE, 
usando a biblioteca Streamlit, de Python.

## Arquivos que você vai encontrar nesse repo ##
- `main_page.py`: Código principal do repositório. É nele que a página web será sempre inicializada;
- `Procfile`: Arquivo necessário para que esse repo rode no Heroku (servidor web);
- `setup.sh`: Outro arquivo necessário para que esse repo rode no Heroku (servidor web);
- `requirements.txt`: Arquivo contendo as bibliotecas usadas neste repositório
- pasta lib: Contém diversos códigos auxiliares para a página web, tanto para realizar a comuinicação com a 
  API da GIDE, quanto acessar outras partes da página web, de forma que deixando eles lá, o código principal
  (app.py) fica bem abstrato, e mais fácil de ser entendido.

## Explicando como funciona o Streamlit ##
Por sorte, existe um tutorial da Python Brasil 2020 100% focado em ensinar como
usar essa biblioteca, e já fazer o deploy da mesma na web usando Heroku. O link é esse:
https://streamlit-heroku-python-br2020.herokuapp.com/
Quem criou foi o @arthurtuio, qualquer dúvida só falar com ele

## Próximos passos ## 
- Depende primeiro da lógica de cálculo da GIDE, que vai pro repositório da API.
Feito isso lá, o próximo passo é adicionar uma lógica de frontend aqui.