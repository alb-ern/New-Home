import pygame as pg
from character import Character
Chars=Character.Chars


class GUI:
    def __init__(self) -> None:

        pg.init()
        res_info = pg.display.Info()
        screen = pg.display.set_mode(
            (res_info.current_w, res_info.current_h-50))
        pg.display.set_caption("New Home the Game by pythonGodXx")


        for char in Chars:
             = GUI.load_img("knight")

        active = True
        clock = pg.time.Clock()

        while active:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    active = False
                elif event.type == pg.KEYDOWN:
                    if event.key==pg.K_RIGHT:
                        pass

            screen.fill((150, 0, 0))
            screen.blit(img_knight, (0, 0))

            pg.display.flip()

            clock.tick(30)

        pg.quit()

    @staticmethod
    def load_img(png: str, scale: tuple[int, int] = (64, 64)) -> pg.Surface:
        raw_img = pg.image.load("assets/"+png+".png")
        img_out = pg.transform.smoothscale(raw_img, scale)
        return img_out


if __name__ == "__main__":
    GUI()
