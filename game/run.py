# run.py

# import game.sound.echo
# game.sound.echo.echo_test()

# from game.sound import echo
# echo.echo_test()

# from game.sound.echo import echo_test
# echo_test()

# *을 이용하여 import할 때는 sound/init.py에 __all__ = ['echo']를 추가해야한다.
from game.sound import *
echo.echo_test()

from game.graphic.render import render_test
render_test()
