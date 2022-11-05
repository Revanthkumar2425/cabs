Feature: goibibo_cabs

  Background: : user is able to book a cab in goibibo through goibibocabs module
    Given User is able to launch chrome browser
    When user is able to click on outstation one_way

  Scenario Outline:
    Then user is able to enter "<from_location>" in from textfield
    Then user is able to click on from autosuggestion
    Then user is able to enter "<to_location>" in to textfield
    Then user is able to click on to autosuggestion
    When user is able to click on pickup date
    Then user is able to select the date
    When user is able to click on pickup time
    Then user is able to select time
    And user is able to click on search cabs
    Then user is able to click on select button
    Then user is able to enter "<pickup_location>" in pickup location textfield
    When user is able to click on location autosuggestion
    Then user is able to enter "<full_name>" in full name textfield
    Then user is able to enter "<mobile_number>" in mobile number textfield
    Then user is able to enter "<email>" in email textfield
    Then user is able to click paynow button
    And user is able to click on payment button


    Examples:
      |from_location|to_location|pickup_location |full_name|mobile_number|email                          |
#      |Bangalore    |Mysore     |Brookefield mall|Revanth  |9742428125   |revanthkumarkanumilli@gmail.com|
#      |Mysore       |Bangalore  |Mysore palace   |Revanth  |9742428125   |revanthkumarkanumilli@gmail.com|
#      |Bangalore    |Mysore     |Brookefield mall|Revanth  |7396424409   |revanthkumarkanumilli@gmail.com|
      |Bangalore    |Mysore     |Brookefield mall|Revanth  |97428125     |revanthkumarkanumilli@gmail.com|
      |Bangalore    |Mysore     |Brookefield mall|Revanth  |9742428125   |revanthkumar                   |
