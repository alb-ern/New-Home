import pygame as pg
import numpy as np
from character import Character
from ui import UI


Chars = Character.Chars


class GUI:
    def __init__(
        self,
        game,
        game_background_color: tuple[int, ...] = (160, 140, 110)
    ) -> None:
        self.game = game
        self.background_color = game_background_color
        pg.init()
        self.font = pg.font.Font(None, 36)
        self.screen_init()
        UI(self.screen, self.font)
        for char in Chars:
            setattr(char, "_img", self.load_img(char.img_name))
        self.bars()
        self._find_player()

    def screen_init(self):
        self.res_info = pg.display.Info()
        UI.display_info(self.res_info)
        self.screen = pg.display.set_mode(
            (self.res_info.current_w, self.res_info.current_h), pg.DOUBLEBUF
        )
        pg.display.set_caption("New Home the Game by pythonGodXx")

    def bars(self):
        self.right_bar = pg.Surface((64 * 3, self.res_info.current_h))
        self.bottom_bar = pg.Surface((self.res_info.current_w, 96))

    def _find_player(self):
        for char in Chars:
            if char.name == "player":
                self.player = char
                break

    def refresh_ui(self) -> None:  # refreshes ui in constant frame loop
        self.screen.fill((100, 100, 100))
        # ui elements here
        UI.render(pg.mouse.get_pos())
        ###
        pg.display.flip()

    def _ref_game_ui(self) -> None:  # refreshes game_ui bars in constant frame loop
        self.right_bar.fill((50, 20, 0))
        self.screen.blit(self.right_bar, (self.res_info.current_w - 3 * 64, 0))
        self.bottom_bar.fill((50, 20, 0))
        self.screen.blit(self.bottom_bar, (0, self.res_info.current_h - 96))

    def refresh_game(self) -> None:
        self.screen.fill(self.background_color)
        self._ref_game_ui()

        np.where(self.game.arr == self.player.name)
        
        for char in Chars:
            # type: ignore # char.loc
            np.where(self.game.arr == char.name)  # TODO:do this
            self.screen.blit(getattr(char, "_img"), char.img_loc)

        pg.display.flip()

    # will look for png assets
    def load_img(self, png: str, scale: tuple[int, int] = (64, 64)) -> pg.Surface:
        raw_img = pg.image.load("assets/" + png + ".png")
        img_out = pg.transform.smoothscale(raw_img, scale)
        return img_out


if __name__ == "__main__":
    pass
    # GUI()
