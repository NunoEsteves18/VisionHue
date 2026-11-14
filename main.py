import cv2
import json
import os

amostras = []
imagem_display = None
imagem_original = None

def rgb_para_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b).upper()

def clique_rato(event, x, y, flags, param):
    global imagem_display, amostras

    if event == cv2.EVENT_LBUTTONDOWN:
        # O OpenCV lê as cores em BGR por defeito
        b, g, r = imagem_original[y, x]
        r, g, b = int(r), int(g), int(b)
        hex_cor = rgb_para_hex(r, g, b)

        print(f"\nPonto selecionado em (X={x}, Y={y})")
        print(f"Cor detetada -> RGB: ({r}, {g}, {b}) | HEX: {hex_cor}")

        etiqueta = input("Nome deste elemento (ex: pele, camisola, jardineiras, ceu): ").strip()
        if not etiqueta:
            etiqueta = f"elemento_{len(amostras) + 1}"

        amostra = {
            "elemento": etiqueta,
            "coordenadas": {"x": x, "y": y},
            "rgb": [r, g, b],
            "hex": hex_cor
        }
        amostras.append(amostra)

        # Desenhar marcador na imagem
        cv2.circle(imagem_display, (x, y), 6, (0, 255, 0), -1)
        cv2.circle(imagem_display, (x, y), 8, (0, 0, 0), 2)
        cv2.putText(
            imagem_display,
            f"{etiqueta} ({hex_cor})",
            (x + 12, y + 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            2
        )
        cv2.imshow("VisionHue - Amostragem de Referencia", imagem_display)

def main():
    global imagem_display, imagem_original

    caminho_imagem = input("Arrasta ou escreve o caminho da foto de referencia: ").strip().strip('"').strip("'")

    if not os.path.exists(caminho_imagem):
        print("Ficheiro nao encontrado. Verifica o caminho e tenta novamente.")
        return

    imagem_original = cv2.imread(caminho_imagem)
    if imagem_original is None:
        print("Nao foi possivel abrir a imagem.")
        return

    # Redimensionar apenas se a imagem for demasiado grande para o ecra
    altura, largura = imagem_original.shape[:2]
    max_dim = 1000
    if max(altura, largura) > max_dim:
        escala = max_dim / max(altura, largura)
        imagem_original = cv2.resize(imagem_original, (int(largura * escala), int(altura * escala)))

    imagem_display = imagem_original.copy()

    print("\nImagem carregada!")
    print("Clica com o botao esquerdo do rato nos elementos para extrair a cor.")
    print("Pressiona 'S' na janela da imagem para guardar e sair, ou 'ESC' para sair sem guardar.\n")

    cv2.imshow("VisionHue - Amostragem de Referencia", imagem_display)
    cv2.setMouseCallback("VisionHue - Amostragem de Referencia", clique_rato)

    while True:
        tecla = cv2.waitKey(1) & 0xFF
        if tecla == ord('s') or tecla == ord('S'):
            with open("paleta_referencia.json", "w", encoding="utf-8") as f:
                json.dump(amostras, f, indent=4, ensure_ascii=False)
            print(f"\nPaleta guardada com sucesso em 'paleta_referencia.json' ({len(amostras)} elementos)!")
            break
        elif tecla == 27:  # Tecla ESC
            print("\nA sair sem guardar.")
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()