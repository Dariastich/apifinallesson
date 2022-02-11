import os
import sys
import pygame
import resquests


def load_map(object):
    map_params = {
        "ll": object.ll(),
        "l": object.type,
        "z": object.zoom,
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    if not response:
        print("Ошибка")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    return map_file



class MapObject():
    def __init__(self):
        self.lat = 55.733842
        self.lon = 37.588144
        self.zoom = 16
        self.type = 'map'

    def ll(self):
        return str(sellf.lon) + ',' + str(self.lat)

        def update(self, event):
            if event.key == pygame.K_PAGEUP and self.zoom < 20:
                self.zoom += 1
            if event.key == pygame.K_PAGEDOWN and self.zoom > 2:
                self.zoom -= 1

    [19: 43]
    if event.type == pygame.KEYUP:
        map.update(event)

pygame.init()
screen = pygame.dsplay.set_mode((600, 450))

map = MapObject()


while True():
    event = pygame.event.ait()
    if event.type == pygame.QUIT:
        break

    map_file = load_map(map)
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()

pygame.quit()
os.remove(map_file)