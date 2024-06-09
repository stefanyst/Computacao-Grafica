from PIL import Image

def convert_to_grayscale(image_path, save_path):
    # Abre a imagem original
    img = Image.open(image_path)

    # Converte a imagem para escala de cinza
    gray_img = img.convert("L")

    # Cria uma nova imagem em escala de cinza
    median_img = Image.new('L', img.size)

    # Itera por cada pixel na imagem original e aplica o filtro de mediana
    for x in range(1, gray_img.width - 1):
        for y in range(1, gray_img.height - 1):
            # Lista para armazenar os valores dos pixels da janela 3x3
            pixels = [gray_img.getpixel((x + i, y + j)) for i in range(-1, 2) for j in range(-1, 2)]
            # Ordena os pixels e pega o valor mediano
            pixels.sort()
            median_value = pixels[4]
            # Define o novo pixel na imagem em escala de cinza
            median_img.putpixel((x, y), median_value)

    # Salva a nova imagem em escala de cinza
    median_img.save(save_path)
    return median_img

if __name__ == "__main__":
    image_path = "images/t-graum.png"
    save_path = "images/median-t-graum.jpg"
    median_img = convert_to_grayscale(image_path, save_path)
    median_img.show()


