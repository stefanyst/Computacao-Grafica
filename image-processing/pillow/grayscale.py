from PIL import Image

def convert_to_grayscale(image_path, save_path):
    # Abre a imagem colorida
    img = Image.open(image_path)

    # Cria uma nova imagem em escala de cinza
    gray_img = Image.new('L', img.size)

    # Itera por cada pixel na imagem original e calcula a conversão em escala de cinza
    for x in range(img.width):
        for y in range(img.height):
            # Obtem o valor do pixel em RGB
            r, g, b = img.getpixel((x, y))

            # Calcula o valor de escala de cinza usando a proporção NTSC
            gray_value = int(0.299 * r + 0.587 * g + 0.114 * b)

            # Define o novo pixel na imagem em escala de cinza
            gray_img.putpixel((x, y), gray_value)

    # Salva a nova imagem em escala de cinza
    gray_img.save(save_path)
    return gray_img

if __name__ == "__main__":
    image_path = "images/girafa.jpg"
    save_path = "images/girafa_gray_hardway.jpg"
    gray_img = convert_to_grayscale(image_path, save_path)
    gray_img.show()


