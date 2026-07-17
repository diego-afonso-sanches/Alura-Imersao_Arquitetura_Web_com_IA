# Álbum Digital de Figurinhas Tech

Este projeto é um álbum interativo de figurinhas digitais inspirado na Imersão em Arquitetura Web com IA da Alura. A aplicação combina um frontend visual e animado com um backend em FastAPI para servir as figurinhas e suas imagens.

## 🚀 Objetivo

Criar uma experiência de álbum de figurinhas com:

- navegação em estilo livro com efeito de virar páginas;
- carregamento dinâmico das figurinhas via API;
- exibição de imagens e informações das figurinhas;
- uma interface responsiva e visualmente envolvente.

## 🧱 Estrutura do projeto

- backend/: aplicação FastAPI responsável por expor os dados das figurinhas e servir as imagens.
- frontend/: interface web do álbum, com HTML, CSS e JavaScript.

## 🛠️ Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- HTML, CSS e JavaScript
- St.PageFlip
- Web Audio API

## ▶️ Como executar

### 1. Backend

Acesse a pasta do backend e instale as dependências:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
pip install fastapi uvicorn
```

Em seguida, inicie o servidor:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

A API ficará disponível em:

- http://localhost:8000/figurinhas
- http://localhost:8000/figurinhas/{id}/imagem

### 2. Frontend

Abra o arquivo abaixo em um navegador ou use uma extensão como Live Server:

```bash
frontend/index.html
```

O frontend consome a API local do backend na porta 8000.

## 📦 Funcionalidades principais

- visualização de um álbum com páginas interativas;
- carregamento automático das figurinhas a partir da API;
- suporte a navegação por teclado e botões;
- efeito sonoro ao virar página;
- exibição das imagens armazenadas no backend.

## 📚 Observações

As imagens das figurinhas estão localizadas na pasta backend/figurinhas e são servidas pelo backend.

## 👤 Autor

Projeto desenvolvido como parte da Imersão Arquitetura Web com IA da Alura.
