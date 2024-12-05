import pygame as pg



class UI:
    def __init__(self) -> None:
        UI.button_enabled, UI.button_disabled, UI.button_mouseover, UI.button_mousedown, UI.button_shadow = UI.load_button()
    @staticmethod
    def render(screen):
        screen.blit(UI.button_disabled,(UI.center[0]-512,UI.center[1]-32))
        pass
    @staticmethod
    def load_button(png: str = "assets/buttons.png", scale: tuple[int, int] = (512, 160)) -> tuple[pg.Surface,...]:
        img = pg.image.load(png)
        #img=pg.transform.smoothscale(raw_img,scale)
        button_rects = []
        for button in range(5):
            button_rects.append(pg.Rect(0, button*64, 1024, 64))
        buttons = []
        for button_rect in button_rects:
            buttons.append(img.subsurface(button_rect))
        return tuple(buttons)
    @staticmethod
    def display_info(res_info):
        UI.center = (res_info.current_w//2, res_info.current_h//2)