# 🐍 Flask Customer Manager

Um projeto simples em Flask desenvolvido para estudar e praticar conceitos fundamentais de back-end com Python e banco de dados.  
O objetivo é criar uma aplicação simples de gestão de clientes, mas com base sólida e arquitetura limpa, servindo de ponto de partida para evoluções futuras.
O projeto é apenas para estudo e desenvolvimento pessoal, o projeto ainda está simples porém pretendo melhorar cada vez mais, evoluindo como programador.

---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Flask** — framework web principal
- **Peewee ORM** — para integração com banco de dados
- **SQLite** (local) — para armazenamento de dados durante o desenvolvimento
- **HTML + Jinja2** — templates dinâmicos
- **Bootstrap** — estilização básica

---

## 🧱 Estrutura do Projeto

```bash
myproject/
│
├── main.py                     # Ponto de entrada da aplicação Flask
├── configuracao.py              # Configuração geral da aplicação
│
├── database/                    # Módulo de banco de dados
│   ├── __init__.py
│   ├── database.py              # Conexão com o banco
│   └── models/
│       └── cliente.py           # Modelo Cliente
│
├── routes/                      # Rotas da aplicação
│   └── cliente.py
│
├── templates/                   # Páginas HTML
│   ├── lista_cliente.html
│   ├── form_cliente.html
│   ├── detalhes_cliente.html
│   └── item_cliente.html
│
└── .gitignore                   # Arquivos ignorados no repositório
⚙️ Funcionalidades
✅ Cadastrar novos clientes
✅ Listar todos os clientes
✅ Editar informações existentes
✅ Excluir registros
✅ Interface simples e responsiva

🌐 Próximos Passos
Implementar banco de dados em nuvem 

Adicionar autenticação de usuários

Criar API REST para integração externa

Publicar versão online

🧠 Sobre o Projeto
Esse projeto faz parte da minha jornada de aprendizado em Engenharia de Software, com foco em desenvolvimento back-end e inteligência artificial.
Toda evolução será registrada aqui no GitHub — então sinta-se à vontade pra acompanhar e deixar sugestões! 😎

📫 linkedin: https://www.linkedin.com/in/matheus-rover-300710352
💼 instagram: https://www.instagram.com/math.rover
📧 Email: rovermatheus@gmail.com
