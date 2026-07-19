Feature: Taint Propagation Analysis
  As a security engineer
  I want to trace dangerous imports through the dependency graph
  So that I can identify all files transitively affected by unsafe code

  Background:
    Given the taint analyzer is configured with standard settings

  Scenario: Direct dangerous import is detected as a taint source
    Given a Python project importing subprocess
    When I detect direct taint sources
    Then the result has at least one path
    And there is a 0-hop direct path
    And source count is at least 1
    And sink count is at least 1

  Scenario: Taint propagates through a single import chain
    Given a three-file import chain ending in subprocess
    When I propagate taint through the import chain
    Then the result has at least one path
    And the longest path has at least 2 hops
    And source count is at least 1

  Scenario: Taint does not propagate beyond max depth
    Given a max depth config of 1
    And a three-file chain with subprocess (max depth test)
    When I run shallow (max depth 1) taint analysis
    Then the result has at least one path
    And no path exceeds 1 hop

  Scenario: Cross-language taint propagation works for JS
    Given a JavaScript project with child_process import
    When I run JS taint analysis
    Then the result has at least one path
    And subprocess appears as the dangerous import
    And JS source count is at least 1
