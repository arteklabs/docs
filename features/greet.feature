Feature: Greet

  Scenario: Greet the user
    Given the CLI is installed
    When I run the "greet" command with "--name John"
    Then it should print "Hello, John!"
