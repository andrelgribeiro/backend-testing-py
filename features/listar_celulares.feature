Feature: Listar celulares
  Scenario: Listar todos os celulares
    Given que eu faço uma requisição para listar celulares
    Then a resposta deve conter uma lista de celulares

  Scenario: Listar celulares com ids específicos
    Given que eu faço uma requisição para listar celulares com ids "3,5,10"
    Then a resposta deve conter os celulares com ids "3,5,10"
