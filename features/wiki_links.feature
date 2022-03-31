Feature: Users who speak different languages should be able to read articles in their own language

  Scenario: As a Spanish speaker, I want to be able to visit the spanish wikipedia, so that I can understand the articles
    Given I am on the Wikipedia homepage
    When I click on the Spanish link
    Then I am on the Spanish Wikipedia page