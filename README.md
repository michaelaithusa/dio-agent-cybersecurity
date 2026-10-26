# DIO Agent - Cibersegurança & AppSec Mentor 🛡️🤖

Este repositório contém uma especialização do projeto **DIO Agent**, evoluído para atuar como um Mentor de Cibersegurança. O objetivo deste projeto foi unir o uso prático de Agentes de IA Autônomos com a análise de vulnerabilidades, simulando o dia a dia de operações de segurança, Cloud e GRC.

## 🎯 A Especialização
O agente foi treinado (via arquivos de contexto e *skills*) para não apenas corrigir códigos, mas para atuar como um profissional de Segurança da Informação. Antes de dar respostas prontas, ele:
1. Avalia o ambiente e coleta contexto.
2. Determina Impacto, Probabilidade e Severidade da falha.
3. Mapeia o vetor de ataque no framework **MITRE ATT&CK**.
4. Educa o usuário sobre os princípios da Tríade CID e Defesa em Profundidade.

**Por que essa especialização?**
Para criar uma ponte prática entre desenvolvimento e segurança contínua (DevSecOps), mostrando como Agentes de IA podem acelerar a análise técnica de Blue Teams e apoiar a implementação de processos de Governança, Risco e Conformidade (GRC).

## 📂 Arquivos Criados / Modificados

- `skills/vulnerability-analysis/SKILL.md`: O roteiro de atuação do agente, definindo o fluxo obrigatório de análise de risco.
- `skills/vulnerability-analysis/README.md`: Documentação da nova skill.
- `agent/knowledge/security-basics.md`: Injeção de conhecimento contendo os fundamentos de Cibersegurança.
- `agent/persona.md`: Adição de traços de personalidade focados em Blue Team e AppSec.
- `AGENTS.md`: Registro da nova skill na tabela do agente.
- `app_vulneravel.py` e `app_seguro.py`: Códigos de laboratório para testes práticos de SQL Injection.

## 🚀 Como rodar o projeto
1. Clone este repositório.
2. Certifique-se de ter o **Hermes** instalado no seu ambiente.
3. Abra o terminal na raiz da pasta do projeto e inicie o agente.
4. Peça para ele analisar o arquivo `app_vulneravel.py` ou descreva um cenário de infraestrutura vulnerável.

---
*Projeto desenvolvido para o Bootcamp da Digital Innovation One.*
