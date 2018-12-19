The goal of this project was to create a basic AI from reinforcement learning for the tic Tac toe game.

I made this project because Reinforcement learning is something interesting me a lot and it was a good thing to begin with this kind of project.

Actually, in my tic Tac toe game, you will play in a row against two AI. 
    "score" is only trained with 1 and -1 rewards if the AI win or lose.
    "equality" is trained with 1 and -1 rewards and I've added a reward of 0.5 if there's an equality.

*I kept the code that deserves me to train my AI (available below)*
*If you want to use it there is a list with all kinds of terrain I've made*
    *-Train p1 and p2 with random player*
    *-Train the trained p1 against the trained p2*
    *-Train p1 and p2 against random player*
    *-Test p1 against random player*


***Train p1 and p2 with random player***
``` 
    x = trained_player1.eps
    y = trained_player2.eps
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
```

***Train the trained p1 against the trained p2***

```
    p1.eps = 0
    p2.eps = 0.99
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
```

***Train p1 and p2 against random player***
```
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
```

***Test p1 against random player***
```
    p1.reset_stat()
    p2.reset_stat()
    for _ in range(0, 1000):
        play(game, p1, random_player, train=False)
    print("p1 win rate", p1.win_nb/1000.)
    print("p1 win mean", np.mean(p1.rewards))
    with open('equalityp1.txt', 'w') as file:
        file.write(json.dumps(p1.V))
    with open('equalityp2.txt', 'w') as file:
        file.write(json.dumps(p2.V))
```
