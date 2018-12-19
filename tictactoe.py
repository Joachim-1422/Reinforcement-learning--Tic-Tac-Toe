#!/usr/bin/env python3

import gameenv
import gameplayer
import random
import json
import numpy as np

def js_r(filen):
   with open(filen) as f_in:
       return(json.load(f_in))

def play(game, p1, p2, train=True):
    state = game.reset()
    players = [p1, p2]
    random.shuffle(players)
    p = 0
    if not game.a_list:
        state = game.reset()
    while game.is_finished(state) == 1:
        players[p%2].checkadd_vs(state)
        tmp = str(state.copy())
        if players[p%2].is_human:
            print('your turn')
            game.display()
        action = players[p%2].play(state, game, players[p%2].stack)
        n_state, reward = game.step(action, players[p%2].stack)
        game.a_list.remove(action)
        players[p%2].checkadd_vs(state)
        players[p%2].checkadd_vs(n_state)
        if (reward != 0):
            players[p%2].lose_nb += 1. if reward == -1 else 0
            players[p%2].win_nb += 1. if reward == 1 else 0
            players[(p+1)%2].lose_nb += 1. if reward == 1 else 0
            players[(p+1)%2].win_nb += 1. if reward == -1 else 0
            players[p%2].add_transition((tmp, reward, str(n_state)))
            players[(p+1)%2].add_transition((tmp, reward * -1, str(n_state)))
        elif len(game.a_list) == 1 and players[(p+1)%2].end_game(state, game.a_list[0], game.a_list, game) == 2:
            reward = 0.6
            players[p%2].win_nb += 1.
            players[(p+1)%2].win_nb += 1.
            players[p%2].add_transition((tmp, reward, str(n_state)))
            players[(p+1)%2].add_transition((tmp, reward, str(n_state)))
        else:
            players[p%2].add_transition((tmp, reward, str(n_state)))
            players[(p+1)%2].add_transition((tmp, reward, str(n_state)))
        state = n_state.copy()
        p += 1
        players[p%2].checkadd_vs(state)
        players[p%2].checkadd_vs(n_state)
    if train:
        p1.train()
        p2.train()

if __name__ == '__main__':
    game = gameenv.TicTacToeEnv([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    p1 = gameplayer.TicTacToePlayer(stack=1, is_human=False, trainable = True)
    p2 = gameplayer.TicTacToePlayer(stack=2, is_human=False, trainable = True)
    trained_player1 = gameplayer.TicTacToePlayer(stack=1, is_human=False, trainable = False)
    trained_player2 = gameplayer.TicTacToePlayer(stack=1, is_human=False, trainable = False)
    human = gameplayer.TicTacToePlayer(stack=2, is_human=True, trainable = False)
    random_player = gameplayer.TicTacToePlayer(stack=2, is_human=False, trainable = False)
    random_player.eps = 1
    trained_player1.V = js_r('scorep1.txt')
    trained_player2.V = js_r('equalityp1.txt')
    trained_player1.eps = 0
    trained_player2.eps = 0    

##    # Play agains us
    print('p1')
    while True:
        play(game, trained_player1, human)
        if input("If you want to play again, enter 'c'>>") == 'c':
            continue
        else:
            break
    print('p2')
    while True:
        play(game, trained_player2, human)
        if input("If you want to play again, enter 'c'>>") == 'c':
            continue
        else:
            break