import rockPaperScissorsMod as mc

while True:
    try:
        user_action = mc.user_selection()
        computer_action = mc.comp_ans()
        winner = mc.determine_winner(user_action, computer_action)
        reTry = mc.try_again()

        if reTry != True:
            break
        print(mc.get_score())
    except KeyboardInterrupt:
        break
