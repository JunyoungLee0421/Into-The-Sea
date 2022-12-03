
intro_1 = "To find the treasure, you have to find to octopus hiding in the depths of the water. But in order to get\n"\
          "strong enough to fight him, you'd need to level up your sub! To level your sub, you have to go to [!]\n" \
          "symbols which indicate events. There are 3 types of events: battle, riddles, and choices. For battles,\n" \
          "if you defeat the monster you gain exp and morale. But if you are defeated by the monster, game over.\n" \
          "For riddle events, if you get the riddle right, crew morale and exp increases. If you get it wrong, \n" \
          "your crew loses faith in you and morale decreases. In the cases of choice events, if you make the \n" \
          "right choice, morale and exp will increase. If you make the wrong choice, morale will decrease.\n"

intro_2 = "There are 2 main ways to lose this game: losing all your crew morale or losing monster battles. \n" \
          "Crew morale increases when you do well at events, and decreases if you run away or lose at events. \n" \
          "So you definitely want to make sure you do well at events or your crew loses faith in you.\n" \
          "We've talked about battle events, but again if you lose all your health in battle it’s game over. \n"\
          "Don't worry though, everytime you finish a battle your hp comes back for the next battle \n" \

intro_3 = "If you look at your submarine map right now, you can only see shallow waters. That’s because we’ve \n"\
          "lost our submarine headlights somewhere in these waters. Gain the headlights by leveling up to level 2! \n" \

level_up_ASCII = """
    __                   __   __  ______     __
   / /   ___ _   _____  / /  / / / / __ \   / /
  / /   / _ \ | / / _ \/ /  / / / / /_/ /  / /
 / /___/  __/ |/ /  __/ /  / /_/ / ____/  /_/
/_____/\___/|___/\___/_/   \____/_/      (_)
"""


level_2_up = "Congratulations on reaching level 2! You’ve successfully gotten your subs headlights back so you’re \n" \
             "able to see slightly deeper into the ocean now. Your stats have leveled up and you’ll be able to \n" \
             "fight tougher monsters. Be aware, these monsters deeper down are going to be tougher than before \n. " \
             "In order to get to the octopus, you need to get to level 3 to get the sonar to find him"

level_3_up = "You’ve reached level 3! Unfortunately, no matter your headlight strength, you won’t be able to see \n" \
             "to the bottom. No worries though, with this sonar, you’ll be able to locate where the octopus is \n" \
             "relative to you. You now have an extra sonar option to choose when you move. Try it out next when \n" \
             "you select your move! Use this sonar to find the octopus to complete the final challenge. Be aware, \n" \
             "there are still many monsters lurking in the deep that are stronger than they've ever been...\n "


octopus_game = "WOOOOO look who's here!! A challenger? I can't wait to rip into you with my squiggly limbs.\n"\
               "What? You're here for this treasure? Not even a hello Mr. Octopus nice to meet you? How rude!\n" \
               "You're lucky I'm in a happy mood today. I'll play a guessing game with you.\n"\
               "I'm thinking of a 3 digit number. All you have to do is guess it. I'll even give you hints cuz \n"\
               "you look like you need them.\n"\
               "\n"\
               "The 3 digits range from 0-9, except for the 1st digit, which cannot be a 0.\n"\
               "Everytime you guess, I'll tell you how close you are to the number by using the letters A and B\n"\
               "'A' means one of the digits you guessed is in the right position and it's the correct number\n"\
               "'B' means one of the digits you guessed is a number that's also in my answer, " \
               "but it's in the wrong position\n"\
               "\n"\
               "For example, if my number is 132, and you guessed 123, my hint to you would be 1A 2B. \n"\
               "1A because you guessed the 1 in the correct first position and correct number. \n"\
               "2B because you guessed the 2 and 3 numbers, but they are in the wrong positions. \n" \
               "If my number was 132, and you guessed 425, my hint to you would be 1B, as the 2 is the right number,\n"\
               "but you guessed in the wrong position.\n"\
               "If my number was 132 and you had guessed 456, my hint to you would be 0A 0B as no numbers are right\n" \
                "\n"\
               "Take your time reading this. Remember, if you lose, you stay down here with me forever! MUAHAHA \n" \
               "When you're ready, press any key to start."

octopus_trash_talk = ["You call that a guess? My friend Urch the urchin does better and he doesn't even have a brain!",
                      "Ha, you'll definitely be staying down here with me, no carbonated water for you down here!",
                      "Most PC users would have gotten this already...you must use a MAC",
                      "Better start thinking of how you're going to spend your free time down here...there's no WIFI",
                      "You must want to stay down here with how bad your guesses are",
                      "Patrick the Star would have gotten this already, just saying.",
                      "Just give up already, you're never going to get it!"]

