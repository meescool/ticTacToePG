# Overall plan for the game

Small plan for getting the game started.

### UI variables
store these values in a separate module

    Screen size : 500 px * 500 px
    Main colors {
        indigo: rgb(54,46,101),
        pink: rgb(255,115,115),
        white: rgb(255,255,255),
        black: rgb(0,0,0)
    }

### show game title
    Wait 1 tick
    show title
    user clicks on screen to continue
### show game menu
    create a player dictionary to store a default skin 
    menu {
        continue (only show if no save data available)
        new game 
        choose skins
        help
        quit
        }

### new game 
    Pass in player as a dictionary
    load game board screen
    start a loop for the game to start
        break if board is:
            - full
            - there is a winner
    if full:
        - show ask to play again screen
    if winner:
        - show a "happy" message
        - show ask to play again screen
    if loser:
        - show a "sad" message
        - show ask to play again screen
    if no to ask to play again screen:
        - ask to save data
        if yes:
            - show 3 slots
            - user just clicks
        if no:
            - show main menu

### continue
    Same as new game, except the player is loaded with stored data.

### choose skins 
    Pass in the player as a dictionary
    show a variety of skins available
    gives the user the option to click on arrows to go through their options
    At the bottom there is a save and a cancel button.
    if save:
        - sets the player to update their skin
        - go back to main menu
    if cancel:
        - no changes are made
        - go back to main menu

### help
    This function shows a brief explanation of the game tic tac toe, and how to change their skins.

### quit
    This quits the game.
    

    
    

