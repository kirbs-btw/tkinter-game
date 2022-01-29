import asyncio
import tkinter as tk
import time

### Preclaimer !! #############
### IMPORTANT !!!
### What i´m doing is just dumb you should never try to
### code a game in tkinter !!!
### thats only some dumb play around with classes and movement scripts lol

class player:
    def __init__(self, x, y, canvas, root):
        self.posx = x
        self.posy = y
        self.widget = canvas
        self.root = root

    def show(self):
        print(f"posx: {self.posx}")
        print(f"posy: {self.posy}")

class enemy:
    def __init__(self, x, y, canvas, root, width):
        self.posx = x
        self.posy = y
        self.widget = canvas
        self.root = root
        self.width = width

    def show(self):
        print(f"posx: {self.posx}")
        print(f"posy: {self.posy}")

"""
initiate the required objects  
"""

enemy = player(None, None, None, None)

player = player(None, None, None, None)
player.posx = 250
player.posy = 450


def main():
    """
    main function - starts the "game"
    :return:
    """

    root = tk.Tk()
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    player.widget = tk.Canvas(canvas, bg="#325599", width=50, height=50)
    player.widget.place(x=player.posx, y=player.posy)
    player.root = canvas

    enemy.root = canvas
    instanceEnemy()

    dButton = tk.Button(canvas, text="D", command=lambda: moveD())
    dButton.place(x=30, y=20)

    aButton = tk.Button(canvas, text="A", command=lambda: moveA())
    aButton.place(x=10, y=20)

    root.mainloop()

def moveD():
    """
    moves the player to the right

    :return:
    """
    player.posx += 50
    player.widget.destroy()
    player.widget = tk.Canvas(player.root, bg="#325599", width=50, height=50)
    player.widget.place(x=player.posx, y=player.posy)
    doChecks()



def moveA():
    """
    moves the player to the left

    :return:
    """
    player.posx -= 50
    player.widget.destroy()
    player.widget = tk.Canvas(player.root, bg="#325599", width=50, height=50)
    player.widget.place(x=player.posx, y=player.posy)
    doChecks()

def doChecks():
    enemyMove()
    collisionCheck()

def doFail():
    print("you lose")
    enemy.widget.destroy()
    player.widget.destroy()

    player.root.create_text(250, 100, text="you lose!", font=("Gotham Black", 25))

def collisionCheck():
    if player.posx == enemy.posx and player.posy == enemy.posy:
        doFail()

def instanceEnemy():
    if enemy.widget != None:
        enemy.widget.destroy()
    enemy.posx = 250
    enemy.posy = -50
    enemy.width = 50
    enemy.widget = tk.Canvas(enemy.root, bg="#221fff", width=50, height=50)
    enemy.widget.place(x=enemy.posx, y=enemy.posy)

def enemyMove():
    if enemy.posy > 450:
        instanceEnemy()
    enemy.posy += 50
    enemy.widget.destroy()
    enemy.widget = tk.Canvas(player.root, bg="#ff0021", width=enemy.width, height=enemy.width)
    enemy.widget.place(x=enemy.posx, y=enemy.posy)

if __name__ == '__main__':
    main()

#credits Bastian Lipka