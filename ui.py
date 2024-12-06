import pygame as pg
import numpy as np
from input_ import INPUT


class UI:
    def __init__(self, font: pg.font.Font) -> None:
        UI.buttons = []
        UI.font = font
        UI.button_enabled, UI.button_disabled, UI.button_mouseover, UI.button_mousedown, UI.button_shadow = UI.load_button()
        play_button = BUTTON(text="START",func=lambda:setattr(INPUT,"screen_ui",False),setattr(INPUT,"",True))
        exit_button = BUTTON(loc=(0, 96), text="EXIT")
        # UI.play_button_rect = UI.button_disabled.get_rect(
        #     center=(UI.center[0], UI.center[1]))
        # UI.exit_button_rect = UI.button_disabled.get_rect(
        #     center=(UI.center[0], UI.center[1]+96))
        # UI.rects = [UI.play_button_rect, UI.exit_button_rect]
        UI._click_sec = 0

    @staticmethod
    def render(screen: pg.Surface, mouse_pos: tuple[int, int]) -> None:
        UI._click_sec -= 1 if UI._click_sec > 0 else 0
        if INPUT.click:
            UI._click_sec = 5
        for button in UI.buttons:
            if button.rect.collidepoint(mouse_pos):
                if UI._click_sec:
                    button.state = "tap"
                    if UI._click_sec == 1:
                        if button_rect == UI.play_button_rect:
                            INPUT.screen_ui = False
                            INPUT.screen_play = True
                        elif button_rect == UI.exit_button_rect:
                            INPUT.screen_play = False
                            INPUT.screen_ui = False
                            INPUT.is_game_running = False
                else:
                    screen.blit(UI.button_mouseover, button_rect.topleft)
            else:
                button.state = "enabled"
            if button_rect == UI.play_button_rect:     screen.blit(
                play_button_text, play_button_text_loc)

                play_button_text = font.render("START", True, (255, 255, 245))
                play_button_text_loc = play_button_text.get_rect(
                    center=button_rect.center)
              elif button_rect == UI.exit_button_rect:
                exit_button_text = font.render("EXIT", True, (255, 255, 245))
                exit_button_text_loc = exit_button_text.get_rect(
                    center=button_rect.center)
                screen.blit(exit_button_text, exit_button_text_loc)

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

    @staticmethod
    def display_info(res_info) -> None:
        UI.center = (res_info.current_w//2, res_info.current_h//2)


class BUTTON:
    def __init__(self,
                loc=(0, 0),
                text: str="no_button_text",
                init_surface:pg.Surface=UI.button_disabled,
                func:function=NotImplemented) -> None:
        UI.buttons.append(self)
        self.state="enabled"
        self.rect = init_surface.get_rect(center=np.add(UI.center, loc))
        self.text = UI.font.render(text, True, (255, 255, 245))
