# 🎨 VisionHue

**VisionHue** é uma ferramenta inteligente de amostragem e correspondência de cores (*color-matching*) para fotografia, impulsionada por Visão por Computador e Inteligência Artificial.

---

## 🎯 O Problema e a Visão

Na edição e pós-produção fotográfica, manter a consistência de cores entre várias fotografias de uma mesma sessão (onde a iluminação, ângulo ou pose variam) exige muito trabalho manual. 

O **VisionHue** resolve este problema combinando um sistema clássico de conta-gotas ("agulha" de cor) com modelos de segmentação por IA:
1. **Amostragem de Referência:** Numa fotografia base, o utilizador seleciona pontos específicos (ex.: tom de pele, camisola, jardineiras, céu). O sistema extrai os códigos de cor (HEX, RGB, LAB) e associa cada cor ao respetivo elemento visual.
2. **Reconhecimento Inteligente:** Em vez de depender apenas de coordenadas estáticas de píxeis, a IA identifica semanticamente cada objeto ou peça de vestuário.
3. **Extração e Sincronização em Lote:** Ao carregar novas fotografias da mesma modelo ou sessão, o VisionHue localiza automaticamente os mesmos elementos (mesmo que a pose mude) e extrai ou compara os códigos de cor correspondentes.

---

## 🚀 Funcionalidades Planeadas

- [ ] **Conta-gotas Interativo (MVP):** Seleção manual de pontos numa imagem para extração instantânea de valores RGB, HEX e LAB.
- [ ] **Gestão de Paletas por Objeto:** Etiquetar cada amostra de cor (ex.: `pele`, `camisola`, `fundo`).
- [ ] **Segmentação Assistida por IA:** Integração com modelos de visão por computador (como SAM / YOLO) para isolar automaticamente roupas e elementos.
- [ ] **Correspondência entre Fotografias:** Deteção automática dos mesmos elementos numa segunda fotografia e comparação de desvios cromáticos.
- [ ] **Interface Gráfica:** Painel visual intuitivo para comparar lado a lado a foto de referência e as fotos alvo.

---

## 🛠️ Stack Tecnológica

* **Linguagem:** Python 3.10+
* **Processamento de Imagem:** OpenCV, Pillow, NumPy
* **Inteligência Artificial / Segmentação:** PyTorch, Segment Anything Model (SAM) / Ultralytics YOLO
* **Interface (UI):** Streamlit ou PyQt

---

## 📦 Instalação e Configuração

1. Clona o repositório:
   ```bash
   git clone https://github.com/o-teu-utilizador/VisionHue.git
   cd VisionHue

2. Cria e ativa um ambiente virtual:
   ```` bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/macOS:
   source venv/bin/activate

3. Instala as dependências:
    ```` bash
    pip install -r requirements.txt
