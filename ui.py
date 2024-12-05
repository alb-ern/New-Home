import pygame as pg
from input_ import INPUT


class UI:
    def __init__(self) -> None:
        UI.button_enabled, UI.button_disabled, UI.button_mouseover, UI.button_mousedown, UI.button_shadow = UI.load_button()
        UI.play_button_rect = UI.button_disabled.get_rect(
            center=(UI.center[0], UI.center[1]))
        UI.exit_button_rect = UI.button_disabled.get_rect(
            center=(UI.center[0], UI.center[1]+96))
        UI.rects = [UI.play_button_rect,UI.exit_button_rect]
        UI._click_sec = 0

    @staticmethod
    def render(screen: pg.Surface, mouse_pos: tuple[int, int], font: pg.font.Font) -> None:
        UI._click_sec -= 1 if UI._click_sec > 0 else 0
        if INPUT.click:
            UI._click_sec = 5
        for button_rect in UI.rects:
            if button_rect.collidepoint(mouse_pos):
                if UI._click_sec:
                    screen.blit(UI.button_mousedown, button_rect.topleft)
                    if UI._click_sec == 1:
                        if button_rect==UI.play_button_rect:
                            INPUT.screen_ui = False
                            INPUT.screen_play = True
                        elif button_rect==UI.exit_button_rect:
                            INPUT.screen_play=False
                            INPUT.screen_ui=False
                            INPUT.is_game_running=False
                else:
                    screen.blit(UI.button_mouseover, button_rect.topleft)
            else:
                screen.blit(UI.button_enabled, button_rect.topleft)
            if button_rect==UI.play_button_rect:
                play_button_text = font.render("START", True, (255, 255, 245))
                play_button_text_loc = play_button_text.get_rect(
                    center=button_rect.center)
                screen.blit(play_button_text, play_button_text_loc)
            elif button_rect==UI.exit_button_rect:
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
    def __init__(self) -> None:
        pass