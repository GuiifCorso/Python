import colorgram

colors = colorgram.extract("pic.jpg", 30)
color_list = []

for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    new_color = (red, green, blue)
    color_list.append(new_color)

color_list.pop(0)