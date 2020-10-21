# The Loast Coast: Developed for PyWeek 30

## Why does this game exist?
Besides the fact that we wanted to take up a challenge from the Python community and do something random, we've all had an innate interest in games and game development to an extent. [PyWeek](https://pyweek.org/) is a bi-annual game jam that promotes writing games for fun in Python, so when the opportunity came, it was hard to pass up. This game was made in a span of 4 days for PyWeek 30. Check out our entry [here](https://pyweek.org/e/nopace/)!

### Update: The ratings are out!
![Game ratings](https://raw.githubusercontent.com/LiquidDazee/PyWeek30/master/screenshots/scores.png)

## Getting Started
To install this game, first clone this git repository.
```shell
git clone https://github.com/Not-Pace/PyWeek30.git
```

Navigate to the folder and make a quick virtual environment to run the game:

```shell
virtualenv .game
```

On UNIX/Linux/WSL:
```shell
source .game/bin/activate
```

On Windows
```shell
source .game/Scripts/activate
```

Install all the dependencies from the  `requirements.txt` folder.
```shell
pip install -r requirements.txt
```

Now run main.py to run the game!

```shell
python main.py
```

## Again, what's this game about?
The Loast Coast is the name of the Discord server that we've created for our friends, and our aim was to kinda make a game celebrating (read: roasting) people from the server, while also abiding by the theme of the challenge, which was *Castaway*. Thus we created this game. The objective of this game is to escape the island to get to the (Loast) coast. The island is haunted by ghosts, and littered around are items that could make the game easier to finish.

![Splash Screen](https://raw.githubusercontent.com/Not-Pace/PyWeek30/master/screenshots/ss2.PNG)

## Libraries Used

We made this entire game using:
- [PyGame](https://www.pygame.org/news)
- [PyTMX](https://pypi.org/project/PyTMX/)
- [Tiled Map Editor](https://www.mapeditor.org/)

The sprites we used were from the [Kenney 1-bit Pack](https://www.kenney.nl/assets/bit-pack)
