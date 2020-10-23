import easygui

welcomemessage = "welcome to the vendning machine. Would you like to purchase anything today?"
title = "vending machine"
choices = ['Yes', 'No']
userchoice = easygui.ynbox(welcomemessage, title, choices)

if userchoice == 1:
    question = "what will you be purchasing?"
    title = "vending machine"
    choices = ["Skittles: $2.50", "M&Ms: $1.75",  "Smarties: $1.00", "Rockets: $0.75", "Cocaine: $100.00/brick"]
    choice = easygui.buttonbox(question, title, choices)
    
    msg = "How many packets or kilos?: "
    title = "vending machine"
    packetnumber = easygui.integerbox(msg, title)

    if choice == "Cocaine":
        totalcoke = "Your total is 100" + "msg"
        easygui.msgbox(totalcoke)


    
else:
    goodbyemessage = "have a good day wanker!"
    title = "vending machine"
    easygui.msgbox(goodbyemessage, title, ok_button = 'OK')
