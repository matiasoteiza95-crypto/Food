"""Draws the Cauldron app icon (a jack-o'-lantern on a night sky) into docs/."""
from PIL import Image, ImageDraw

def icon(size):
    s = 4  # supersample
    W = size * s
    im = Image.new("RGB", (W, W), (20, 15, 28))
    d = ImageDraw.Draw(im)
    u = W / 100
    # glow
    for r, c in [(46, (44, 28, 40)), (40, (60, 34, 40))]:
        d.ellipse([50*u - r*u, 54*u - r*u, 50*u + r*u, 54*u + r*u], fill=c)
    # pumpkin lobes
    orange, deep = (255, 138, 42), (226, 104, 20)
    for x0, x1, col in [(14, 52, deep), (48, 86, deep), (24, 76, orange)]:
        d.ellipse([x0*u, 30*u, x1*u, 82*u], fill=col)
    d.ellipse([30*u, 31*u, 70*u, 81*u], fill=orange)
    # stem
    d.rounded_rectangle([46*u, 18*u, 54*u, 34*u], radius=3*u, fill=(127, 209, 139))
    # face
    face = (29, 15, 4)
    d.polygon([(32*u, 52*u), (42*u, 52*u), (37*u, 43*u)], fill=face)
    d.polygon([(58*u, 52*u), (68*u, 52*u), (63*u, 43*u)], fill=face)
    d.polygon([(30*u, 60*u), (70*u, 60*u), (64*u, 70*u), (57*u, 66*u), (50*u, 72*u), (43*u, 66*u), (36*u, 70*u)], fill=face)
    return im.resize((size, size), Image.LANCZOS)

for n in (180, 192, 512):
    icon(n).save(f"docs/icon-{n}.png", optimize=True)
