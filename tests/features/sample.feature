Feature: Simple sample page

  Scenario: open a sample page
    Given we are on the sample page
    When we read the page text
    Then we see the text "Hello world"
