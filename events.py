import random

level_1_events = [
    {'event_type': 'riddle', 'question': 'What do you need to break before using? What am I?',
     'mc_answers': ['an egg', 'a clock', 'a hand', 'a hammer'], 'answer': '1', 'hint': 'You eat these for breakfast'},
    {'event_type': 'riddle', 'question': 'I’m tall when I’m young, and I’m short when I’m old. What am I?',
     'mc_answers': ['a tree', 'a waterfall', 'a candle', 'a watch'], 'answer': '3',
     'hint': 'You light these when the powers out'},
    {'event_type': 'riddle', 'question': 'How many months of the year has 28 days?',
     'mc_answers': ['1', '9', '11', '12'], 'answer': '4', 'hint': 'All months have more than 28 days'},
    {'event_type': 'choice', 'question': 'You see a dolphin in front of your submarine. Do you want to stop and say hi?'
        , 'yes_choice': 'Your crew loved the dolphin! Morale and exp has increased by 1',
     'no_choice': "Your crew is upset with you that you didn't stop. Morale has decreased by 1"},
    {'event_type': 'choice', 'question': 'An oyster shell is open and you see a pearl. Do you want to take the pearl?',
     'yes_choice': 'The pearl is a nice trophy! Morale and exp increased by 1',
     'no_choice': 'The crew respects you for not falling to greed. Morale and exp has increased by 1'},
    {'event_type': 'choice', 'question': 'A baby turtle is stuck in some plastic. Help it out?',
     'yes_choice': 'The baby turtle gives the ship a high five as thanks! Morale and exp has increased by 1',
     'no_choice': 'What kind of human are you?! The crew is outraged. Morale has decreased by 1'},

]

level_2_events = [
    {'event_type': 'riddle', 'question': 'What gets wet while drying?',
     'mc_answers': ['towel', 'hair', 'skin', 'clothes'], 'answer': '1', 'hint': 'You use this after you shower'},
    {'event_type': 'riddle', 'question': 'I have branches, but no fruit, trunk or leaves. What am I?',
     'mc_answers': ['an apple tree', 'a thought', 'a bank', 'a car'], 'answer': '3',
     'hint': 'You deposit money at this place'},
    {'event_type': 'riddle', 'question': 'The more of this there is, the less you see. What is it?',
     'mc_answers': ['darkness', 'sun', 'happiness', 'sadness'], 'answer': '1', 'hint': 'Hello _________ my old friend'},
    {'event_type': 'choice', 'question': 'A jellyfish is stuck on the hull of the sub. Should we try to shake it off?',
     'yes_choice': 'All the shaking has made the crew sick and the jellyfish is still there. Morale has decreased by 1',
     'no_choice': "The jellyfish calmly swam away. Morale and exp has increased by 1"},
    {'event_type': 'choice', 'question': 'You see some trash floating in the ocean. Pick it up?',
     'yes_choice': "Great job! People who litter are the worst. Morale aned exp has increased by 1",
     'no_choice': "You're part of the problem! The crew does not approve. Morale has decreased by 2"},
    {'event_type': 'choice', 'question': 'Someone in the crew offered you carbonated water. Drink the water?',
     'yes_choice': "Haven't you learned Chris? Morale has decreased by 1 as have Patty's happiness.",
     'no_choice': "Wow, I'm impressed! Even though I know it's a lie...Morale and exp has increased by 1"},

]

level_3_events = [
    {'event_type': 'riddle', 'question': 'David’s parents have 3 sons: Snap, Crackle. What’s the name of their 3rd son?'
        , 'mc_answers': ['Pop', 'Rice Krispie', 'Snip', 'David'], 'answer': '4', 'hint': 'Starts with a D'},
    {'event_type': 'riddle', 'question': 'Where does today come before yesterday?',
     'mc_answers': ['your head', 'the dictionary', 'google', 'apple'], 'answer': '2',
     'hint': 'Can look for meanings of words in this'},
    {'event_type': 'riddle', 'question': 'It belongs to you, but other people use it more than you do. What is it?',
     'mc_answers': ['your name', 'your computer', 'your car', ], 'answer': '1', 'hint':"For you, it's Chris"},
    {'event_type': 'riddle', 'question': 'What has hands, but can’t clap?',
     'mc_answers': ['your attitude', 'a clock', 'a map', 'you'], 'answer': '2', 'hint': 'tick, tock, but not tik tok'},
    {'event_type': 'choice',
     'question': "One of your crew offers you some radioactive kelp to try. 'It's the bomb man! Take the kelp?",
     'yes_choice': "the kelp made you sick and you threw up. The crew thinks you're uncool. Morale has decreased by 1",
     'no_choice': "The crew thinks you're uncool for not taking it. Morale has decreased by 1"},
    {'event_type': 'choice', 'question': 'OOH a shiny light...should you follow it?',
     'yes_choice': "You got lured in by an anglerfish. Haven't you seen the movies? Shiny light = bad. "
                   "The crew is not impressed. Morale has decreased by 1",
     'no_choice': "Whew you avoided an anglerfish! The crew is thankful. Morale and exp has increased by 1"},
    {'event_type': 'choice', 'question': 'Tim and Patty have made an awesome game! Do you agree?',
     'yes_choice': "Thanks :)! Morale and exp has increased by 1", 'no_choice': ":( Morale has decreased by 1"},
    {'event_type': 'choice', 'question': 'A stingray wants to play tag. Play tag with it?',
     'yes_choice': "The stringray tagged you with its tail and stung your crew. Morale has decreased by 1",
     'no_choice': "Good choice. Chances are the sting ray would have stung you. Morale and exp has increased by 1."},
]

random.shuffle(level_1_events)
random.shuffle(level_2_events)
random.shuffle(level_3_events)
