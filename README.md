# Nostr Terminal Client

Um cliente **Nostr** para terminal, desenvolvido em **Python**, que exibe notas públicas em tempo real de múltiplos relays diretamente no terminal. As notas são mostradas com **painéis coloridos usando Rich**, proporcionando uma visualização clara e organizada.

---

## Funcionalidades

- Conecta a **múltiplos relays Nostr** simultaneamente
- Exibe notas públicas (`kind=1`) no terminal
- Painéis estilizados com **Rich**
- Feed contínuo em tempo real
- Estrutura modular: separa **UI, client e configuração de relays**

---

## Requisitos

- Python **3.14.2**
- Pacotes Python:

```bash
pip install -r src/requirements.txt
