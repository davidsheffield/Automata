import automata


if __name__ == '__main__':
    game = automata.conway.Conway([100, 100], 0.2)
    game.run_show(30)
