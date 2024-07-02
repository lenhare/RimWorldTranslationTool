# RimWorld Translation Tool with Google Cloud Translate

## Descrição

O **RimWorld Translation Tool with Google Cloud Translate** é uma ferramenta projetada para automatizar e simplificar o processo de tradução do jogo RimWorld para diferentes idiomas. Utilizando a API do Google Cloud Translate, esta ferramenta facilita a extração, tradução e inserção de textos do jogo, assegurando traduções rápidas e precisas.

## Funcionalidades

- **Extração de Texto:** Extrai textos de arquivos XML do RimWorld para facilitar a tradução.
- **Tradução Automática:** Utiliza a API do Google Cloud Translate para traduzir textos de forma automática e eficiente.
- **Suporte a Múltiplos Idiomas:** Suporta traduções para uma ampla variedade de idiomas, incluindo Português Brasileiro, Espanhol, Francês, Alemão, entre outros.
- **Inserção de Texto:** Insere os textos traduzidos de volta nos arquivos XML do jogo.
- **Configuração Personalizável:** Permite configurações personalizadas para atender às necessidades específicas dos tradutores.

## Requisitos

- Conta no Google Cloud Platform com acesso à API do Google Cloud Translate.
- Python 3.7 ou superior.
- Bibliotecas Python necessárias (listadas no arquivo `requirements.txt`).

## Como Usar

1. **Clone o Repositório:**
    ```bash
    git clone https://github.com/seu-usuario/rimworld-translation-tool.git
    cd rimworld-translation-tool
    ```

2. **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure a API do Google Cloud Translate:**
    - Siga as instruções [aqui](https://cloud.google.com/translate/docs/setup) para configurar a API.
    - Salve a chave JSON de autenticação como `google_credentials.json` no diretório do projeto.

4. **Execute a Ferramenta:**
    ```bash
    python translate.py --input ../RimWorld-Original/DefInjected --output ../RimWorld-Translated/DefInjected --lang pt
    ```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
