from PIL import Image

def binarize_image(image_path, save_path, threshold=165):
    # Carregando a imagem em tons de cinza
    gray_img = Image.open(image_path).convert("L")

    # Obtendo as dimensões da imagem
    width, height = gray_img.size

    # Criando uma nova imagem binarizada
    bin_img = Image.new('1', (width, height))

    # Aplicando a conversão para a nova imagem binarizada
    for x in range(width):
        for y in range(height):
            # Obtendo o valor de cinza do pixel atual
            gray_value = gray_img.getpixel((x, y))
            
            # Atribuindo o novo valor binário ao novo pixel
            bin_value = 1 if gray_value >= threshold else 0
            bin_img.putpixel((x, y), bin_value)

    # Salvando a nova imagem binarizada
    bin_img.save(save_path)
    return bin_img

if __name__ == "__main__":
    image_path = "images/girafa_gray_hardway.jpg"
    save_path = "images/imagem_binaria.jpg"
    bin_img = binarize_image(image_path, save_path)
    bin_img.show()

