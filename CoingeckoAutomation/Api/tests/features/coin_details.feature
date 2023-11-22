Feature: Coin details

  Scenario Outline: Get basic coin information
    Given I want to get information about "<coin>"
    When I send get request
    Then I should receive correct response

    Examples:
      | coin           |
      | Bitcoin (bitcoin)  |
      | Everest (everid)   |
      | Ethereum (ethereum) |