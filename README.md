#  Gerenciador de Biblioteca

##  Objetivo
Este projeto tem como objetivo desenvolver um sistema simples de *gerenciamento de biblioteca, aplicando conceitos de **Engenharia de Software* como versionamento, testes automatizados, documentação e gestão de tarefas no GitHub.

---
#  Escopo do Projeto

###  Escopo Incluído
- Cadastro de livros com título, autor e ano.
- Listagem completa dos livros cadastrados.
- Busca de livros por título (case-insensitive).
- Controle de empréstimo e devolução (status: disponível/emprestado).
- Testes automatizados para validar funcionalidades básicas.
- Documentação inicial (README com objetivo, funcionalidades, entrevista e metodologia).
- Gestão de tarefas via GitHub (Issues, Kanban, Pull Requests).

###  Fora do Escopo (nesta versão inicial)
- Controle de usuários (quem pegou o livro emprestado).
- Relatórios avançados (estatísticas de uso, histórico de empréstimos).
- Interface gráfica ou web (o sistema roda apenas em terminal).
- Acesso simultâneo por múltiplos usuários.
- Integração com banco de dados (atualmente usa listas em memória).

###  Possíveis Evoluções Futuras
- Adicionar controle de usuários e histórico de empréstimos.
- Criar relatórios e dashboards com estatísticas.
- Implementar interface web ou desktop.
- Persistência dos dados em banco de dados.

## Funcionalidades
- Cadastro de livros (título, autor, ano).
- Listagem de livros disponíveis.
- Busca de livros por título.
- Empréstimo e devolução de livros.
- Testes automatizados para garantir qualidade.

---

##  Estrutura do Projeto
projeto/
├── src/              # Código fonte
│   └── main.py
├── tests/            # Testes automatizados
│   └── test_main.py
├── docs/             # Documentação e diagramas
└── README.md

---

##  Como executar
1. Clone o repositório:
   git clone https://github.com/marcosamambaia/engenharia-software-projeto.git
   cd engenharia-software-projeto

2. Execute o programa:
   python3 src/main.py

3. Rode os testes:
   python3 -m unittest tests/test_main.py

---

##  Gestão no GitHub
- *Issues:* cada funcionalidade ou bug é registrado como uma Issue.  
- *Projects (Kanban):* organização das tarefas em To Do, In Progress e Done.  
- *Pull Requests:* revisão de código antes de integrar na branch principal.  
- *Wiki:* documentação adicional (escopo, diagramas, regras de negócio).  
- *Actions (CI/CD):* execução automática dos testes em cada PR.

---

##  Metodologia
O projeto segue práticas ágeis:
- Desenvolvimento incremental.  
- Uso de Issues para rastreabilidade.  
- Revisão de código via Pull Requests.  
- Testes automatizados para garantir qualidade contínua.  

---

##  Entrevista com o Cliente (Levantamento de Requisitos)

*Pergunta 1:* Qual é o principal objetivo do sistema que você deseja?  
*Resposta:* Quero um sistema simples para gerenciar os livros da biblioteca, com cadastro, busca e controle de empréstimos.  

*Pergunta 2:* Quais informações precisam ser registradas sobre cada livro?  
*Resposta:* Título, autor e ano de publicação já são suficientes para começar.  

*Pergunta 3:* Você gostaria de ter uma funcionalidade de busca?  
*Resposta:* Sim, é essencial poder buscar livros pelo título, mesmo que seja só parte do nome.  

*Pergunta 4:* Como você imagina o controle de empréstimos?  
*Resposta:* Preciso saber se o livro está disponível ou emprestado, e registrar quando ele for devolvido.  

*Pergunta 5:* Deseja que o sistema registre quem pegou o livro emprestado?  
*Resposta:* No início não é necessário, basta saber se está emprestado ou não. Podemos evoluir depois.  

*Pergunta 6:* Você gostaria de relatórios ou listagens?  
*Resposta:* Sim, quero listar todos os livros cadastrados e também filtrar apenas os disponíveis.  

*Pergunta 7:* O sistema precisa ser acessado por várias pessoas ao mesmo tempo?  
*Resposta:* Não, por enquanto será usado apenas em um computador local.  

*Pergunta 8:* Você gostaria de ter testes automatizados para garantir a qualidade?  
*Resposta:* Sim, é importante que o sistema seja confiável e que cada funcionalidade seja validada.  

*Pergunta 9:* Como você gostaria que fosse a documentação do projeto?  
*Resposta:* Um README explicando objetivo, escopo e funcionalidades já ajuda bastante. Diagramas podem ser adicionados depois.  

*Pergunta 10:* Você pretende evoluir o sistema no futuro?  
*Resposta:* Sim, futuramente quero adicionar controle de usuários e histórico de empréstimos, mas por enquanto o básico já atende.