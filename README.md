# Link Checker Multi-thread

## Descrição

O **Link Checker Multi-thread** é um sistema que testa múltiplos links simultaneamente, verificando se estão ativos (**live**) ou inativos (**dead**). Utiliza múltiplas threads para otimizar a velocidade de verificação e exibe um contador dinâmico para acompanhar o progresso em tempo real.

## Tecnologias Utilizadas
- Python
- ThreadPoolExecutor para execução concorrente
- Requests para realizar as requisições HTTP
- Manipulação de arquivos para salvar os links ativos e inativos

## Como Funciona

1. O programa gera um identificador aleatório.
2. Ele faz uma requisição para a API do GoFile usando esse identificador.
3. Se o link for válido, ele é salvo no arquivo `live.txt`.
4. Se o link for inválido ou houver erro na requisição, ele é salvo no arquivo `dead.txt`.
5. O programa exibe um contador dinâmico mostrando a quantidade de testes realizados e os resultados.

## Instalação e Uso

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/link-checker-multithread.git
   cd link-checker-multithread
   ```

2. Execute o script:
   ```sh
   python main/api/extractData.py
   ```

## Configuração

- O token de autorização pode ser alterado dentro do script na variável `authorization`.
- O número de threads simultâneas pode ser ajustado no `ThreadPoolExecutor(max_workers=5)`. 

## Autor
Desenvolvido por [Daniel de Deus Souza](https://github.com/dnsouzadev).

## Licença
Este projeto está sob a licença MIT.
