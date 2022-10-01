# project_afred
Project Alfred é o meu gestor de gastos. 

O servidor de mysql usado para o teste foi o XAMPP

Link para download: https://www.apachefriends.org/download_success.html

Após baixar e instalar o xampp, basta executa-lo e ligar o servidor mysql

Quando ligar o servidor mysql, acesse o CMD e rode os comandos abaixo.

--------- Criar um ambiente virtual ---------

python -m venv venv_alfred

--------- Levantando ambiente virtual ---------

venv_alfred\Scripts\activate

--------- Instalando dependencias ---------

pip install -r alfred\requirements.txt

--------- Instalando o projeto ---------

cd project_alfred

python project_up.py

--------- Lnaçando um valor ---------

python main.py

==================== A TITULO DE TESTE, SEGUE UM LINK DA RECEITA FEDERAL ====================

http://www.fazenda.pr.gov.br/nfce/qrcode?p=41220676430438003944650050002119801005433332%7C2%7C1%7C1%7CB5138FF4C7FFA7136AFAD791C72BC9C474EC753C
