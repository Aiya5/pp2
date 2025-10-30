import time
import pygame as pg
pg.init()

oliviaPath = "C:/Users/Гульжан/Desktop/pp2/pygame 7/songs/OliviaRo.mp3"
sabrinaPath = "C:/Users/Гульжан/Desktop/pp2/pygame 7/songs/SabrinaTears.mp3"
twicePath = "C:/Users/Гульжан/Desktop/pp2/pygame 7/songs/TwiceStrategy.mp3"
sc = pg.display.set_mode((720, 711))
pg.display.set_caption("slayyy")
clock = pg.time.Clock()
olivia = pg.mixer.music.load(oliviaPath)
sabrina = pg.mixer.music.load(sabrinaPath)
twice = pg.mixer.music.load(twicePath)
musicList = [twicePath, sabrinaPath, oliviaPath]
pg.mixer.music.play(-1)
penguin = pg.image.load("C:/Users/Гульжан/Desktop/pp2/pygame 7/penguin.jpg")
sc.blit(penguin, (0, 0))
Play = False
run = True
index = 0
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                Play = not Play
                if Play:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key == pg.K_RIGHT:
                index += 1
                if index == len(musicList):
                    index = 0
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()
            elif event.key == pg.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(musicList)-1
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()

    pg.display.flip()
    clock.tick(60)