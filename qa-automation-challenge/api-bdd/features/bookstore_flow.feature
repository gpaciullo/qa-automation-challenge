
Feature: DemoQA BookStore API - Fluxo end-to-end
  Como avaliador do desafio
  Eu quero rodar um cenário BDD que encadeia as chamadas de API
  Para validar o fluxo principal do BookStore

  Scenario: Criar usuário, autorizar, listar e adicionar dois livros
    Given que eu possuo credenciais válidas
    When eu crio um novo usuário
    And eu gero um token de acesso
    And eu verifico a autorização do usuário
    And eu consulto a lista de livros disponíveis
    And eu adiciono dois livros ao usuário
    Then o usuário deve conter exatamente esses dois livros
