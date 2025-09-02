from turtle import *
from colorsys import *
import colorsys

# ---------- Pattern Functions ----------

def spectrum_bloom():
    speed(0); bgcolor("black"); h=0
    for i in range(72):
        color(hsv_to_rgb(h,1,1))
        circle(100)
        left(5); h+=0.01
    done()

def rainbow_galaxy():
    speed(0); bgcolor("black"); h=0
    for i in range(360):
        color(hsv_to_rgb(h,1,1))
        h+=0.005; circle(i,60); left(10)
    done()

def prism_circle():
    speed(0); bgcolor("black"); h=0
    for i in range(36):
        color(hsv_to_rgb(h,1,1))
        circle(150); left(10); h+=0.03
    done()

def neon_spiral():
    speed(0); bgcolor("black"); h=0
    for i in range(200):
        color(hsv_to_rgb(h,1,1))
        forward(i); left(59); h+=0.01
    done()

def aurora_wheel():
    speed(0); bgcolor("black"); h=0
    for i in range(90):
        color(hsv_to_rgb(h,1,1))
        circle(120,180); left(40); h+=0.02
    done()

def chromatic_lotus():
    speed(0); bgcolor("black"); h=0
    for i in range(36):
        color(hsv_to_rgb(h,1,1))
        circle(100,60); left(120); circle(100,60); left(10); h+=0.03
    done()

def solar_spectrum():
    speed(0); bgcolor("black"); h=0
    for i in range(180):
        color(hsv_to_rgb(h,1,1))
        forward(200); backward(200); left(2); h+=0.01
    done()

def infinity_colors():
    speed(0); bgcolor("black"); h=0
    for i in range(250):
        color(hsv_to_rgb(h,1,1))
        circle(i,91); h+=0.005
    done()

def radiant_halo():
    speed(0); bgcolor("black"); h=0
    for i in range(120):
        color(hsv_to_rgb(h,1,1))
        circle(80); left(15); h+=0.02
    done()

def cosmic_prism():
    speed(0); bgcolor("black"); h=0
    for i in range(72):
        color(hsv_to_rgb(h,1,1))
        forward(150); left(170); h+=0.02
    done()

# ----- Galaxy/Space -----
def galaxy_spiral(): neon_spiral()
def starburst_mandala():
    speed(0); bgcolor("black"); h=0
    for i in range(72):
        color(hsv_to_rgb(h,1,1))
        forward(200); backward(200); left(5); h+=0.01
    done()

def cosmic_bloom(): chromatic_lotus()
def orbital_flower(): aurora_wheel()
def nebula_circle(): prism_circle()
def astro_wheel(): spectrum_bloom()
def supernova_petals(): chromatic_lotus()
def celestial_spin(): radiant_halo()
def blackhole_radiance(): infinity_colors()
def starlight_swirl(): rainbow_galaxy()

# ----- Nature/Flowers -----
def lotus_spiral(): chromatic_lotus()
def infinity_flower(): chromatic_lotus()
def mystic_rose(): chromatic_lotus()
def blooming_star(): starburst_mandala()
def floral_cosmos(): chromatic_lotus()
def crystal_bloom(): chromatic_lotus()
def sunflower_radiance(): aurora_wheel()
def petal_wheel(): chromatic_lotus()
def natures_mandala(): spectrum_bloom()
def eternal_bloom(): chromatic_lotus()

# ----- Abstract -----
def kaleido_spiral(): neon_spiral()
def infinity_mandala(): spectrum_bloom()
def mystic_wheel(): radiant_halo()
def radiance_flow(): aurora_wheel()
def dream_spiral(): neon_spiral()
def hypnotic_bloom(): rainbow_galaxy()
def fractal_lotus():
    speed(0); bgcolor("black"); h=0
    def draw_flower(radius, depth, h):
        if depth==0: return
        color(hsv_to_rgb(h,1,1)); circle(radius)
        for i in range(6):
            penup(); forward(radius); pendown()
            draw_flower(radius/2, depth-1, h+0.1)
            penup(); backward(radius); pendown(); left(60)
    draw_flower(100,3,h); done()

def zen_mandala(): spectrum_bloom()
def aurora_bloom(): aurora_wheel()
def sacred_geometry(): prism_circle()

# ----- Modern/Tech -----
def cyber_spiral(): neon_spiral()
def neon_matrix(): rainbow_galaxy()
def digital_lotus(): chromatic_lotus()
def tech_bloom(): aurora_wheel()
def quantum_wheel(): radiant_halo()
def ai_mandala(): spectrum_bloom()
def virtual_spiral(): neon_spiral()
def hologram_bloom(): chromatic_lotus()
def spectrum_code(): rainbow_galaxy()
def infinity_grid(): prism_circle()

# ---------- Dictionary ----------
patterns = {
    "Spectrum Bloom": spectrum_bloom,
    "Rainbow Galaxy": rainbow_galaxy,
    "Prism Circle": prism_circle,
    "Neon Spiral": neon_spiral,
    "Aurora Wheel": aurora_wheel,
    "Chromatic Lotus": chromatic_lotus,
    "Solar Spectrum": solar_spectrum,
    "Infinity Colors": infinity_colors,
    "Radiant Halo": radiant_halo,
    "Cosmic Prism": cosmic_prism,
    "Galaxy Spiral": galaxy_spiral,
    "Starburst Mandala": starburst_mandala,
    "Cosmic Bloom": cosmic_bloom,
    "Orbital Flower": orbital_flower,
    "Nebula Circle": nebula_circle,
    "Astro Wheel": astro_wheel,
    "Supernova Petals": supernova_petals,
    "Celestial Spin": celestial_spin,
    "Blackhole Radiance": blackhole_radiance,
    "Starlight Swirl": starlight_swirl,
    "Lotus Spiral": lotus_spiral,
    "Infinity Flower": infinity_flower,
    "Mystic Rose": mystic_rose,
    "Blooming Star": blooming_star,
    "Floral Cosmos": floral_cosmos,
    "Crystal Bloom": crystal_bloom,
    "Sunflower Radiance": sunflower_radiance,
    "Petal Wheel": petal_wheel,
    "Nature’s Mandala": natures_mandala,
    "Eternal Bloom": eternal_bloom,
    "Kaleido Spiral": kaleido_spiral,
    "Infinity Mandala": infinity_mandala,
    "Mystic Wheel": mystic_wheel,
    "Radiance Flow": radiance_flow,
    "Dream Spiral": dream_spiral,
    "Hypnotic Bloom": hypnotic_bloom,
    "Fractal Lotus": fractal_lotus,
    "Zen Mandala": zen_mandala,
    "Aurora Bloom": aurora_bloom,
    "Sacred Geometry": sacred_geometry,
    "Cyber Spiral": cyber_spiral,
    "Neon Matrix": neon_matrix,
    "Digital Lotus": digital_lotus,
    "Tech Bloom": tech_bloom,
    "Quantum Wheel": quantum_wheel,
    "AI Mandala": ai_mandala,
    "Virtual Spiral": virtual_spiral,
    "Hologram Bloom": hologram_bloom,
    "Spectrum Code": spectrum_code,
    "Infinity Grid": infinity_grid
}

# ---------- Main ----------
if __name__ == "__main__":
    print("Available Patterns (50):")
    for name in patterns.keys():
        print("-", name)

    choice = input("\nEnter the pattern name you want to see: ")

    if choice in patterns:
        patterns[choice]()
    else:
        print("❌ Pattern not found. Please choose from the list above.")
