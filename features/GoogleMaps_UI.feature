Feature: Google Map

  @asad @google-maps-car
  Scenario: Validate car distance on google maps from PA to CA is more than 40 hours
    Given I go to Google Maps
    When I input source and destination in maps
    Then I verify car distance in the maps from PA to CA is greater than 40 hours

  @asad @google-maps-walk
  Scenario: Validate walking distance on google maps from PA to CA is more than 900 hours
    Given I go to Google Maps
    When I input source and destination in maps
    Then I verify walking distance in the maps from PA to CA is more than 900 hours

  @asad @google-maps-bicycle
  Scenario: Validate bicycle distance on google maps from PA to CA is more than 250 horus and includes Ferry in the directions
    Given I go to Google Maps
    When I input source and destination in maps
    Then I verify bicycle distance on google maps from PA to CA is more than 250 horus and includes Ferry in the directions

  @asad @google-maps-edge-case
  Scenario: Validate flight booking from google maps doesn't allow booking for more than 11 months in the future
    Given I go to Google Maps
    When I input source and destination in maps
    When I check flights information by clicking google flights
    Then I verify flight booking from google maps doesn't allow booking for more than 11 months in the future