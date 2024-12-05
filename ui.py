import pygame as pg
from loop import LOOP


class UI:
    def __init__(self) -> None:
        UI.button_enabled, UI.button_disabled, UI.button_mouseover, UI.button_mousedown, UI.button_shadow = UI.load_button()
        UI.play_button_rect = UI.button_disabled.get_rect(
            topleft=(UI.center[0]-512, UI.center[1]-32))
        UI.rects = [UI.play_button_rect]
        UI._click_sec=0

    @staticmethod
    def render(screen, mouse_pos) -> None:
        UI._click_sec-=1 if UI._click_sec>0 else 0
        if LOOP.click:
            UI._click_sec=8
        for button_rect in UI.rects:
            if button_rect.collidepoint(mouse_pos):
                if UI._click_sec:
                    screen.blit(UI.button_mousedown, button_rect.topleft)
                    if UI._click_sec==1:
                        LOOP.screen_ui=False
                        LOOP.screen_play=True
                else:
                    screen.blit(UI.button_mouseover, button_rect.topleft)
            else:
                screen.blit(UI.button_enabled, button_rect.topleft)
        pass

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
