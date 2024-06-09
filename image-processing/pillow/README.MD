
Processamento de Cores: Separação de Canais R, G e B

Funcionalidade:

Este filtro separa uma imagem colorida em três canais de cores: vermelho (R), verde (G) e azul (B), resultando em três imagens individuais, uma para cada canal de cor.

Implementação:

    Abre a imagem colorida utilizando a função Image.open() da biblioteca PIL.
    Foi utilizada a função split() para separar os canais de cores da imagem em três imagens individuais: uma para o canal vermelho, outra para o canal verde e outra para o canal azul.
    Exibe cada imagem separada utilizando o método show().

Conversão de Colorido RGB para Tons de Cinza

Funcionalidade:

Este filtro converte uma imagem colorida em uma imagem em tons de cinza, onde cada pixel é representado por um único valor de intensidade luminosa.

Implementação:

    Abre a imagem colorida utilizando a função Image.open() da biblioteca PIL.
    Foi utilizado o método convert() para converter a imagem para o modo de escala de cinza ('L').
    Exibe a nova imagem em tons de cinza utilizando o método show().

Conversão de Tons de Cinza para Preto e Branco (Limiarização/Binarização Manual)

Funcionalidade:

Este filtro converte uma imagem em tons de cinza para uma imagem binária (preto e branco) aplicando um limiar manualmente definido.

Implementação:

    Abre a imagem em tons de cinza utilizando a função Image.open() da biblioteca PIL.
    Itera sobre cada pixel na imagem em tons de cinza.
    Para cada pixel, compara seu valor de intensidade com um limiar predefinido.
    Se o valor do pixel for maior ou igual ao limiar, atribuí o valor 255 (branco) ao pixel na nova imagem binária; caso contrário, atribuí o valor 0 (preto).
    Exibe a nova imagem binária utilizando o método show().

Filtros da Média

Funcionalidade:

Estes filtros suavizam uma imagem aplicando uma média dos valores de intensidade de cada pixel e seus vizinhos, resultando em uma imagem mais suave.

Implementação:

    Abre a imagem utilizando a função Image.open() da biblioteca PIL.
    Itera sobre cada pixel na imagem.
    Para cada pixel, calculamos a média dos valores de intensidade dos pixels em uma janela ao redor do pixel atual.
    Atribuí o valor médio ao pixel na nova imagem.
    Exibe a nova imagem utilizando o método show().

Filtro da Mediana

Funcionalidade:

Este filtro suaviza uma imagem substituindo cada pixel pelo valor mediano dos pixels em uma janela ao redor dele, resultando em uma imagem com redução de ruído.

Implementação:

    Abre a imagem utilizando a função Image.open() da biblioteca PIL.
    Itera sobre cada pixel na imagem.
    Para cada pixel, calculamos o valor mediano dos pixels em uma janela ao redor do pixel atual.
    Atribuí o valor mediano ao pixel na nova imagem.
    Exibe a nova imagem utilizando o método show().

Girar a Imagem 90 Graus

Funcionalidade:

Este filtro gira uma imagem em 90 graus no sentido horário ou anti-horário.

Implementação:

    Abre a imagem utilizando a função Image.open() da biblioteca PIL.
    Utiliza o método rotate() para girar a imagem em 90 graus, especificando a direção (horário ou anti-horário).
    Exibe a nova imagem girada utilizando o método show().

Inverter a Imagem (Horizontal/Vertical)

Funcionalidade:

Este filtro inverte uma imagem horizontal ou verticalmente, produzindo uma imagem espelhada.

Implementação:

    Abre a imagem utilizando a função Image.open() da biblioteca PIL.
    Utiliza o método transpose() com os argumentos Image.FLIP_LEFT_RIGHT para inversão horizontal ou Image.FLIP_TOP_BOTTOM para inversão vertical.
    Exibe a nova imagem invertida utilizando o método show().
