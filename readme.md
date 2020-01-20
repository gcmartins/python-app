## Python-app

Aplicação que retorna um JSON com a chave "extenso" cujo o valor é a versão por extenso do número inteiro enviado no path, como por exemplo:

Requisição:
``
http://localhost:3000/1
``

Resposta:
``
{ "extenso": "um" }
``

### Execução da imagem Docker
A aplicação pode ser executada pela imagem Docker pública "gcmartins/python-app" disponibilizada no Docker Hub executando:

``
docker run -p 8000:5000 gcmartins/python-app
``

Após executar a imagem, a API pode ser testada utilizando o browser ou o comando ``curl`` com a URL:

``
http://localhost:8000/<numero>
``

sendo ``<numero>`` igual a um numero inteiro entre [-99999, 99999].

Obs.: Caso se utilize o sistema operacional Windows com o DockerToolbox, o localhost da URL precisa ser substituído pelo IP da maquina virtual obtido pelo comando no terminal:

``
docker-machine ip
``