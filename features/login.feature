Feature: Test login functionality

   Scenario Outline: Check login with valid credentials
    Given user is on login page
    When user enters <user name> and clicks on next and <password>
    When user clicks on login
    When user types <content>
    When user clicks on post
    Then user should get a toast <message>
    Then user clicks on logout

    Examples:
      | user name                    | password     | content  |message|
      | sudeshnashetty2211@gmail.com | 987654Suddu@ | wdef  @gari_setti61193 |Your post was sent.|

  Scenario Outline: Check login with valid credentials
    Given user is on login page
    When user enters <user name> and clicks on next and <password>
    When user clicks on login
    When user clicks on notifications and opens the account
    When user takes a screenshot
    When click back
    When clicks on reply
    When posts the screenshot
    Then user should get a toast <message>
    Then user clicks on logout

  Examples: 
    | user name                    | password     | message             |
    | sudeshna1995shetty@gmail.com | 987654Suddu@ | Your post was sent. |
