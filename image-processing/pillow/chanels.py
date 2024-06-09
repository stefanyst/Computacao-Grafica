from PIL import Image

def extract_rgb_channels(image_path):
    # Carrega a imagem original
    img = Image.open(image_path)

    # Obtém as dimensões da imagem
    width, height = img.size

    # Cria novas imagens para cada canal de cor
    img_r = Image.new("RGB", (width, height))
    img_g = Image.new("RGB", (width, height))
    img_b = Image.new("RGB", (width, height))

    # Itera sobre cada pixel da imagem original
    for x in range(width):
        for y in range(height):
            # Obtém os valores dos canais RGB do pixel atual
            r, g, b = img.getpixel((x, y))

            # Define os pixels nas novas imagens para cada canal
            img_r.putpixel((x, y), (r, r, r))
            img_g.putpixel((x, y), (g, g, g))
            img_b.putpixel((x, y), (b, b, b))

    return img_r, img_g, img_b

if __name__ == "__main__":
    image_path = "images/girafa.jpg"
    
    # Extrai os canais RGB
    img_r, img_g, img_b = extract_rgb_channels(image_path)

    # Exibe a imagem do canal Red
    img_r.show()
    # Exibe a imagem do canal Green
    img_g.show()
    # Exibe a imagem do canal Blue
    img_b.show()


