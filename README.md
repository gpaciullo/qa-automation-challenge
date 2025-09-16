
# QA Automation Challenge – Accenture (DemoQA)  🧪🚀

[![API Tests](https://github.com/USER/qa-automation-challenge/actions/workflows/ci.yml/badge.svg)](https://github.com/USER/qa-automation-challenge/actions/workflows/ci.yml)

Repositório com duas camadas de automação:
- **`api-tests/`** → Python + Pytest + Requests (fluxo E2E do BookStore).
- **`frontend-tests/`** → Cypress + Page Objects (smokes de UI).

> Substitua `USER` na badge pelo seu usuário do GitHub após fazer o push.

---

## 🎯 Objetivos do desafio
**Parte 1 (API)** – Fluxo encadeado:
1. Criar usuário (`POST /Account/v1/User`)
2. Gerar token (`POST /Account/v1/GenerateToken`)
3. Verificar autorização (`POST /Account/v1/Authorized`)
4. Listar livros (`GET /BookStore/v1/Books`)
5. Adicionar 2 livros (`POST /BookStore/v1/Books`)
6. Consultar usuário e validar os livros (`GET /Account/v1/User/{userID}`)

**Parte 2 (Frontend)** – Smokes visuais:
- Listagem e busca de livros
- Tela de login presente e interagível

---

## 🏗️ Stack
**API:** Python 3.10+, Pytest, Requests, python-dotenv  
**Frontend:** Node 18+, Cypress 13

---

## ▶️ Como executar localmente

### API
```bash
cd api-tests
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

### Frontend (Cypress)
```bash
cd frontend-tests
npm install
npx cypress open      # modo interativo
# ou
npx cypress run       # modo headless
```

---

## ⚙️ Variáveis (.env) – opcional
Crie `api-tests/.env` (com base em `.env.example`) para fixar credenciais/base URL.  
Por padrão, os testes **geram usuário/ senha válidos automaticamente** a cada execução.

---

## 🧱 Arquitetura e padrões
- Encapsulamento HTTP via `DemoQAClient` (requests.Session)
- Testes organizados por camadas (`tests/`, `src/`)
- Page Objects no Cypress (`cypress/e2e/pages`)
- Fácil extensão para BDD (Cucumber/Behave) e Page Object Model no backend

---

## 🧪 Relatórios
- **Pytest** gera JUnit XML em `api-tests/reports/pytest-junit.xml` (consumido no CI).
- **Cypress** salva vídeos e screenshots automaticamente no CI (artefatos).

> **Allure (opcional):** pode ser habilitado (instruções abaixo), mas o CI já funciona sem.

---

## 🤖 CI (GitHub Actions)
Pipeline único que executa API e Frontend em cada push/PR, publica artefatos (JUnit, vídeos e screenshots).  
O arquivo está em **`.github/workflows/ci.yml`**.

### Como habilitar a badge
1. Faça o **push** do repositório para o GitHub.
2. Edite a URL da badge no topo deste README, trocando `USER` pelo seu usuário/orga.

---

## 🧴 Allure Reports (opcional)
Para habilitar:
1. Instale `allure-pytest` no `api-tests/requirements.txt`:
   ```txt
   allure-pytest==2.13.5
   ```
2. Rode local:
   ```bash
   pytest --alluredir=reports/allure-results
   allure serve reports/allure-results
   ```
3. No CI (passos comentados em `.github/workflows/ci.yml`) gere resultados e publique como artefato.

---

## 📁 Estrutura
```
qa-automation-challenge/
├─ api-tests/
│  ├─ requirements.txt
│  ├─ pytest.ini
│  ├─ .env.example
│  ├─ src/
│  │  ├─ config.py
│  │  └─ client/api_client.py
│  └─ tests/
│     ├─ conftest.py
│     └─ test_bookstore_flow.py
├─ frontend-tests/
│  ├─ package.json
│  ├─ cypress.config.js
│  └─ cypress/
│     └─ e2e/
│        ├─ bookstore_ui.cy.js
│        └─ pages/{BooksPage.js, LoginPage.js}
└─ .github/workflows/ci.yml
```


---

## 🧩 BDD (Behave) — Parte 1 (API)
Pasta: `api-bdd/`

### Como executar
```bash
cd api-bdd
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
behave -f pretty -f junit -o reports/junit
```
Gere credenciais dinamicamente por execução ou configure `.env` com `DEMOQA_USERNAME`, `DEMOQA_PASSWORD`, `DEMOQA_BASE_URL`.


---

### 🤖 CI — Job BDD
Agora o pipeline também executa o job **api-bdd** com Behave, gerando relatórios JUnit em cada push/PR.  
Os resultados ficam disponíveis nos artefatos do GitHub Actions (`bdd-junit`).


### 📈 Allure para BDD (Behave)
Para gerar resultados do Allure localmente:
```bash
cd api-bdd
pip install -r requirements.txt
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results -f pretty
# Visualizar local (se tiver o Allure commandline instalado):
allure serve reports/allure-results
```
Nota: o CI já publica `reports/allure-results` como artefato.
