``` 
    x = trained_player1.eps
    y = trained_player2.eps
    print('Train p1 and p2 with rand')
    for i in range(0, 70000):
        if i % 10 == 0:
            trained_player1.eps = x
            trained_player2.eps = y
            trained_player1.eps = max(trained_player1.eps*0.999, 0.05)
            trained_player2.eps = max(trained_player2.eps*0.999, 0.05)
            x = trained_player1.eps
            y = trained_player2.eps
        if i % 1000 == 0:
            trained_player1.eps = 0
            trained_player2.eps = 0
            trained_player1.reset_stat()
            trained_player2.reset_stat()
            # Play agains a random player
            for _ in range(0, 100):
                play(game, trained_player1, random_player, train=False)
                play(game, trained_player2, random_player, train=False)
            trained_player1.eps = x
            trained_player2.eps = y
            print("eps=%sp1 win rate=%s" % (trained_player1.eps, trained_player1.win_nb/100.))
            print("eps=%sp1 win rate=%s" % (trained_player2.eps, trained_player2.win_nb/100.))
            print()
        play(game, trained_player1, trained_player2)
    p1.eps = 0
    p2.eps = 0.99
    print('train p1 trained against p2 trained')
    for _ in range(0, 100000):
        if _ % 50 == 0:
        if _ % 1000 == 0:
            trained_player1.reset_stat()
            trained_player2.reset_stat()
            for _ in range(0, 100):
                play(game, trained_player1, random_player, train=False)
                play(game, trained_player2, random_player, train=False)
            print("eps=%sp1 win rate=%s" % (trained_player1.eps, trained_player1.win_nb/100.))
            print("eps=%sp1 win rate=%s" % (trained_player2.eps, trained_player2.win_nb/100.))
        play(game, trained_player1, trained_player2)
    p1.eps = 0
    p2.eps = 0
    while True:
        play(game, p1, human)
        if input("If you want to play again, enter 'c'>>") == 'c':
            continue
        else:
            break
    print('train p1 and p2 against random player')
    for _ in range(0, 30000):
        if _ % 1000 == 0:
            p1.reset_stat()
            p2.reset_stat()
            for _ in range(0, 100):
                play(game, p1, random_player, train=False)
                play(game, p2, random_player, train=False)
            print("eps=%sp1 win rate=%s" % (p1.eps, p1.win_nb/100.))
            print()
            print("eps=%sp2 win rate=%s" % (p2.eps, p2.win_nb/100.))
        play(game, p1, random_player)
        play(game, p2, random_player)
    p1.reset_stat()
    p2.reset_stat()
    print('test p1 against random player')
    for _ in range(0, 1000):
        play(game, p1, random_player, train=False)
    print("p1 win rate", p1.win_nb/1000.)
    print("p1 win mean", np.mean(p1.rewards))
    with open('equalityp1.txt', 'w') as file:
        file.write(json.dumps(p1.V))
    with open('equalityp2.txt', 'w') as file:
        file.write(json.dumps(p2.V))
```