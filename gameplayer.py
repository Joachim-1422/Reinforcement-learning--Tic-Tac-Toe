#!/usr/bin/env python3


from random import randint
from copy import deepcopy
import random

class TicTacToePlayer(object):

    def __init__(self, stack, is_human, trainable=True):
        super(TicTacToePlayer, self).__init__()
        self.is_human = is_human
        self.history = []
        self.V = {}
        self.V[str([[0, 0, 0], [0, 0, 0], [0, 0, 0]])] = 0.
        self.win_nb = 0.
        self.lose_nb = 0.
        self.rewards = []
        self.eps = 0.99
        self.trainable = trainable
        self.stack = stack

    def reset_stat(self):
        self.win_nb = 0
        self.lose_nb = 0
        self.rewards = []

    def checkadd_vs(self, state):
        if str(state) in self.V:
            return
        else:
            self.V[str(state)] = 0.

    def end_game(self, state, a, a_list, game):
        #print("j")
        a_list.remove(a)
        if not a_list:
            return 2
        elif game.is_finished(state) != 1:
            return 3
        else:
            return 1

    def greedy_step(self, state, game, p):
        actions = deepcopy(game.a_list)
        vmin = None
        vi = None
        states = deepcopy(state)
        gamos = deepcopy(game.a_list)
        #print(gamos)
        #print(len(actions))
        #print(state)
        for i in range(0, len(actions)):
            a = deepcopy(actions[i])
            #print("x", a)
            states = deepcopy(state)
            #print("i", i)
            if self.end_game(states, a, gamos, game) == 1:
                #print("k")
                states[a[0]][a[1]] = p
                self.checkadd_vs(states)
                s = str(states)
                #print("vmin", vmin)
                #print("vs", self.V[s])
                if (vmin is None or vmin < self.V[s]):
                    vmin = self.V[s]
                    vi = i
            gamos = deepcopy(game.a_list)
        #print("vi", vi)
        return actions[vi if vi is not None else 0]

    def play(self, state, game, p):
        if self.is_human is False:
            if random.uniform(0, 1) < self.eps:
                x = randint(0, len(game.a_list) - 1)
                action = deepcopy(game.a_list[x])
            else:
                action = self.greedy_step(state, game, p)
        else:
            action = [int(x) for x in input("$>").split()]
        self.checkadd_vs(state)
        return action

    def add_transition(self, n_tuple):
        self.history.append(n_tuple)
        s, r, sp = n_tuple
        self.rewards.append(r)

    def train(self):
        if not self.trainable or self.is_human is True:
            return
        x = 0
        for transition in reversed(self.history):
            s, r, sp = transition
            if x == 0:
                self.V[sp] = self.V[sp] + 0.01*(r - self.V[sp])
            self.V[s] = self.V[s] + 0.01*(self.V[sp] - self.V[s])
            x += 1

        #print("hist", self.history)
        self.history = []