octopus_ASCII ="""MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNK0OOkOOO0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMWWWWKkxxollcccllodxk0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNOdoclc,... ....;olldkKWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOoll:'..          ..,cloxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMMMMWWWKdlc;'...           ....,:llkNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMMMMWNkol:..'lOx. .,;;;'.. :Ox:..,cld0WWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWW0doc;.  .;;clxKNNNXXKOdl:;,.  ':lokNMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXkoxo'       .kKOO0K00O0Kc       .,coo0WWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNOdolc.        .xKOkO0OOO0Kc        .'codxKWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWMMMWWXOddo:.       ...;lxKX0kKNNOol,...      .,loox0NWWWWWMMWMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMWWWWWWXOkxddl,.        .ck0;.cKXXXOo,.d0d;.        .;ldddO0XWWMWWWMWWMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0OOkkkdldd:'.            .;. .;cl:,'. .;.            ',lxooxkkkOO0NMWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMWWOooolloc:'...            ...''',,,,,,,''''...            .'.,:lolooodKWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo;,.....            .,;;:clooooooooooooooollc::;'.            ....';;kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWO:.     .'.     .';:loolloddddxxkxkO0K000OOxdooolc:,.     .'.       :KWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKl;c;. .:'   .':looodxdodxdddxxxxxkOOkkkOOOOOOxdoloc;.   .:, .'::,lKWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXkdOOc.    .;looddxxdodxxxxxxxxxxxxkxxkxxxxkkkxxxxolc,.    'dOxdONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkxx;   .:cdxoloddddxxxxxxxxxxxxxxxxxxxxxxxxxxxdddlc;.  .lxxONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXOd,..;coxdddoldxxxkxxxxxxxxxxxxxxxxxxxxxxxxdddoolc' .:xKNMWWMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMWMWWN0xccxdoxdloxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdoddoclkKWMMWWWWMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMWWXdoxddxxdxxxkxxxxxxxxxxxxxxxxxxxxxxxxxxxdoodolkWWWMMWMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKooxdddxxxxkxxxxxxxxxxxxxxxxxxxxxxxxxxxdoddxxlxWMMMWWWWWKkkkkxxdxkXWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXookxddOOkxkxxxxxxxxxxxxxxxxxxxxxxxxxxxxdodkklkWWWMMWW0xddxxxxddollxXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWMMWNdlkxxxkkkxkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxddkdcOMMMMMNxlkkdll::oolc::OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWxld0WMMklxxxxxxxkxxxxxxxkxxkxxxxkkxxxxxxxxxkxxxodkooXMMMMWxcxkdl;;dKWWNklxNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWNWWXlcdckWMNdlkxxxxddxxdddxxkkxxxkxxxxxkxdodxkkddxxdxdlOWMMMMXllkddd:cOWMMMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWW0doodlldOooNMMKookxxlcxd;.'lllxkxxkkxxxxkdlo;.'cxocokkxlxNWMMMMXllkdllxdxNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0kxdc,:coxxxoo0WMMWKdoxxclx;  .,.'oxxxkxxkkxk:.,. ..od:okdlkNMMMMMMWdcxdc:,lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKxdoxdldxoodxOXMMMMMWXkoddclc,.  .:dkkkkkkkkkko,. .';lcldod0WMMMMMMWMkcdxll;:xKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0c;cldkkdxKNWMWMMMMMMMWKxoolccllodkxOkxkOxxkO00OkxllccoookXMMMMMMMMMM0cokoc:dkONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKxl:looOxkWWWMWWMMMMMMMMMWOlddldOkkxkOOkkkkOO00O0K0kolxooXWMMMMMMMMMMMkcdkdlllo0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWkkkdOxd0dlKMWWMMMMMMMMMMMNxoddxxxxxxkkkkkkkkkkkkkOkkkxxcdWMWWMMMMMMMWKooOkdodc,xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKdccc:lkOdoxKNWWMMMMMWNKkdoooddodxxkxxxxxxxkxxkxxxxxxoolcOWWWWWMWWWW0ooOOxdl;;clOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWxcocdkdxOxoodxxxxxxxddoloxdodddxxxxxxxxxxxxxxkxxkxxxdoooldk0KNNX0xoldkkxxooc:dx0WMMMWMWWWWMWWMWWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMOxKxlolldxxxkkxxddxxdddoodddxxxxxxkxxdodooxxxxxxkxxxoldddollodoolodkkxxdl:c::xNWMMMMMMWWMWWWMMMWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0kd;;lclkOoodddxxxxxxdxddddddoxxxxddoldlcddddkkxxxxdoodddxxxxxddkkkxxolllool0MWWMMWWMXOxONWWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNxoOOxlcccllldkkc:oooddollccdkxxdddddclxdocldxxxxxkxxxxxkkxxxxxddccl:::ok0WMWMWWMMWx:l:xWWMMWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWMWWMMMMMMMMN0OOklck0Ol,;:c;;cccodc;:;lkxxdodddc:dkxkdc::coddddddddxkxllllcccoxxl:OWWMMMWWWWXklox;oNMMWWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWWKxxx0WMWWWWMMWKOOOxc;:cc:::clllc;:xkdxdddxd;ckxxxkxxl:;;;:ccloollc;:cddl;;oxocoxxxkkkxxdoldxo;dWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWWWWOcox:dNWWMMMMWWWNKkxolodxdddkkxdcldkxdoooddc;lxkkkxxO0d::cc:;;cdxd:,;lxxocoolodxolcloolldkxdo;cKMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWWMNolkxolx0KKK0Okxdollodddddxxxxdl:oxxxxxooxd:okoxkxxxkk0x:okxdoc;,:llloddddxxddddxddddkxxxddoc;lKWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWWMWxcxxxdoloooooodxddxddxxxxxdoc;:dxxxxxdddd;,O0odddxxxk0x:lxxxdddc;clccooddddxxxxddddddoooc::lONMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWWMXocoxxxxkkkkkxkxxxxxxddlcclc;cxkkxxxdodo;.oNOlooodxxk0dcdxxxdod:oXKkdocc:::ccccccc::::cldkKWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWWMMNkollloddxdddooolccclodk0xldxxxxkxxxdl;;,xWkcodoodxO0o;:cdxxdd:oNWWWNXK0kxxddddddxkO0KNMMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWMWWXOxdddddxxddxxO0KNWWNxloodxxxkOxo;:kOlxWd:xkxxdkOk:':lddxxdlcKWWMMMMMMMMMMMMMMMMMMWMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWXdcddodxk0kl;co;lxcxXolxxkxdxko,:l;:lxxxdcxWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdcooddxOOl;;;;;;:;'dklolodddxdckk::clddxkocOWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWkcdddxOOooxc:ldo:x0occldooodxdcdNXxoc;:oxxkdcOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXolxxkOxlkNWx::cl::lc.;doddoxkocOWWNOo::ccldkxldXMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0lokxkdlOWMWOc::,;c:'.:xddxxxxxcdNWWWNkoc,;:oxxolxKWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKlokxxcdWMWWKc:od::x:.;xkxxkxxxdlo0NWMWKko:c::codoldkXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdcxkdckMMMMXl:c::;,.,oldxkkkddoooldKWWMMWKko;,:clooloxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKllxxloXMMMKl;ll:lkcoN0dolodxdddodlckNWWWWWWKkxo,:ololldKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKoloxol0WM0::odc:lcOMMWXOkxdoodxddocOWMMMMMMMWX0kd:;:l:lKWMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0doolOWWx;c:,;;,lNMWWWWMMNKxllxxkldNMMMMMMMMMWWWX0xolxXWMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWNKXWWKc;clo::lOWMMWWWMWXKXKllxOooNMMMMMMMMWWWWWWMWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMMMWWMWd;cc::;cONMMMMMX0xocoNd:kOlxWMMMMMMMMMWMWMMMMMWWMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk::lc;ldKMWMMMMWx,:dlldldkloXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0:,;:cckNWMWWMMMM0dololooolxNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXxoxO0XWMMMMMMWWMWWXOxxxxONWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"""

you_win_ASCII = """

__  ______  __  __   _       _______   __   __
\ \/ / __ \/ / / /  | |     / /  _/ | / /  / /
 \  / / / / / / /   | | /| / // //  |/ /  / / 
 / / /_/ / /_/ /    | |/ |/ // // /|  /  /_/  
/_/\____/\____/     |__/|__/___/_/ |_/  (_)   
                                              
"""

you_lose_ASCII = """
                         __           __                    
   __  ______  __  __   / /___  _____/ /_                   
  / / / / __ \/ / / /  / / __ \/ ___/ __/                   
 / /_/ / /_/ / /_/ /  / / /_/ (__  ) /_   _    _    _       
 \__, /\____/\__,_/  /_/\____/____/\__/  (_)  (_)  (_)      
/____/                                                      

"""

