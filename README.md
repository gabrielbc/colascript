# Colascript

Script para atender a demanda de professores que desejam aplicar provas permitindo que seus alunos usem notebook e/ou celular como ferramenta, porém, sem consultar as respostas na internet.

## Funcionamento

Em momento anterior a prova, os endereços MAC de cada computador são registrados pelo professor. No dia da prova, os alunos se conectam em um roteador sem acesso a internet, e sua permanência nesse roteador é monitorada para que permaneçam sem acesso. Caso conectem-se em outra rede, um arquivo de log é registrado e um aviso é disparado com o nome do aluno.

## Utilização

As instruções seguintes se referem a utilização do script.

### Pré-Requisitos

O que será preciso:

* Uma máquina com Ubuntu
* Python 2.7
* arp-scan
* Roteador


### Instalação

O script foi testado em uma máquina com Ubuntu 16.04, que já vem com o Python 2.7 instalado. Para o arp-scan, abra o terminal (ctrl + alt + t) e execute o comando:

```
sudo apt-get install arp-scan
```

### Aplicação

1. Configurar uma rede wifi no roteador
2. Solicitar o endereço MAC dos aparelhos dos alunos
3. Gravar os nomes e respectivos MAC's em arquivo chamado alunos.csv, como no exemplo a seguir:
```
alunos.csv

José,44:80:eb:91:f3:cd
Maria,45:40:ab:71:f3:cc
Pedro,44:80:ea:21:f4:fc
```

4. Conectar o roteador na tomada (apenas na energia), e solicitar que os alunos conectem na rede.
5. Iniciar o programa pelo terminal
```
sudo python main.py
```
6. O monitoramento é iniciado. Se tudo estiver correto, o output "Todos alunos conectados" aparecerá na tela, senão, o nome dos alunos que saíram da rede.
7. Ao final da execução, o arquivo log.txt apresentará os registros para análise, com desconexões junto ao nome e a hora do ocorrido.
8. CTRL + c para finalizar o programa.

## Licença

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
