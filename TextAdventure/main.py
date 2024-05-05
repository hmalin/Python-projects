print('''
  .       . 
 +  :      .
           :       _
       .   !   '  (_)
          ,|.' 
-  -- ---(-O-`--- --  -
         ,`|'`.
       ,   !    .
           :       :  " 
           .     --+--
 .:        .       !

**********ESCAPE********

''')

print("!!!!!!!!!!!!!!!!!!")
print('''You awaken in a strange place to sounds of distant screams....
You need need to escape this place..... You see two paths> One to the left and one to the right.
''')
first_room = input("Which one do you choose Enter: Left or Right. \n ").lower()

if first_room == "left":
    print("You make it to the next room ands see a strange gun on the table ")
    print('''
                _____
             .':::::::'.
       ___ /:::::::::::\____ _            _.''_
      /||   ||`.______.-`||   | |\_\\\\____/_ _.-'\\\\
     .|-| ||===||           ||===| ||_||||____|_| .-'|||||
     '|-| ||===||===========||===| ||_||||____|_|`-._|||||
       \||___||___________||___|_|/ ////       `-._////
            )  _____  (
           / .'| (  '. \
          ( (  './    ) )
           \ '._____.' /
            '._______.' 
    
    ''')

    item_pickup = input("Do you pick it up? Enter Yes or No \n ").lower()
    if item_pickup== "yes":
        print("You run into a horifying creature")
        print('''
        
                  (()))
                               /|x x|
                              /\( - )
                      ___.-._/\/
                     /=`_'-'-'/  !!
                     |-{-_-_-}     !
                     (-{-_-_-}    !
                      \{_-_-_}   !
                       }-_-_-}
                       {-_|-_}
                       {-_|_-}
                       {_-|-_}
                       {_-|-_}  ZOT
                   ____%%@ @%%_______
        
        
        ''')
        choice = input("shoot it? Yes or No \n").lower()
        if choice == "yes":
            print(" You felled the creature and move to a room with an escape shuttle")
            print("You find a control panel with four buttons which look to unlock the shuttle ")
            last_choice = input("which button do you press Red , Blue or Yellow ?: Enter your choice \n ").lower()
            if last_choice == "yellow":
                print("The Ship is unlocked! You board and make your escape! ")
                print('''
                              _,--=--._
                            ,'    _    `.
                           -    _(_)_o   -
                      ____'    /_  _/]    `____
                -=====::(+):::::::::::::::::(+)::=====-
                          (+).""""""""""""",(+)
                              .           ,
                              `      -=-  '
                
                 
                
                 *************ESCAPE SUCCESS**********
                 ''')

            elif last_choice == "red":
                print("The room explodes!")
                print(''' 
                
                           --_--
                        (  -_    _).
                      ( ~       )   )
                    (( )  (    )  ()  )
                     (.   )) (       )
                      ``..     ..``
                           | |
                         (=| |=)
                           | |     
                       (../( )\.))
                *******GAME OVER*********
                ''')
            elif last_choice == "blue":
                print("You opened the airlock and are sucked into space")
                print('''
                                .              +   .                .   . .     .  .
                                         .                    .       .     *
                        .       *                        . . . .  .   .  + .
                                                   .   .  +  . . .
                       .                              .  .   .    .    . .
                                                     .     .     . +.    +  .
                                                      .       .   . .
                            . .                  .    * . . .  .  +   .
                                +      .           .   .      +
                            .       . +  .+. .
                 .                      .     . + .  . .     .      .
                 .      .    .     . .   . . .        ! /
                 *             .    . .  +    .  .       - O -
                 .     .    .  +   . .  *  .       . / |
                 . + .  .  .  .. +  .
                  .      .  .  .  *   .  *  . +..  .            *
                  .      .   . .   .   .   . .  +   .    .            +
                **************GAME OVER********************************
                ''')
            else:
                print("You hesitate to make a valid choice and are greeted by your Alien overloads")
                print('''
                                 \.   \.      __,-"-.__      ./   ./
                             \.   \`.  \`.-'"" _,="=._ ""`-.'/  .'/   ./
                              \`.  \_`-''      _,="=._      ``-'_/  .'/
                               \ `-',-._   _.  _,="=._  ,_   _.-,`-' /
                            \. /`,-',-._"""  \ _,="=._ /  """_.-,`-,'\ ./
                            \`-'  /    `-._  "       "  _.-'    \  `-'/
                            /)   (         \    ,-.    /         )   (
                         ,-'"     `-.       \  /   \  /       .-'     "`-,
                       ,'_._         `-.____/ /  _  \ \____.-'         _._`,
                      /,'   `.                \_/ \_/                .'   `,/
                     /'       )                  _                  (       `
                             /   _,-'"`-.  ,++|T|||T|++.  .-'"`-,_   /
                            / ,-'        \/|`|`|`|'|'|'|\/        `-, /
                           /,'             | | | | | | |             `,
                          /'               ` | | | | | '               `
                                              ` | | | '
                                                ` | '

                         ******************No ESCAPE*************************
                         *****************GAME OVER**************************
                                                                                ''')
        else:
            print("You hesitated and are devoured by the creature.......Game over")
    else:
        print("you attempt to escape unarmed and are slaughtered by the horrors that lay ahead... Game Over.")

else:
    print("You fall into a laser trap and are burnt to a cinder")
    print('''
         (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     ***************GAME OVER******************
    ''')