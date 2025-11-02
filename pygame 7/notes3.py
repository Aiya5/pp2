'''
Playing a song once:
pygame.mixer.music.load('foo.mp3')
pygame.mixer.music.play(0)


Playing a song infinitely:
pygame.mixer.music.load('foo.mp3')
pygame.mixer.music.play(-1)

And write a function that chooses a different song randomly that gets called each time the SONG_END event is fired:
import random

def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song:
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()
    
    
Or if you want them to play in the same sequence each time:
    def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
    
        minute_angle = now.minute * -6  # 360/60 = 6 degrees per minute
    second_angle = now.second * -6  # 360/60 = 6 degrees per second
'''

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