import cv2

# Pedir o caminho da imagem ao utilizador
caminho_imagem = input("Arrasta ou escreve o caminho da foto de referencia: ").strip()

# Remover aspas caso o caminho tenha sido colado com elas
caminho_imagem = caminho_imagem.strip('"').strip("'")

# Ler a imagem com o OpenCV
imagem = cv2.imread(caminho_imagem)

if imagem is None:
    print("Ficheiro nao encontrado ou formato invalido. Verifica o caminho e tenta novamente.")
    exit()

# Converter a imagem de BGR para HSV (essencial para extrair Matiz/Calor e Saturação)
hsv_imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

def amostrar_cor(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Dispara com um clique esquerdo do rato
        # Obter valores BGR
        b, g, r = imagem[y, x]
        
        # Obter valores HSV
        # No OpenCV, o Hue (H) varia de 0 a 180, Saturation (S) e Value (V) de 0 a 255
        h, s, v = hsv_imagem[y, x]
        
        print(f"\n--- Ponto Selecionado: X={x}, Y={y} ---")
        print(f"RGB  -> R: {r}, G: {g}, B: {b}")
        print(f"HSV  -> Matiz (Tom/Calor): {h} | Saturação: {s} | Brilho: {v}")

# Criar a janela e associar o evento do rato
nome_janela = "VisionHue - Color Picker"
cv2.namedWindow(nome_janela)
cv2.setMouseCallback(nome_janela, amostrar_cor)

print("\nJanela aberta! Clica em qualquer ponto da imagem para ver os valores. Pressa a tecla 'q' para sair.")

while True:
    cv2.imshow(nome_janela, imagem)
    
    # Pressionar 'q' para fechar a janela
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()