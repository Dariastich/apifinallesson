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
            elif event.key == pygame.K_PAGEDOWN and self.zoom > 2:
                self.zoom -= 1
            elif event.key == pygame.K_LEFT:
                self.lon -= LON_STEP * (2 ** (15 - self.zoom))
            elif event.key == pygame.K_RIGHT:
                self.lon += LON_STEP * (2 ** (15 - self.zoom))
            elif event.key == pygame.K_UP and self.lat < 70:
                self.lat += LAT_STEP * (2 ** (15 - self.zoom))
            elif event.key == pygame.K_DOWN and self.lat > -65:
                self.lat -= LAT_STEP * (2 ** (15 - self.zoom))

            if self.lon > 180:
                self.lon = self.lon - 360
            if self.lon < -180:
                self.lon = self.lon + 360

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