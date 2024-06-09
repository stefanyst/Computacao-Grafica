from PIL import Image

def apply_mean_filter(image_path, save_path):
    # Abre a imagem original
    img = Image.open(image_path)

    # Converte a imagem para escala de cinza
    gray_img = img.convert("L")

    # Cria uma nova imagem para armazenar o resultado
    mean_img = Image.new('L', img.size)

    # Itera por cada pixel na imagem original, exceto as bordas
    for x in range(1, gray_img.width - 1):
        for y in range(1, gray_img.height - 1):
            # Calcula a média dos valores dos pixels na janela 3x3
            mean_value = sum(gray_img.getpixel((x + i, y + j)) for i in range(-1, 2) for j in range(-1, 2)) // 9

            # Define o novo pixel na imagem de saída
            mean_img.putpixel((x, y), mean_value)

    # Salva a nova imagem processada
    mean_img.save(save_path)
    return mean_img

if __name__ == "__main__":
    image_path = "images/t-graum.png"
    save_path = "images/mean-t-graum.jpg"
    mean_img = apply_mean_filter(image_path, save_path)
    mean_img.show()


