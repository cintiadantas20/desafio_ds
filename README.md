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












## Overview

This is data science project which addresses 


## Requirements

this project requires
- docker
- python 3.8 to 3.10
- kedro 0.18

### Setting up

Create a virtual environment by running `python -m venv venv`. To activate the virtual environment, run `.\venv\Scripts\Activate.ps1`on Windows or `source .\venv\Scripts\Activate` on Linux

When first cloning, make sure to install requirements either using:

`pip install src/requirements.txt`

Check if installation was succesful by running: `kedro --version`

Finally copy the file conf/base/globals.yaml to conf/local/locals.yaml
and set up your username. Your username here will define path prefixing on databricks file system and mlflow experiments.
E.g if you set username to john.doe, your experiment at databricks mlflow will be:

```
/Users/john.doe/databricks_base_project
```

### Experimentation & version control

Versioning is done with git. The project (loosely) follows trunk based development, which means there is a `main` branch with production code and new changes target it directly. 

[Experiments](https://wiki.indicium.tech/en/dados/data-science/ml-ops#experimentos) changes made to the pipeline's code with the objective of improving model performance. The experimentation process starts with identifying an improvement opportunity and ends with the code changes addressing the opportunity merged to the `main` branch.  

`git checkout -b experiment/short_experiment_description`

When creating the pull request, a ci execution will build the project and run the steps needed to train a model and generate performance metrics - on training and out of sample data as well! This is done using Bitbucket pipelines and the goal is to **provide reviewers with more context on how code changes affect model performance.**

Changes that are not experiment related - such as workflow changes or documentation updates - should be developed in branches with the following pattern:

`git checkout -b short_description_of_changes_made`

⚠️ Prefer short commits with clear messages of what the commit changes.

***

## About the dataset

### Machine Predictive Maintenance Classification Dataset

Since real predictive maintenance datasets are generally difficult to obtain and in particular difficult to publish, we present and provide a synthetic dataset that reflects real predictive maintenance encountered in the industry to the best of our knowledge.

The dataset consists of 10 000 data points stored as rows with 14 features in columns

* UID: unique identifier ranging from 1 to 10000
* productID: consisting of a letter L, M, or H for low (50% of all products), medium (30%), and high (20%) as product quality variants and a variant-specific serial number
* air temperature [K]: generated using a random walk process later normalized to a standard deviation of 2 K around 300 K
process temperature [K]: generated using a random walk process normalized to a standard deviation of 1 K, added to the air temperature plus 10 K.
* rotational speed [rpm]: calculated from powepower of 2860 W, overlaid with a normally distributed noise
* torque [Nm]: torque values are normally distributed around 40 Nm with an Ïƒ = 10 Nm and no negative values.
* tool wear [min]: The quality variants H/M/L add 5/3/2 minutes of tool wear to the used tool in the process. 
* 'machine failure' label that indicates, whether the machine has failed in this particular data point for any of the following failure modes are true.

Important : There are two Targets - Do not make the mistake of using one of them as feature, as it will lead to leakage.

Target: Failure or Not
Failure Type: Type of Failure

***

## Kedro's rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://kedro.readthedocs.io/en/stable/faq/faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

### How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

### How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

To configure the coverage threshold, go to the `.coveragerc` file.


### How to run this project on Databricks

Assuming you have a Databricks account access and your Databricks git credentials,
add this repo to your repos and open the file notebooks/databricks_kedro_runner
at this notebook you'll find 3 cells:

Install python requirements at your notebook environment

```python
pip install -r ../src/requirements.txt
```

Make your notebook pick changes in other notebooks/files without refreshing and load kedro session objects:

```python
%load_ext autoreload
%autoreload 2
%load_ext kedro.ipython
```

And finally a cell that runs your pipeline
All this empty vars are there to show that you can pass any of the kedro cli run parameteres setting values to this vars.

```python
# If you change something at the catalog or any of the conf files, you should reload kedro objects
# You can uncomment the following line and execute this cell to reload kedro
# %reload_kedro

# Running default Pipeline without any params:

env = No    ne
params = None
tag = None
node_names = []
from_nodes = None
to_nodes = None
from_inputs = None
to_outputs = None
load_version = None
pipeline = None


session.run(
    tags=tag,
    node_names=node_names,
    from_nodes=from_nodes,
    to_nodes=to_nodes,
    from_inputs=from_inputs,
    to_outputs=to_outputs,
    load_versions=load_version,
    pipeline_name=pipeline,
)
```

### How to test this project on Databricks

Open the file notebooks/databricks_test_runner,
at this notebook you'll also find 3 cells:

```python
pip install -r ../src/requirements.txt
```

Make your notebook pick changes in other notebooks/files without refreshing:

```python
%load_ext autoreload
%autoreload 2
```

Run tests:

```python
import pytest
import os
import sys


os.chdir("..")
print(os.getcwd())

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

# Run pytest.
retcode = pytest.main([".", "-v", "-p", "no:cacheprovider"])

# Fail the cell execution if there are any test failures.
assert retcode == 0, "The pytest invocation failed. See the log for details."
```

#### How to ignore notebook output cells in `git` NOT DATABRICKS, BUT MAYBE IT MAKES SENSE FOR DATABRICKS TOO
To automatically strip out all output cell contents before committing to `git`, you can run `kedro activate-nbstripout`. This will add a hook in `.git/config` which will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

### Package your Kedro project

[Further information about building project documentation and packaging your project](https://kedro.readthedocs.io/en/stable/tutorial/package_a_project.html)


### CI/CD

We are running the pipelines in databricks cluster using [dbx](https://dbx.readthedocs.io/en/latest/)
We need to set up two pipeline vars to use databricks api via dbx:

- DATABRICKS_HOST
- DATABRICKS_TOKEN

#### Test pipeline

The test pipeline runs the test_entrypoint.py file at tests/pipelines/.
This file exists so dbx can have an entry point defined at the deployment.yaml file.
The deployment.yaml file sets up tasks and worfklows that will run at databricks and is placed at conf/deployment.yaml
you can find more info [here](https://dbx.readthedocs.io/en/latest/reference/deployment/)

#### Report pipeline

The report pipeline actually runs the whole pipeline and register its results as an mlflow experiment
When we run this pipeline we will log the results of our pipeline at a experiment in databricks at:

```
/Shared/dbx/databricks_base_kedro_classification_project/
```

Experiments are configured at conf/{env}/mlflow.yml

Databricks experiment link:

https://dbc-367add7f-147d.cloud.databricks.com/?o=2615207362795523#mlflow/experiments/1373316213505283?searchFilter=&orderByKey=attributes.start_time&orderByAsc=false&startTime=ALL&lifecycleFilter=Active&modelVersionFilter=All%20Runs&selectedColumns=attributes.%60Source%60,attributes.%60Models%60,tags.%60dbx_action_type%60,tags.%60dbx_branch_name%60,tags.%60dbx_environment%60,tags.%60dbx_status%60&runsExpanded[c25889176f47440eab393cb2364ba0ee]=false&isComparingRuns=false

##TODO
separar os requirements por env: local ci run
melhorar no settings.py como eu to pegando ali o path
cluster name deveria ser variavel
quebrar linhas do dbx execute no pipeline develop
noa usar mlflow como uploader