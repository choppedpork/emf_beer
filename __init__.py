import wifi
import urequests, ujson

import vga2_8x16 as font

from tidal import *
from app import TextApp

def get_remaining(x):
    return x["remaining_pct"]

class Beer(TextApp):
    TITLE = "beer"
    BG = BLACK
    FG = WHITE

    # fake_list = b'{"ales": [{"id": 233, "stocktype_id": 82, "manufacturer": "Bristol Beer", "name": "Fortitude", "abv": "4.0", "fullname": "Bristol Beer Fortitude (4.0% ABV)", "price": "4.00", "remaining_pct": "25.69444444444444444400"}, {"id": 221, "stocktype_id": 75, "manufacturer": "Ledbury", "name": "Rock the Hops Pale Ale", "abv": "4.2", "fullname": "Ledbury Rock the Hops Pale Ale (4.2% ABV)", "price": "4.20", "remaining_pct": "77.77777777777777777800"}, {"id": 122, "stocktype_id": 23, "manufacturer": "Milton", "name": "Justinian", "abv": "3.9", "fullname": "Milton Justinian (3.9% ABV)", "price": "4.00", "remaining_pct": "42.70833333333333333300"}, {"id": 128, "stocktype_id": 25, "manufacturer": "Milton", "name": "Nero", "abv": "5.0", "fullname": "Milton Nero (5.0% ABV)", "price": "4.40", "remaining_pct": "42.36111111111111111100"}], "kegs": [{"id": 184, "stocktype_id": 47, "manufacturer": "Cloudwater", "name": "Happy", "abv": "3.5", "fullname": "Cloudwater Happy (3.5% ABV)", "price": "4.90", "remaining_pct": "42.23484848484848484800"}, {"id": 10, "stocktype_id": 2, "manufacturer": "Dortmunder", "name": "Vier", "abv": "4.0", "fullname": "Dortmunder Vier (4.0% ABV)", "price": "4.00", "remaining_pct": "65.34090909090909090900"}, {"id": 155, "stocktype_id": 33, "manufacturer": "Five Points", "name": "Pale", "abv": "4.4", "fullname": "Five Points Pale (4.4% ABV)", "price": "4.50", "remaining_pct": "55.11363636363636363600"}, {"id": 167, "stocktype_id": 37, "manufacturer": "Lost & Grounded", "name": "Hop-Hand Fallacy", "abv": "4.4", "fullname": "Lost & Grounded Hop-Hand Fallacy (4.4% ABV)", "price": "4.50", "remaining_pct": "94.31818181818181818200"}, {"id": 134, "stocktype_id": 26, "manufacturer": "Milton", "name": "Dynamo", "abv": "3.9", "fullname": "Milton Dynamo (3.9% ABV)", "price": "4.50", "remaining_pct": "97.72727272727272727300"}], "ciders": [{"id": 246, "stocktype_id": 94, "manufacturer": "Gwatkin", "name": "Farmhouse Perry (Medium)", "abv": "6.0", "fullname": "Gwatkin Farmhouse Perry (Medium) (6.0% ABV)", "price": "4.30", "remaining_pct": "13.35227272727272727300"}, {"id": 252, "stocktype_id": 100, "manufacturer": "Llanblethian Orchards", "name": "May Day (Sweet)", "abv": "6.2", "fullname": "Llanblethian Orchards May Day (Sweet) (6.2% ABV)", "price": "4.50", "remaining_pct": "17.61363636363636363600"}, {"id": 236, "stocktype_id": 84, "manufacturer": "Severn Cider", "name": "Dry", "abv": "5.8", "fullname": "Severn Cider Dry (5.8% ABV)", "price": "4.40", "remaining_pct": "46.02272727272727272700"}, {"id": 3, "stocktype_id": 1, "manufacturer": "Westons", "name": "Stowford Press", "abv": "4.5", "fullname": "Westons Stowford Press (4.5% ABV)", "price": "4.00", "remaining_pct": "47.15909090909090909100"}]}'
    # fake_list = b'{"ales": [{"id": 223, "stocktype_id": 76, "manufacturer": "Dancing Duck", "name": "22", "abv": "4.3", "fullname": "Dancing Duck 22 (4.3% ABV)", "price": "4.00", "remaining_pct": "90.62500000000000000000"}, {"id": 123, "stocktype_id": 23, "manufacturer": "Milton", "name": "Justinian", "abv": "3.9", "fullname": "Milton Justinian (3.9% ABV)", "price": "4.00", "remaining_pct": "54.16666666666666666700"}, {"id": 129, "stocktype_id": 25, "manufacturer": "Milton", "name": "Nero", "abv": "5.0", "fullname": "Milton Nero (5.0% ABV)", "price": "4.40", "remaining_pct": "5.20833333333333333300"}, {"id": 225, "stocktype_id": 78, "manufacturer": "Uley", "name": "Taverner", "abv": "4.5", "fullname": "Uley Taverner (4.5% ABV)", "price": "4.20", "remaining_pct": "97.22222222222222222200"}], "kegs": [{"id": 175, "stocktype_id": 41, "manufacturer": "Cloudwater", "name": "Volley", "abv": "6.0", "fullname": "Cloudwater Volley (6.0% ABV)", "price": "7.00", "remaining_pct": "94.31818181818181818200"}, {"id": 11, "stocktype_id": 2, "manufacturer": "Dortmunder", "name": "Vier", "abv": "4.0", "fullname": "Dortmunder Vier (4.0% ABV)", "price": "4.00", "remaining_pct": "15.34090909090909090900"}, {"id": 158, "stocktype_id": 33, "manufacturer": "Five Points", "name": "Pale", "abv": "4.4", "fullname": "Five Points Pale (4.4% ABV)", "price": "4.50", "remaining_pct": "46.59090909090909090900"}, {"id": 165, "stocktype_id": 36, "manufacturer": "Lost & Grounded", "name": "Helles", "abv": "4.4", "fullname": "Lost & Grounded Helles (4.4% ABV)", "price": "4.50", "remaining_pct": "82.00757575757575757600"}, {"id": 138, "stocktype_id": 26, "manufacturer": "Milton", "name": "Dynamo", "abv": "3.9", "fullname": "Milton Dynamo (3.9% ABV)", "price": "4.50", "remaining_pct": "82.38636363636363636400"}], "ciders": [{"id": 240, "stocktype_id": 88, "manufacturer": "CJ\'s", "name": "Wench (Medium)", "abv": "5.5", "fullname": "CJ\'s Wench (Medium) (5.5% ABV)", "price": "4.20", "remaining_pct": "4.82954545454545454500"}, {"id": 239, "stocktype_id": 87, "manufacturer": "Hartland\'s", "name": "Medium Sweet", "abv": "6.0", "fullname": "Hartland\'s Medium Sweet (6.0% ABV)", "price": "4.40", "remaining_pct": "30.39772727272727272700"}, {"id": 245, "stocktype_id": 93, "manufacturer": "Ross on Wye", "name": "Foxton Mill (Blend, Dry)", "abv": "6.5", "fullname": "Ross on Wye Foxton Mill (Blend, Dry) (6.5% ABV)", "price": "4.50", "remaining_pct": "3.40909090909090909100"}, {"id": 5, "stocktype_id": 1, "manufacturer": "Westons", "name": "Stowford Press", "abv": "4.5", "fullname": "Westons Stowford Press (4.5% ABV)", "price": "4.00", "remaining_pct": "61.36363636363636363600"}]}'
    ontap = {}
    types = []
    type_idx = 0

    def log(self, msg):
        self.window.println(msg)
        print(msg)

    def on_activate(self):
        super().on_activate()
        self.rotate()

        self.window.println("attempting wifi connection...")
        self.window.println()
        self.window.println("if this fails, try moving")
        self.window.println("closer to a dataklo.")
        self.window.println()

        wifi_attempts = 0
        while not wifi.status():
            wifi.stop()
            wifi_attempts += 1
            self.window.println("attempt {}".format(wifi_attempts))
            wifi.connect(ssid="emfcamp-insecure22")
            wifi.wait()

        if wifi.status():
            self.window.println("got wifi! loading beers...")
            ontap_json = urequests.get("https://bar.emf.camp/api/on-tap.json")
            self.ontap = ujson.loads(ontap_json.content)
            self.window.println("loaded!")
            wifi.disconnect()

        # self.ontap = ujson.loads(self.fake_list)

        for type in self.ontap:
            self.types.append(type)
            # also sort by availability while at it
            self.ontap[type].sort(reverse=True, key=get_remaining)
    
        self.help() # tee hee
    
    def on_start(self):
        super().on_start()
        # couldn't get the left/right buttons to work without assigning the rest too
        self.buttons.on_press(BUTTON_A, lambda: print("a button be a-workin'"))
        self.buttons.on_press(JOY_CENTRE, lambda: print("joy button be a-workin'"))
        self.buttons.on_press(JOY_LEFT, self.prev)
        self.buttons.on_press(JOY_RIGHT, self.next)
        self.buttons.on_press(JOY_UP, lambda: print("up button be a-workin'"))
        self.buttons.on_press(JOY_DOWN, lambda: print("down button be a-workin'"))
    
    def next(self):
        self.type_idx = self.type_idx + 1 if self.type_idx < len(self.types) -1 else 0
        print(f"idx: {self.type_idx}")
        self.show_beers(self.types[self.type_idx])
    
    def prev(self):
        self.type_idx = self.type_idx - 1 if self.type_idx > 0 else len(self.types) - 1
        print(f"idx: {self.type_idx}")
        self.show_beers(self.types[self.type_idx])
    
    def help(self):
        self.window.redraw()    
        x = 2
        y = 13
        self.window.display.text(font, "drinks currently on tap", x, y, WHITE, BLACK)
        y += font.HEIGHT+1
        self.window.display.text(font, "", x, y, WHITE, BLACK)
        y += font.HEIGHT+1
        self.window.display.text(font, "!", x, y, RED, BLACK)
        self.window.display.text(font, "means less than 20% left", x + font.WIDTH*2, y, WHITE, BLACK)
        y += (font.HEIGHT+1)*2
        self.window.display.text(font, "press left/right to browse", x, y, WHITE, BLACK)

    def show_beers(self, type):
        self.window.set_title(type)
        self.window.redraw()
        x = 2
        y = 13

        for item in self.ontap[type]:
            if float(item["remaining_pct"]) < 20.0:
                self.window.display.text(font, "!", x, y, RED, BLACK)
                x = 2 + font.WIDTH*2

            self.window.display.text(font, item["fullname"], x, y, WHITE, BLACK)
            y += font.HEIGHT+1
            x = 2

main = Beer
