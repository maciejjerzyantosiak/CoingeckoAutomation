Feature: Coingecko search bar

  Scenario Outline: Search for coins
    Given I am on home page
    When I search for "<coin>"
    Then page should display "<coin>" page

    Examples:
      | coin     |
      | Bitcoin  |
      | Everest  |
      | Ethereum |