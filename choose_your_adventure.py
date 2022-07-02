print(''' *                       *
            *                 *
           )       (\___/)     (
        * /(       \ (. .)     )\ *
          # )      c\   >'    ( #
           '         )-_/      '
         \\|,    ____| |__    ,|//
           \ )  (  `  ~   )  ( /
            #\ / /| . ' .) \ /#
            | \ / )   , / \ / |
             \,/ ;;,,;,;   \,/
              _,#;,;;,;,
             /,i;;;,,;#,;
            ((  %;;,;,;;,;
             ))  ;#;,;%;;,,
           _//    ;,;; ,#;,
          /_)     #,;  //
                 //    \|_
                 \|_    |#\
                  |#\    -" 
''')
print("Welcome to The Haunted House.")
print("Your mission is escape before the ghosts catch you.")

choice_1 = input("You come across a narrow hallway. You slowly walk to the end to see two paths, one leading right "
                 "and one leading left. Where will you go? Type 'left' or 'right': ").lower()
if choice_1 == "left":
    choice_2 = input("You creep into a room and find a witch! What will you do? Type 'wait' or 'run': ").lower()
    if choice_2 == "wait":
        choice_3 = input("You wait and soon the witch leaves. You now see a red, yellow, and blue door. Where will you "
                         "go? Type 'red', 'yellow' or 'blue: '").lower()
        if choice_3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice_3 == "yellow":
            print("You manage to escape! You Win!")
        elif choice_3 == "blue":
            print("You enter a room of deadly beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by the angry witch. Game Over.")
else:
    print("You fell into a never-ending hole. Game Over.")
