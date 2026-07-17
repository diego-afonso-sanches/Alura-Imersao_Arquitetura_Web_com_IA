# Alura Album - Copa do Mundo Tech

O **Alura Album - Copa do Mundo Tech** é um álbum de figurinhas digital interativo desenvolvido como parte da Imersão Julho 2026 da Alura. O projeto é um tributo às mentes brilhantes que moldaram a computação, banco de dados, desenvolvimento de software e a educação tecnológica no Brasil e no mundo.

Utilizando efeitos visuais modernos, folheamento realista em 3D, geração de áudio procedural e integração com uma API backend para carregar as figurinhas dinamicamente, o projeto oferece uma experiência premium e nostálgica de colecionador.

---

## 🚀 Tecnologias Utilizadas

- **HTML5**: Estrutura semântica das páginas do álbum.
- **CSS3 (Vanilla)**: Design responsivo com efeitos de *glitch*, gradientes modernos, sombras realistas, micro-animações e estilização para o layout de páginas de livro.
- **JavaScript (ES6+)**: Lógica de navegação, integração com API, controle de áudio e manipulação do DOM.
- **St.PageFlip**: Biblioteca Javascript para simular o efeito de virar páginas físicas de forma realista.
- **Web Audio API**: Geração procedural e dinâmica de efeitos sonoros em tempo real (simulação do som de papel sendo folheado).

---

## 📂 Arquivos do Projeto (Frontend)

O frontend do projeto é composto por três arquivos principais:

### 1. `index.html`
Define a estrutura semântica e o conteúdo do álbum.
- **Controles de Interface**: Inclui um botão para alternar o som (mudo/ativado) e botões de seta flutuantes (`#btn-prev` e `#btn-next`) para virar as páginas.
- **Estrutura do Álbum**: Contém a div principal `.flip-book` que envolve todas as páginas do livro:
  - **Capa (Pág. 0)**: Possui efeito visual de *glitch* no título, colagens de silhuetas de figurinhas clássicas e um elemento central brilhante representando uma esfera tecnológica 3D.
  - **Páginas Temáticas (Págs. 1 a 6)**: Cada página contém uma categoria específica com slots de figurinhas numerados de `#01` a `#30`.
  - **Contracapa (Pág. 7)**: Possui a ficha técnica do álbum, um resumo da coleção e um código de barras estilizado via CSS.
- **Dependências**: Carrega a biblioteca externa `St.PageFlip` a partir de uma CDN e o script local `app.js`.

### 2. `style.css`
Gerencia todo o design visual do álbum, com ênfase em uma experiência rica e imersiva.
- **Layout de Livro**: Configura as páginas com dimensões fixas que se estendem dinamicamente na tela e adiciona gradientes que simulam a dobra física no centro do álbum (*page spine*).
- **Temas e Badges**: Estiliza os cartões e crachás de categoria com cores personalizadas de acordo com o tema tecnológico (IA, Python, Banco de Dados, Sistemas Operacionais e Brasil).
- **Efeitos Premium**:
  - Efeito *glitch* animado no título da capa.
  - Efeitos de luz (*glow*) em slots especiais e na esfera central da capa.
  - Sombras dinâmicas que aumentam o realismo 3D ao folhear.
- **Responsividade**: Ajusta o zoom e o posicionamento das páginas para diferentes tamanhos de tela.

### 3. `app.js`
Implementa toda a inteligência e o comportamento interativo da aplicação. Suas principais funcionalidades são:

*   **Configuração e Inicialização do PageFlip**:
    *   Configura e inicializa o componente `St.PageFlip` com parâmetros de dimensionamento flexíveis (*stretch*), sombras e tempo de transição otimizado para 800ms.
    *   Gerencia os estados de exibição dos botões de navegação, ocultando a seta de retorno na capa e a de avanço na contracapa.
*   **Controle Customizado de Arraste (Drag & Swipe)**:
    *   Desativa os cliques acidentais e gestos automáticos nas bordas da página.
    *   Implementa um sensor de arraste manual com limite (*threshold*) de 10px para evitar viradas acidentais de página ao clicar ou interagir com botões.
*   **Geração Procedural de Som (Web Audio API)**:
    *   Em vez de carregar arquivos pesados de áudio `.mp3`, o script sintetiza um som realista de folheamento de papel em tempo real utilizando ruído branco (*white noise*).
    *   Aplica uma curva de envelope de volume que atinge o pico em 30% do tempo e decai suavemente.
    *   Modula filtros do tipo `bandpass` (com varredura de frequência de 1500Hz a 350Hz para simular o movimento do papel no ar) e `lowpass` (para suavizar agudos metálicos digitais).
*   **Integração com a API Backend**:
    *   Realiza uma requisição assíncrona (`fetch`) para obter a lista de figurinhas salvas na API backend em `http://localhost:8000/figurinhas`.
    *   Mapeia dinamicamente os IDs das figurinhas retornadas e preenche os slots `.sticker-slot` correspondentes inserindo imagens e aplicando a classe de animação `.slot-preenchido`.

---

## 📖 Estrutura do Álbum e Categorias

As figurinhas estão divididas nas seguintes categorias temáticas:

1.  **Pioneiros da Inteligência Artificial (Pág. 1)**: Focada em nomes como Alan Turing, John McCarthy, Sam Altman, Geoffrey Hinton e Yann LeCun.
2.  **Arquitetos da Simplicidade - Python (Pág. 2)**: Guido van Rossum, Tim Peters, Raymond Hettinger, Travis Oliphant e Wes McKinney.
3.  **Arquitetos de Bancos de Dados (Pág. 3)**: Edgar F. Codd, Larry Ellison, Michael Widenius, Salvatore Sanfilippo e Eliot Horowitz.
4.  **Arquitetos da Computação Moderna - Sistemas Operacionais (Pág. 4)**: Linus Torvalds, Dennis Ritchie, Richard Stallman, Bill Gates e Steve Jobs.
5.  **Celebridades Tech no Brasil (Págs. 5 e 6)**: Educadores, criadores e personalidades do ecossistema brasileiro de desenvolvimento, como Paulo Silveira, Guilherme Silveira, Gustavo Guanabara, Maurício Aniche, Andre David, Guilherme Lima, Gi (Space Coding), Vinicius Neves e Rafaela Ballerini.
6.  **Slot do Colecionador (Figurinha #30)**: Um espaço reservado para você ("Você") colocar a sua própria foto e fazer parte do álbum!

---

## 🛠️ Como Executar o Projeto

1.  **Executar o Frontend**:
    *   Por se tratar de arquivos HTML, CSS e JS estáticos, você pode abrir o arquivo `index.html` diretamente no seu navegador, ou utilizar uma extensão como o *Live Server* do VS Code para rodar um servidor de desenvolvimento local.
2.  **Executar o Backend (API)**:
    *   Para que as fotos das figurinhas sejam carregadas corretamente nos slots correspondentes, certifique-se de que a API do backend está em execução.
    *   Para iniciar o servidor FastAPI, execute no terminal:
        ```bash
        cd backend/dia-3
        uvicorn main:app --reload
        ```
    *   A API backend servirá as informações das figurinhas na porta `8000` (`http://localhost:8000`), permitindo que o frontend preencha os slots dinamicamente.
