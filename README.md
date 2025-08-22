# Desafio 3S

Este projeto é uma solução fullstack para desafios técnicos, combinando **React** no frontend, **FastAPI** no backend e **Docker** para orquestração. Ele foi desenvolvido com foco em organização, escalabilidade e boas práticas de arquitetura.

---

## ✨ Principais Diferenciais

- **Backend com Padrão Strategy:**  
  O backend utiliza o padrão de projeto Strategy para encapsular diferentes regras de negócio (validação de string, sequência, tabuleiro e benefícios), facilitando a manutenção e a extensão do sistema.
- **Frontend Modular e Reutilizável:**  
  O frontend React é organizado em funções e utilitários reutilizáveis, promovendo clareza e facilidade de manutenção.
- **Containerização Profissional:**  
  Todo o ambiente roda em containers Docker, garantindo portabilidade e facilidade de setup.
- **Comunicação Segura via API REST:**  
  O frontend se comunica com o backend por meio de endpoints REST bem definidos, com validações robustas.

---

## 🚀 Funcionalidades

- **Desafio 1:** Validação de string (ex: palíndromos, padrões, etc)
- **Desafio 2:** Validação de sequência numérica
- **Desafio 3:** Validação de tabuleiro de jogo
- **Desafio 4:** Cálculo de benefícios trabalhistas

---

## 🛠️ Tecnologias Utilizadas

- **Frontend:** React + TypeScript + Nginx
- **Backend:** FastAPI + Python (com Strategy Pattern)
- **Containerização:** Docker & Docker Compose

---

## 📁 Estrutura do Projeto

```
desafio_3S/
├── backend/
│   ├── api/
│   ├── core/
│   ├── src/
│   │   └── challenges/
│   │       └── string_challenge.py  # Exemplo de Strategy Pattern
│   ├── Dockerfile
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   └── utils/
│   │       └── validators.ts
│   ├── nginx.conf
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🧠 Padrões e Boas Práticas

### Backend (FastAPI)
- **Strategy Pattern:**  
  Cada desafio (string, sequência, tabuleiro, benefícios) é implementado como uma estratégia independente, facilitando a adição de novas regras sem alterar o core da aplicação.
- **Validações com Pydantic:**  
  Todos os dados de entrada são validados com modelos Pydantic, garantindo segurança e integridade.

### Frontend (React)
- **Componentização sugerida:**  
  Cada desafio pode ser extraído para um componente próprio, tornando o código mais limpo e reutilizável.
- **Funções utilitárias:**  
  Validações comuns (números, datas) ficam em `utils/validators.ts`, evitando repetição.
- **Estilo centralizado:**  
  Uso de estilos inline e possibilidade de migração para CSS Modules ou Styled Components.

---

## 🐳 Como rodar

1. **Pré-requisitos:**  
   - Docker e Docker Compose instalados

2. **Suba o projeto:**  
   No diretório raiz, execute:
   ```bash
   docker compose up --build
   ```

3. **Acesse o frontend:**  
   - [http://localhost](http://localhost)

4. **Acesse o backend (Swagger):**  
   - [http://localhost:8001/docs](http://localhost:8001/docs)

---

## 💡 Como usar

- Escolha um desafio no menu lateral.
- Preencha os campos conforme o desafio.
- Clique em "Validar" ou "Calcular".
- O resultado será exibido na tela.

---

## 📌 Observações

- O projeto está pronto para produção e desenvolvimento local.
- Para evoluir, basta adicionar novas estratégias no backend e novos componentes no frontend.
- Código limpo, modular e fácil de manter.

---

**Desenvolvido para o desafio técnico S3, com foco em arquitetura, escalabilidade e experiência do usuário.**
