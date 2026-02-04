# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 01:06:43 2025

@author: Usuario
"""
import random as rm
import time as tm 

valid_location_numbers = [1,2,3,4,5,6,7,8,9]
location_list = [" "," "," "," "," "," "," "," "," "] 
player_1_choices = []
player_2_choices = []
winner_symbol = " "
player_symbol_flag = False 
computer_number_flag = False  
stop_game = False
 
#This part of the code draws the game mat
a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15 = " "," "," ","*"," "," "," "," "," "," "," ","*","*"," "," "
a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30 = " "," "," "," ","*","*"," "," "," "," ","*"," ","*"," "," "
a31, a32, a33, a34, a35, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45 = " "," "," ","*"," "," "," "," ","*"," "," "," "," "," "," "
a46,a47,a48,a49,a50,a51,a52,a53,a54,a55,a56,a57,a58,a59,a60= " ","*"," "," "," "," ","*"," "," "," "," "," "," "," "," "
a61,a62,a63,a64,a65,a66,a67,a68,a69,a70,a71,a72,a73,a74,a75 = " ","*"," "," "," "," "," ","*"," ","*"," "," "," "," "," "
a76, a77, a78, a79, a80, a81, a82, a83, a84, a85, a86, a87, a88, a89,a90 = "*"," "," "," "," "," "," ","*"," "," "," "," "," "," "," "
a91,a92,a93,a94,a95,a96,a97,a98,a99,a100,a101,a102,a103,a104,a105 = " "," "," "," ","*"," "," ","*","*","*","*","*"," "," "," "
a106, a107, a108, a109, a110, a111, a112, a113, a114, a115, a116, a117, a118, a119,a120 = "*","*","*","*","*"," "," "," "," "," ","*"," ","*"," "," "
a121,a122,a123,a124,a125,a126,a127,a128,a129,a130,a131,a132,a133,a134,a135 = " ","*"," "," "," "," ","*"," "," ","*","*","*","*","*","*"
a136, a137, a138, a139, a140, a141, a142, a143, a144, a145, a146, a147, a148, a149,a150= " "," "," "," ","*","*","*"," "," "," ","*"," "," "," "," "
a151,a152,a153,a154,a155,a156,a157,a158,a159,a160,a161,a162,a163,a164,a165 = "*"," "," ","*"," "," "," "," "," "," "," ","*"," "," "," "
a166,a167,a168,a169,a170,a171,a172,a173,a174,a175,a176,a177,a178,a179,a180 = " "," "," "," ","*","*","*","*","*","*"," "," ","*"," "," "
a181,a182,a183,a184,a185,a186,a187,a188,a189,a190,a191,a192,a193,a194,a195 = "*"," "," "," "," ","*"," "," ","*"," "," "," "," "," "," "
a196,a197,a198,a199,a200,a201,a202,a203,a204,a205,a206,a207,a208,a209,a210 = " "," "," ","*"," "," "," "," "," "," "," ","*"," "," ","*"
a211,a212,a213,a214,a215,a216,a217,a218,a219,a220,a221,a222,a223,a224,a225 = " "," "," "," ","*"," "," "," "," "," "," "," ","*"," "," "
a226,a227,a228,a229,a230,a231,a232,a233,a234,a235,a236,a237,a238,a239,a240 = "*"," "," ","*"," "," "," "," "," "," "," ","*"," "," "," "
a241,a242,a243,a244,a245,a246,a247,a248,a249,a250,a251,a252,a253,a254,a255 = " ","*","*","*","*","*","*"," "," "," ","*","*","*","*"," "
a256,a257,a258,a259,a260,a261,a262,a263,a264,a265,a266,a267,a268,a269,a270 = " "," "," ","*","*","*","*"," "," "," "," "," "," "," "," "
a271,a272,a273,a274,a275,a276,a277,a278,a279,a280,a281,a282,a283,a284,a285 ="*"," "," ","*"," "," "," "," ","*"," "," ","*"," "," "," "
a286,a287,a288,a289,a290,a291,a292,a293,a294,a295,a296,a297,a298,a299,a300 = " ","*"," "," "," "," "," "," ","*"," "," "," "," ","*","*"
a301,a302,a303,a304,a305,a306,a307,a308,a309,a310,a311,a312,a313,a314,a315 = "*","*"," "," "," "," ","*","*","*","*"," "," "," "," "," "
a316,a317,a318,a319,a320,a321,a322,a323,a324,a325,a326,a327,a328,a329,a330 = " ","*"," "," "," "," ","*"," "," "," "," ","*"," "," "," "
a331,a332,a333,a334,a335,a336,a337,a338,a339,a340,a341,a342,a343,a344,a345 = " "," ","*"," "," "," "," "," "," ","*"," "," "," "," "," "
a346,a347,a348,a349,a350,a351,a352,a353,a354,a355,a356,a357,a358,a359,a360 = " ","*","*","*","*"," "," "," "," ","*"," "," "," "," "," "
a361,a362,a363,a364,a365,a366,a367,a368,a369,a370,a371,a372,a373,a374,a375 = " ","*"," "," "," "," "," "," ","*"," "," "," "," "," "," "

def tablero_1_1():
    print("*"*28)
    print(f"*{a1}{a2}{a3}{a4}{a5}{a6}{a7}{a8}*{a9}{a10}{a11}{a12}{a13}{a14}{a15}{a16}*{a17}{a18}{a19}{a20}{a21}{a22}{a23}{a24}*")
    print(f"*{a25}{a26}{a27}{a28}{a29}{a30}{a31}{a32}*{a33}{a34}{a35}{a36}{a37}{a38}{a39}{a40}*{a41}{a42}{a43}{a44}{a45}{a46}{a47}{a48}*")
    print(f"*{a49}{a50}{a51}{a52}{a53}{a54}{a55}{a56}*{a57}{a58}{a59}{a60}{a61}{a62}{a63}{a64}*{a65}{a66}{a67}{a68}{a69}{a70}{a71}{a72}*")
    print(f"*{a73}{a74}{a75}{a76}{a77}{a78}{a79}{a80}*{a81}{a82}{a83}{a84}{a85}{a86}{a87}{a88}*{a89}{a90}{a91}{a92}{a93}{a94}{a95}{a96}* ")
    print(f"*{a97}{a98}{a99}{a100}{a101}{a102}{a103}{a104}*{a105}{a106}{a107}{a108}{a109}{a110}{a111}{a112}*{a113}{a114}{a115}{a116}{a117}{a118}{a119}{a120}*")
    print("*"*28)
    print(f"*{a121}{a122}{a123}{a124}{a125}{a126}{a127}{a128}*{a129}{a130}{a131}{a132}{a133}{a134}{a135}{a136}*{a137}{a138}{a139}{a140}{a141}{a142}{a143}{a144}*")
    print(f"*{a145}{a146}{a147}{a148}{a149}{a150}{a151}{a152}*{a153}{a154}{a155}{a156}{a157}{a158}{a159}{a160}*{a161}{a162}{a163}{a164}{a165}{a166}{a167}{a168}*")
    print(f"*{a169}{a170}{a171}{a172}{a173}{a174}{a175}{a176}*{a177}{a178}{a179}{a180}{a181}{a182}{a183}{a184}*{a185}{a186}{a187}{a188}{a189}{a190}{a191}{a192}*")
    print(f"*{a193}{a194}{a195}{a196}{a197}{a198}{a199}{a200}*{a201}{a202}{a203}{a204}{a205}{a206}{a207}{a208}*{a209}{a210}{a211}{a212}{a213}{a214}{a215}{a216}*")
    print(f"*{a217}{a218}{a219}{a220}{a221}{a222}{a223}{a224}*{a225}{a226}{a227}{a228}{a229}{a230}{a231}{a232}*{a233}{a234}{a235}{a236}{a237}{a238}{a239}{a240}*")
    print("*"*28)
    print(f"*{a241}{a242}{a243}{a244}{a245}{a246}{a247}{a248}*{a249}{a250}{a251}{a252}{a253}{a254}{a255}{a256}*{a257}{a258}{a259}{a260}{a261}{a262}{a263}{a264}*")
    print(f"*{a265}{a266}{a267}{a268}{a269}{a270}{a271}{a272}*{a273}{a274}{a275}{a276}{a277}{a278}{a279}{a280}*{a281}{a282}{a283}{a284}{a285}{a286}{a287}{a288}*")
    print(f"*{a289}{a290}{a291}{a292}{a293}{a294}{a295}{a296}*{a297}{a298}{a299}{a300}{a301}{a302}{a303}{a304}*{a305}{a306}{a307}{a308}{a309}{a310}{a311}{a312}*")
    print(f"*{a313}{a314}{a315}{a316}{a317}{a318}{a319}{a320}*{a321}{a322}{a323}{a324}{a325}{a326}{a327}{a328}*{a329}{a330}{a331}{a332}{a333}{a334}{a335}{a336}*")
    print(f"*{a337}{a338}{a339}{a340}{a341}{a342}{a343}{a344}*{a345}{a346}{a347}{a348}{a349}{a350}{a351}{a352}*{a353}{a354}{a355}{a356}{a357}{a358}{a359}{a360}*")
    print("*"*28) 


#this funtion erases the numbers in teh selcted square of the game grid and replaces the number for the selcted symbol "X" or "O"
def mark(num,symbol):
    if num == 1:
        #Erasing the number 1
        global a4,a2,a3,a5,a6,a7,a27,a26,a28, a30,a31,a50, a52,a55,a74, a75, a76,a78,a79,a98,a99, a100, a101 ,a102,a103 
        a4,a26,a28,a52,a76,a98, a99 ,a100, a101, a102  = " "," ", " "," ", " ", " "," "," "," "," " 
        #Writing  X in the position 1
        if symbol == "X":
            a2,a7,a27,a30,a52,a75,a78,a98,a103 = "*","*","*","*","*","*","*","*","*" 
        #Writing  O(circle) in position 1
        if symbol == "O":
            a2,a3,a4,a5,a6,a7,a26,a31,a50,a55,a74,a79,a98,a99,a100,a101,a102,a103  = "*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*" 
    elif num == 2:
        global a10,a11,a12,a13,a14,a15,a34,a35,a38,a39,a58,a60,a62,a63,a82,a87,a83,a86,a106, a107,a108,a109,a110,a111
        #Erasing the number 2
        a12,a13,a34,a39,a62,a83,a106,a107,a108,a109,a110  = " "," "," "," "," "," "," "," "," "," "," " 
        #Writing  X in the position 2
        if symbol == "X":
            a10,a15,a35,a38,a60,a83,a86,a106,a111 = "*", "*","*","*","*","*","*","*","*"
         #Writing  O(circle) in position 2
        if symbol == "O":
            a10,a11,a12,a13,a14,a15,a34,a39,a58,a63,a82,a87,a106,a107,a108,a109,a110,a111 = "*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*" 
    elif num == 3:
        #Erasing the number 3
        global a20,a18,a19,a21,a22,a23,a42,a43,a46,a47,a66,a68,a70,a71,a90,a91,a94,a95,a114,a115,a117,a119,a116,a118 
        a20,a21,a47,a68,a70,a95,a116,a118 = " "," "," "," "," "," "," "," "
        #Writing  X in the position 3
        if symbol == "X":
            a18,a23,a43,a46,a68,a91,a94,a114,a119 = "*", "*","*","*","*","*","*","*","*"
        #Writing  O(circle) in position 3
        if symbol == "O":
            a18,a19,a20,a21,a22,a23,a42,a47,a66,a71,a90,a95,a114,a115,a116,a117,a118,a119 = "*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*" 
    elif num == 4:
        global a122,a123,a124,a125,a126,a127,a146,a147,a150,a151,a170,a171,a172,a173,a174,a175,a194,a195,a198,a199,a218,a219,a220,a221,a222,a223
        #Erasing the number 4
        a122,a127,a146,a151,a170,a171,a172,a173,a174,a175,a199,a223 = " "," "," "," "," "," "," "," "," "," "," "," "
        #Writing  X in the position 4
        if symbol == "X":
           a122,a127,a147,a150,a172,a195,a198,a218,a223  = "*","*","*","*","*","*","*","*","*" 
         #Writing  O(circle) in position 4
        if symbol == "O":
           a122,a123,a124,a125,a126,a127,a146,a151,a170,a175,a194,a199,a218,a219,a220,a221,a222,a223 = "*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*" 
    elif num == 5:
        global a130,a131,a132,a133,a134,a135,a154,a155,a158,a159,a178,a180,a181,a183,a202,a203,a206,a207,a226,a227,a228,a229,a230,a231 
        #Erasing the number 5
        a130,a131,a132,a133,a134,a135,a154,a178,a181,a207,a226,a229  = " "," "," "," "," "," "," "," "," "," "," "," "
        #Writing  X in the position 5
        if symbol == "X":
            a130,a135,a155,a158,a180,a203,a206,a226,a231 = "*","*","*","*","*","*","*","*","*" 
         #Writing  O(circle) in position 4
        if symbol == "O":
             a130,a131,a132,a133,a134,a135,a154,a159,a178,a183,a202,a207,a226,a227,a228,a229,a230,a231 = "*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*" 
    elif num == 6:
        global a138,a139,a140,a141,a142,a143,a162,a163,a166,a167,a186,a188,a189,a191,a210,a211,a214,a215,a234,a235,a236,a237,a238,a239
        #Erasing the number 6
        a140,a141,a142,a162,a186,a189,a210,a215,a237  = " "," "," "," "," "," "," "," "," "
        #Writing  X in the position 6
        if symbol == "X":
            a138,a143,a163,a166,a188,a211,a214,a234,a239  = "*","*","*","*","*","*","*","*","*" 
        #Writing  O(circle) in position 6
        if symbol == "O":
            a138,a139,a140,a141,a142,a143,a162,a167,a186,a191,a210,a215,a234,a235,a236,a237,a238,a239 =  "*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*" 
    elif num == 7:
       global  a242,a243,a244,a245,a246,a247,a266,a267,a270,a271,a290,a292,a294,a295,a314,a315,a317,a318,a319,a338,a339,a341,a342,a343,a340
       #Erasing the number 7
       a242,a243,a244,a245,a246,a247,a271,a294,a317,a340 = " "," "," "," "," "," "," "," "," "," "
       #Writing  X in the position 7
       if symbol == "X":
           a242,a247,a267,a270,a292,a315,a318,a338,a343 = "*","*","*","*","*","*","*","*","*"
       #Writing  O(circle) in position 7
       if symbol == "O":
        a242,a243,a244,a245,a246,a247,a266,a271,a290,a295,a314,a319,a338,a339,a340,a341,a342,a343 =  "*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"    
    elif num == 8:
         global a250,a251,a252,a253,a254,a255,a274,a275,a278,a279,a298,a299,a300,a301,a302,a303,a322,a323,a326,a327,a346,a347,a348,a349,a350,a351
         #Erasing the number 8 
         a251,a252,a253,a254,a274,a279,a299,a300,a301,a302,a322,a327,a347,a348,a349,a350 = " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "
         #Writing  X in the position 8
         if symbol == "X":
             a250,a255,a275,a278,a300,a323,a326,a346,a351 = "*","*","*","*","*","*","*","*","*"    
         #Writing  O(circle) in position 8
         if symbol == "O":
             a250,a251,a252,a253,a254,a255,a274,a279,a298,a303,a322,a327,a346,a347,a348,a349,a350,a351 =  "*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"
    elif num == 9:
         global a258,a259,a260,a261,a262,a263,a282,a283,a286,a287,a306,a307,a308,a309,a310,a311,a330,a331,a334,a333,a335,a354,a355,a356,a357,a358,a359 
         #Erasing the number 9
         a259,a260,a261,a262,a282,a287,a307,a308,a309,a310,a333,a355 = " "," "," "," "," "," "," "," "," "," "," "," "
         #Writing  X in the position 9
         if symbol == "X":
             a258,a263,a283,a286,a308,a331,a334,a354,a359 = "*","*","*","*","*","*","*","*","*" 
         #Writing  O(circle) in position 9
         if symbol == "O":
             a258,a259,a260,a261,a262,a263,a282,a287,a306,a311,a330,a335,a354,a355,a356,a357,a358,a359  = "*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*" 

#Ensures that the user(player or computer) only uses valid number(1 to 9) once for game  
def number_check(number,check_list_1,check_list_2):
    try: 
        int(number)/5 
    except ValueError:
        return False
    if int(number) < 1 or int(number) > 9 or int(number) in check_list_1 or int(number) in check_list_2:
        return False
    else:
        return True 
#Decides if the player or the computer has won the match    
def victory_check(test_list,symbol):
    if test_list[0] == test_list[1] == test_list[2] == symbol :
        return (True,symbol)
    elif test_list[3] == test_list[4] == test_list[5] == symbol :
        return (True,symbol)
    elif test_list[6] == test_list[7] == test_list[8] == symbol:
        return (True,symbol)
    elif test_list[0] == test_list[4] == test_list[8] == symbol:
        return (True,symbol)
    elif test_list[6] == test_list[4] == test_list[2] == symbol:
        return (True,symbol)
    elif test_list[0] == test_list[3] == test_list[6] == symbol:
        return (True,symbol)
    elif test_list[1] == test_list[4] == test_list[7] == symbol:
        return (True,symbol)
    elif test_list[2] == test_list[5] == test_list[8] == symbol:
        return (True,symbol)
    else:
        return (False,symbol)
#runs the main game
def main_game():
    global player_symbol_flag 
    global winner_symbol 
    global player_number_flag 
    global computer_number_flag
    global player_symbol_flag
    global draw_game_flag
    winning_condition = False
    draw_game_flag = False
    print("Welcomo to Tic-Tac-Toe")
   
    # showing the board
    tablero_1_1()
    
    # asigning the symbols X and O to the player_1(user) and player_2(computer)
    
    print("player_1 please slect the symbol that you are using")
    player_1_symbol = input("please use X or O as a symbol: ")
    player_1_symbol.upper()
    if player_1_symbol == "X" or player_1_symbol == "O":
        player_symbol_flag = True
    try: 
        while(player_symbol_flag == False ):
            print("That is not a valid symbol")
            player_1_symbol = input("please use X or O as a symbol: ")
            if player_1_symbol == "X" or player_1_symbol == "O":
                player_symbol_flag = True    
    except ValueError:
        print("That is not a valid symbol")
        player_1_symbol = input("please use X or O as a symbol: ")
       
    if player_1_symbol == "X":
         player_2_symbol = "O"
    else:
         player_2_symbol = "X"
         
    while(winning_condition == False):
        # player 1 deciding on which position to place his/her symbol
        
        player_1_number = (input("player_1 please select a position from 1 to 9 that is not occupied: "))
        
        while(number_check(player_1_number,player_1_choices,player_2_choices)== False ):
            
            print("That is not a valid number.")
            player_1_number = (input("player_1 please select a position from 1 to 9 that is not occupied: ")) 
        
        player_1_choices.append(int(player_1_number)) 
        location_list[int(player_1_number)-1] = player_1_symbol
        mark(int(player_1_number),player_1_symbol)
        if  location_list.count(" ") == 0:  
           draw_game_flag = True
        tablero_1_1()
        
        # Stop time to give the ilusion that the computer is "thinking"
        print("thinking....")
        tm.sleep(5) 
        
        # player 2 deciding on which position to place its symbol
        player_2_number = rm.randint(1,9)
        while(player_2_number in player_1_choices or player_2_number in player_2_choices and draw_game_flag == False):
            if location_list.count(" ") == 1:
                print("Darw Game")
                draw_game_flag == True
                winning_condition == True
                   
            player_2_number = rm.randint(1,9)
        
        player_1_winning_decision = victory_check(location_list,player_1_symbol)  
        player_2_winning_decision = victory_check(location_list,player_2_symbol)
    
      #sending winner message 
        if player_1_winning_decision[0] == True and player_1_winning_decision[1] == player_1_symbol:
            winning_condition = True
            print("player 1 wins")
            break
        elif player_2_winning_decision[0] == True and player_2_winning_decision[1] == player_2_symbol:
            print("Player_2 wins")
            winning_condition = True
        elif location_list.count(" ") == 0:
            print("draw game")
            winning_condition = True # itmay seem confusuing but winning codition is mnerely used a a flag 
        print(location_list.count(" "))


        # Recording player_2 choices         
        player_2_choices.append(player_2_number) 
        location_list[player_2_number-1] = player_2_symbol
        mark(player_2_number,player_2_symbol)
        tablero_1_1()
        #"X" winning conditions
       
        player_1_winning_decision = victory_check(location_list,player_1_symbol)  
        player_2_winning_decision = victory_check(location_list,player_2_symbol)
      
        #Sending the winner message 
        if player_1_winning_decision[0] == True and player_1_winning_decision[1] == player_1_symbol:
            winning_condition = True
            print("player 1 wins")
            break 
        elif player_2_winning_decision[0] == True and player_2_winning_decision[1] == player_2_symbol:
            print("Player_2 wins")
            winning_condition = True
        elif location_list.count(" ") == 0:
            print("draw game")
            winning_condition = True # itmay seem confusuing but winning codition is mnerely used a a flag 
    
main_game()
