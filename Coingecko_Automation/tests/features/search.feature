Feature: Coingecko search bar

  Scenario: Search for coins
     Given I am on home page
      When I search for Bitcoin
      Then page should display Bitcoin page