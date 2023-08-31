# Prevendo séries temporais do PIB para 2024-2028 com ARIMA e Kedro

Este projeto tem por finalidade prever os dados do PIB para os países para os anos de 2024 a 2028, utilizando análise de dados e modelos preditivos, comparando com os dados do dataset original fornecido. 

Para tanto, imputamos os dados faltantes com o algoritmo KNNImputer, utilizamos o modelo de previsão ARIMA e as métricas de avaliação RMSE, MAE e MAPE. Como framework do fluxo de desenvolvimento do projeto, usamos o Kedro

Para maiores detalhes sobre os dados, as análises, as técnicas empregadas e as decisões tomadas, por favor acesse os notebooks de EDA na pasta `desafio_ds/notebooks`.

## Como instalar
Nessa etapa, vamos descrever as instalações e os comandos a serem dados na linha de comando Linux. Antes, vale clonar este repositório com o comando:
```
git clone https://github.com/cintiadantas20/desafio_ds
```
- Ambiente virtual
Primeiro é necessário criar um ambiente virtual com este comando:
```
python -m venv venv
```
Depois, ative o venv:
```
source venv/bin/activate
```
- Kedro
Foi usado o framework Kedro, instalado com o comando:
```
pip install kedro
```
Após clonar o repositório, instale os pacotes necessários com este comando:
```
ip install -r src/requirements.txt
```
Verifique a instalação do kedro com um `kedro --version` na linha de comando.
É preciso ainda copiar o arquivo `conf/base/globals.yaml` e colar na pasta `conf/local/locals.yaml` e substituir o nome do usuário (`username`), como no exemplo:
```
/Users/`username`/desafio_ds/data/
```
## Como rodar
Após clonar o repositório, instalar os pacotes e configurar o arquivo `locals.yaml`, execute o comando `kedro run` no seu terminal e veja a mágica acontecer, se tudo der certo!

Sinta-se à vontade para testar novas formas de imputação de dados, novos modelos e comentar. Quanto à minha experiência, foi muito enriquecedor implementar este projeto no Kedro!

## Autora

- [@cintiadantas20](https://github.com/cintiadantas20)
- [@Cíntia Dantas](https://www.linkedin.com/in/cintia-dantas/)
