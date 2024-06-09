from PIL import Image

def flip_image(image_path, save_path, mode):
    """
    Inverte a imagem horizontal ou verticalmente.

    Args:
        image_path (str): O caminho da imagem original.
        save_path (str): O caminho onde a imagem invertida será salva.
        mode (str): O modo de inversão ('horizontal' ou 'vertical').
    """
    # Abre a imagem original
    img = Image.open(image_path)

    # Inverte a imagem de acordo com o modo especificado
    if mode == 'horizontal':
        flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif mode == 'vertical':
        flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        raise ValueError("O modo deve ser 'horizontal' ou 'vertical'.")

    # Salva a nova imagem invertida
    flipped_img.save(save_path)
    return flipped_img

if __name__ == "__main__":
    # Caminho da imagem original
    image_path = "images/girafa.jpg"
    
    # Caminho onde a imagem invertida será salva
    save_path_horizontal = "images/girafa_inverted_horizontal.jpg"
    save_path_vertical = "images/girafa_inverted_vertical.jpg"

    # Inverter a imagem horizontalmente
    flipped_horizontal = flip_image(image_path, save_path_horizontal, 'horizontal')
    flipped_horizontal.show()

    # Inverter a imagem verticalmente
    flipped_vertical = flip_image(image_path, save_path_vertical, 'vertical')
    flipped_vertical.show()

