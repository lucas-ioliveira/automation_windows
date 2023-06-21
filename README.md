# Projeto de automatização de tarefas

- O projeto consiste em automatizar uma tarefa que faço diariamente que é excluir arquivos "inúteis/temporários" que acabam acumulando e ocupando memória da minha máquina e a deixando lenta para uso.

- O script é um execultável e roda alguns comandos do sistema operacional Windows que faz essa limpeza de arquivos.
  - Para gerar um executável basta rodar os seguintes comandos:
  - no diretório do projeto abra o terminal, certifique-se se o ambiente virtual está ativo e instale a lib para gerar o arquivo.exe (pip install cx-Freeze)
  - E por fim rode o comando cxfreeze app.py isso irá gerar o execultável.

- O script foi realizado para rodar somente na minha máquina, pois está sendo usado uma biblioteca que capta a posição do mouse ou seja cada notebook tem uma resolução de tela diferente e para funcionar em outras máquinas é necessário realizar esses ajustes.