import pygame as pg
import numpy as np
from input_ import INPUT


class UI:

    @staticmethod
    def load_button(png: str = "assets/buttons.png", scale: tuple[int, int] = (512, 160)) -> tuple[pg.Surface, ...]:
        img = pg.image.load(png)
        # img=pg.transform.smoothscale(raw_img,scale)
        button_rects = []
        for button in range(5):
            button_rects.append(pg.Rect(0, button*64, 1024, 64))
        buttons = []
        for button_rect in button_rects:
            buttons.append(img.subsurface(button_rect))
        return tuple(buttons)

    button_enabled, button_disabled, button_mouseover, button_mousedown, button_shadow = load_button()

    def __init__(self, screen: pg.Surface,  font: pg.font.Font) -> None:
        UI.buttons: list["BUTTON"] = []
        UI.screen = screen
        UI.font = font

        _start_button = BUTTON(text="START", func=lambda: (setattr(INPUT, "screen_ui", False),
                                                          setattr(INPUT, "screen_play", True)))
        _exit_button = BUTTON(loc=(0, 96), text="EXIT", func=lambda: (setattr(INPUT, "screen_ui", False),
                                                                     setattr(
                                                                         INPUT, "screen_play", False),
                                                                     setattr(INPUT, "is_game_running", False)))
        # UI.play_button_rect = UI.button_disabled.get_rect(
        #     center=(UI.center[0], UI.center[1]))
        # UI.exit_button_rect = UI.button_disabled.get_rect(
        #     center=(UI.center[0], UI.center[1]+96))
        # UI.rects = [UI.play_button_rect, UI.exit_button_rect]
        UI._click_sec = 0

    @staticmethod
    def render(mouse_pos: tuple[int, int]) -> None:
        UI._click_sec -= 1 if UI._click_sec > 0 else 0
        if INPUT.click:
            UI._click_sec = 5
        for button in UI.buttons:
            if button.rect.collidepoint(mouse_pos):
                if UI._click_sec:
                    button.state = "tap"
                    if UI._click_sec == 1:
                        button.func()
                else:
                    button.state = "mouse_over"
            else:
                button.state = "enabled"
            button.render()

    @staticmethod
    def display_info(res_info) -> None:
        UI.center = (res_info.current_w//2, res_info.current_h//2)


class BUTTON:
    def __init__(self,
                 loc: tuple[int, int] = (0, 0),
                 text: str = "no_button_text",
                 init_surface: pg.Surface = UI.button_disabled,
                 func=lambda: ...) -> None:  # pylint: disable=unnecessary-lambda
        UI.buttons.append(self)
        self.func = func
        self.state = "enabled"
        self.rect = init_surface.get_rect(center=np.add(UI.center, loc))
        self.text = UI.font.render(text, True, (255, 255, 245))
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def render(self) -> None:
        if self.state == "enabled":
            UI.screen.blit(UI.button_enabled, self.rect)
        elif self.state == "mouse_over":
            UI.screen.blit(UI.button_mouseover, self.rect)
        elif self.state == "tap":
            UI.screen.blit(UI.button_mousedown, self.rect)
        UI.screen.blit(self.text, self.text_rect)
        pass
