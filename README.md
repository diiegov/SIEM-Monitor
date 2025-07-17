
🔐 SIEM Monitor – Sistema de Monitoramento de Eventos de Segurança

Este projeto é uma API desenvolvida com FastAPI que simula um SIEM (Security Information and Event Management),
com o objetivo de registrar e consultar eventos de segurança em tempo real.

🎯 Objetivo

O projeto tem como finalidade demonstrar como um sistema de monitoramento de logs de segurança pode ser construído com Python,
utilizando uma estrutura enxuta e moderna, ideal para fins didáticos e portfólio profissional.

⚙️ Funcionalidades

- ✅ Criar logs de eventos de segurança
- ✅ Listar todos os logs registrados
- ✅ Buscar logs por ID
- 🚧 Atualização e exclusão de logs (em versões futuras)

🛠️ Tecnologias utilizadas

- Python 3.11+
- FastAPI – Framework moderno para APIs
- Uvicorn – Servidor ASGI leve
- SQLAlchemy – ORM para manipulação do banco
- SQLite – Banco de dados leve

🚀 Passo a passo para rodar o projeto

1. Clone o repositório

git clone https://github.com/diiegov/SIEM-Monitor
cd siem-monitor

2. (Opcional) Crie e ative um ambiente virtual

# Criar ambiente virtual
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ou no Linux/macOS
source venv/bin/activate

3. Instale as dependências

pip install -r requirements.txt

4. Estrutura do projeto

siem-monitor/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # Arquivo principal com rotas da API
│   ├── crud.py              # Funções de acesso ao banco
│   ├── models.py            # Modelos SQLAlchemy
│   ├── schemas.py           # Pydantic schemas
│   └── database.py          # Conexão com SQLite
│
└── requirements.txt         # Dependências

5. Execute o projeto localmente

uvicorn app.main:app --reload

Acesse no navegador:

http://127.0.0.1:8000/docs → Interface interativa (Swagger UI)
http://127.0.0.1:8000/redoc → Documentação alternativa (ReDoc)

🧪 Como testar a API

Criar um log (POST)

curl -X 'POST' \
  'http://127.0.0.1:8000/logs' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "origem": "Firewall",
  "mensagem": "Tentativa de acesso não autorizada detectada",
  "nivel": "alto"
}'

Listar todos os logs (GET)

curl -X 'GET' http://127.0.0.1:8000/logs

Buscar log por ID (GET)

curl -X 'GET' http://127.0.0.1:8000/logs/1

📘 Licença

Este projeto está sob a licença MIT.
Você pode usá-lo, modificar e compartilhar à vontade.
