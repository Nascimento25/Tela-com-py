# 1. Introdução

Este projeto apresenta um exemplo prático de como implementar um sistema de login utilizando a biblioteca PySimpleGUI, que permite a criação de interfaces gráficas simples com Python.

# 2. Objetivos

O objetivo principal deste projeto é desenvolver um sistema de login que permita:

* Receber entradas de usuário e senha.
* Validar as credenciais fornecidas pelo usuário.
* Exibir uma mensagem de boas-vindas caso as credenciais estejam corretas.
  
# 3. Metodologia

A metodologia adotada para o desenvolvimento do projeto inclui:

## 3.1 Ferramentas Utilizadas:

Linguagem de Programação: Python 3.
Biblioteca: PySimpleGUI para criação de interfaces gráficas.
## 3.2 Estrutura do Projeto: O sistema é composto por três principais componentes:

* Layout da Interface: Definição dos elementos visuais, como campos de entrada, botões e caixas de seleção.
* Janela do Sistema: Criação da janela principal onde o usuário interage com o sistema.
* Lógica de Autenticação: Verificação das credenciais inseridas pelo usuário para conceder ou negar acesso.

## 3.3 Implementação do Código: O código é estruturado em três etapas principais:

Importação e Configuração do Layout: O layout da GUI é configurado usando o PySimpleGUI, incluindo campos para entrada de nome de usuário e senha, e um botão de login.

Criação da Janela: A janela é criada com o layout definido, sendo exibida para o usuário interagir.

Lógica de Verificação de Credenciais: Ao clicar no botão "Entrar", o sistema verifica se o nome de usuário e senha correspondem aos valores predefinidos ('Marcos' e '1234'). Se as credenciais forem corretas, uma mensagem de boas-vindas é exibida.

# 4. Resultados
<img
  src="Captura de tela 2024-09-05 094430.png"
  alt="projeto em funcionamento"
  width="400"
  height="341" />
  
O sistema desenvolvido funciona conforme o esperado, permitindo a autenticação com credenciais válidas. A implementação demonstrou a capacidade da biblioteca PySimpleGUI de criar uma interface amigável e eficiente para o usuário final, com a facilidade de desenvolvimento rápido e integração com lógicas básicas de segurança.
# 5. Discussão
Embora o projeto tenha alcançado seus objetivos de criar um sistema de login funcional, ele possui limitações no que tange à segurança, como a ausência de proteção contra ataques de força bruta ou armazenamento seguro de credenciais. Para aplicações comerciais, a adoção de técnicas de criptografia e um backend seguro para o gerenciamento de usuários seriam necessárias.
