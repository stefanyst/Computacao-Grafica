from PIL import Image

def rotate_image(image_path, save_path, degrees):
    # Abre a imagem original
    img = Image.open(image_path)

    # Rotaciona a imagem
    rotated_img = img.rotate(degrees, expand=True)

    # Salva a nova imagem rotacionada
    rotated_img.save(save_path)
    return rotated_img

if __name__ == "__main__":
    image_path = "images/girafa.jpg"
    save_path = "images/girafa_rotated_90.jpg"
    
    # Rotaciona a imagem em 90 graus
    rotated_img = rotate_image(image_path, save_path, 90)
    
    # Exibe a imagem rotacionada
    rotated_img.show()

