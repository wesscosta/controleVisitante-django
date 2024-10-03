# controleVisitante-django
Projeto django de controle de visitante
STEP

### Clonar o Repositorio do GitHub
01. git clone https://github.com/wesscosta/controleVisitante-django.git

### Acessar o repositorio do projeto
02. cd controleVisitante-django.git

### Cria o ambiente virtual
03. python -m venv .env

#### Ativar o ambiente virutal
03. .\.env\Script\activate

### Instalar os pacotes e dependencias
04. pip install -r .\requirements.txt

### Realizar as migrações
05. python .\manage.py makemigrations
06. python .\manage.py migrate

### Criação do superusuario
07. python .\manage.py createsuperuser

### Start o Projeto
08. python .\manage.py runserver


