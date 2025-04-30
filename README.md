# README

## Questão 1

- Criaria um serviço simples com FastAPI e um endpoint:
  - `GET /valida-cadastro?cnpj=...&cep=...`
- Centralizaria a lógica de comparação em um serviço de validação.
- Usaria o padrão Adapter para os provedores de CEP:
  - `BrasilCepAdapter`, `ViaCepAdapter`
  - Ambos implementariam a mesma interface com o método `get_address()`.
- Para garantir resiliência:
  - Criaria um decorator customizado de retry com delay e número de tentativas.
  - Após X tentativas, faria fallback automático para o segundo provedor.
  - Poderia usar a lib `tenacity`, mas optaria pelo decorator pela simplicidade do projeto.

## Questão 2

- Se possível, usaria um ETL para um data lake e faria a visualização a partir desse repositório.
- Caso precise implementar via código:
  - Capturaria os dados relevantes via uma task assíncrona.
  - Enviaria os eventos para uma fila/mensagem (ex: Kafka, RabbitMQ).
  - Um microserviço separado processaria e salvaria os dados em um banco separado.
  - Usaria uma Dead Letter Queue (DLQ) para capturar eventos com falha e permitir reprocessamento posterior.

## Questão 3

- Faria testes de carga com Locust.io para validar suporte a 1.000 requisições por segundo com P99 de 30ms.
- Usaria Prometheus + Grafana (ou outra ferramenta de observabilidade) para monitoramento de latência, uso de CPU, memória e throughput.
- Testes a realizar:
  - Teste de carga sustentada
  - Teste de estresse (aumentando o volume até falha)
  - Teste de latência (P99)
  - Teste de falha (parar e reiniciar o agendador)
  - Teste de confiabilidade (verificar se eventos agendados não são perdidos ou duplicados)

## Questão 6

1. Variáveis e credenciais devem estar em um `config.ini` ou `.env`.
2. Separar a criação da instância da aplicação e do banco em funções ou arquivos distintos.
3. A função `task1(db)` está sendo chamada imediatamente em vez de ser passada como função anônima. Deveria ser `lambda: task1(db)`.
4. A variável `task_instance` não é usada e pode ser removida.
5. A query do banco poderia usar o ORM, e mesmo sendo SQL bruto, deveria estar dentro de um bloco `try/except`.
6. No loop `for` de `orders`, poderia ser usado `enumerate` para controle do índice.
7. Algumas questões de linter como espaçamento entre funções, nomes de variáveis e organização do código poderiam ser melhoradas.

## Questão 7

- Uso comum do padrão Adapter com interfaces base usando abc do Python:

```python
from abc import ABC, abstractmethod

class MessageService(ABC):
    @abstractmethod
    def send_message(self, to, message):
        pass
