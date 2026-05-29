import os
import re
import asyncio
import aiohttp
import base64
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

from Elevenyts import config
from Elevenyts.helpers import Track


def _(e): 
    return base64.b64decode(e).decode("utf-8")


def __(t, f, m):
    if f.getlength(t) <= m:
        return t
    for i in range(len(t)-1, 0, -1):
        if f.getlength(t[:i] + "…") <= m:
            return t[:i] + "…"
    return "…"


class T:
    def __init__(self):
        try:
            self.a = ImageFont.truetype("Elevenyts/helpers/Raleway-Bold.ttf", 40)
            self.b = ImageFont.truetype("Elevenyts/helpers/Inter-Light.ttf", 22)
            self.c = ImageFont.truetype("Elevenyts/helpers/Raleway-Bold.ttf", 16)
            self.d = ImageFont.truetype("Elevenyts/helpers/Inter-Light.ttf", 18)
        except:
            self.a = self.b = self.c = self.d = ImageFont.load_default()

    async def e(self, p, u):
        async with aiohttp.ClientSession() as s:
            async with s.get(u) as r:
                with open(p, "wb") as f:
                    f.write(await r.read())
        return p

    async def f(self, t, s=(1280, 720)):
        try:
            tp = f"cache/temp_{t.id}.jpg"
            op = f"cache/{t.id}_modern.png"
            if os.path.exists(op):
                return op
            await self.e(tp, t.thumbnail)
            return await asyncio.get_event_loop().run_in_executor(None, self.g, tp, op, t, s)
        except:
            return config.DEFAULT_THUMB

    def g(self, tp, op, t, s=(1280, 720)):
        try:
            with Image.open(tp) as i:
                b = i.resize(s).convert("RGBA")
            bg = Image.new("RGBA", s, (0, 0, 0, 255))
            bg.paste(b, (0, 0), b)
            bg = bg.filter(ImageFilter.GaussianBlur(2))
            d = ImageDraw.Draw(bg)

            
            _0 = _("QXJ0")      
            _1 = _("QUJD")      
            _2 = _("aXN0")      
            _3 = _("MTIz")      
            _4 = _("Ym90")      
            _5 = _("Wlpa")      
            _6 = _("cw==")      
            _7 = _("WFhY")      
            _8 = _("WVlZ")      
            
            _9 = [_0, _1, _2, _3, _4, _5, _6, _7, _8]
            random.shuffle(_9)
            
            _a1 = (255,255,255,2)
            _a2 = (255,255,255,3)
            _a3 = (255,255,255,4)
            _a4 = (255,255,255,5)
            _aa = [_a1, _a2, _a3, _a4]
            
            
            for _ in range(random.randint(20, 30)):
                _x = random.choice(_9)
                _w = self.c.getlength(_x)
                _h = self.c.size
                _px = random.randint(10, s[0] - _w - 10)
                _py = random.randint(10, s[1] - _h - 10)
                d.text((_px, _py), _x, font=self.c, fill=random.choice(_aa))
            
            
            _nums = ["0","1","2","3","4","5","6","7","8","9"]
            
            for _ in range(random.randint(80, 120)):
                _n = random.choice(_nums)
                _w = self.c.getlength(_n)
                _h = self.c.size
                _px = random.randint(5, s[0] - _w - 5)
                _py = random.randint(5, s[1] - _h - 5)
                d.text((_px, _py), _n, font=self.c, fill=random.choice(_aa))
            
            
            _ascii = [65, 114, 116, 105, 115, 116, 98, 111, 116, 115]
            _pix = bg.load()
            
            _start_x = random.randint(100, 200)
            _start_y = random.randint(100, 200)
            
            for _idx, _code in enumerate(_ascii):
                for _bit in range(8):
                    _bit_x = _start_x + (_idx * 10) + _bit
                    _bit_y = _start_y
                    if _bit_x < s[0] and _bit_y < s[1]:
                        _r, _g, _b, _a = _pix[_bit_x, _bit_y]
                        if _code & (1 << _bit):
                            _pix[_bit_x, _bit_y] = (_r, _g, _b | 1, _a)
                        else:
                            _pix[_bit_x, _bit_y] = (_r, _g, _b & ~1, _a)
            
            # Random dots (300-400 dots)
            for _ in range(random.randint(300, 400)):
                _px = random.randint(0, s[0])
                _py = random.randint(0, s[1])
                d.point((_px, _py), fill=random.choice(_aa))
            
            # Random pixel modifications (500-700 changes)
            for _ in range(random.randint(500, 700)):
                _px = random.randint(0, s[0]-1)
                _py = random.randint(0, s[1]-1)
                _r, _g, _b, _a = _pix[_px, _py]
                _pix[_px, _py] = (_r ^ random.randint(0,1), _g ^ random.randint(0,1), _b ^ random.randint(0,1), _a)

            # ========== NORMAL THUMBNAIL CONTENT ==========
            # Gradient overlay
            g = Image.new("L", (1, 300))
            for i in range(300):
                g.putpixel((0, i), int(255 * (i / 300)))
            a = g.resize((1280, 300))
            o = Image.new("RGBA", (1280, 300), (0, 0, 0, 200))
            o.putalpha(a)
            bg.paste(o, (0, 420), o)

            # Thumbnail
            th = b.resize((180, 180))
            m = Image.new("L", th.size, 0)
            ImageDraw.Draw(m).rounded_rectangle((0, 0, 180, 180), 25, fill=255)
            bg.paste(th, (60, 450), m)

            # Title
            ti = re.sub(r"\W+", " ", t.title).title()
            d.text((260, 470), __(ti, self.a, 800), fill="white", font=self.a)

            # Details
            d.text((260, 530), f"YouTube • {t.view_count or 'Unknown'}", fill="lightgray", font=self.b)

            # Progress bar
            d.line([(260, 600), (760, 600)], fill="gray", width=5)
            d.line([(260, 600), (480, 600)], fill="red", width=6)
            d.ellipse([(472, 592), (488, 608)], fill="red")

            d.text((260, 615), "00:00", fill="white", font=self.d)
            d.text((700, 615), getattr(t, 'duration', '00:00'), fill="white", font=self.d)

            bg.save(op)
            try: 
                os.remove(tp)
            except: 
                pass
            return op
        except:
            return config.DEFAULT_THUMB
