import random
from game import Game

names = ['иван', 'мария', 'петр', 'анна', 'дмитрий', 'елена']
my_game = Game()

n = random.randint(4, 6)
for i in range(1, n+1):
    my_game.add(i, random.choice(names))

k_step = random.randint(2, 3)
my_game.run(k_step, 'log.txt')

print('\nготово! лог игры в файле log.txt')