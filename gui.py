import pygame as pg
from character import Character
Chars = Character.Chars


class GUI:
    def __init__(self, background_color=(160, 140, 110)) -> None:
        self.background_color = background_color
        pg.init()
        res_info = pg.display.Info()
        self.screen = pg.display.set_mode(
            (res_info.current_w, res_info.current_h-50))
        pg.display.set_caption("New Home the Game by pythonGodXx")

        for char in Chars:
            char.img = GUI.load_img(char.img_name)
        #
        # active = True
        # clock = pg.time.Clock()
        # ======================================
        # LOOOP CARIIED TO loop.py
        # ======================================
        # # while active:
        # #     for event in pg.event.get():
        # #         if event.type == pg.QUIT:
        # #             active = False
        # #         elif event.type == pg.KEYDOWN:
        # #             if event.key == pg.K_RIGHT:
        # #                 pass

        # #     self.screen.fill((150, 0, 0))
        # #     for char in Chars:
        # #         self.screen.blit(char.img, char.loc)

        # #     pg.display.flip()

        # #     clock.tick(30)
        # # print(Chars)
        # # pg.quit()
        print("gui init")

    def refresh(self) -> None:
        self.screen.fill(self.background_color)
        for char in Chars:
            self.screen.blit(char.img, char.loc)

        pg.display.flip()

    @staticmethod
    def load_img(png: str, scale: tuple[int, int] = (64, 64)) -> pg.Surface:
        raw_img = pg.image.load("assets/"+png+".png")
        img_out = pg.transform.smoothscale(raw_img, scale)
        return img_out


if __name__ == "__main__":
    GUI()
