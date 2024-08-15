<h1>SpellBoar</h1>
O projeto SpellBoar, foi um projeto que desenvolvi em grupo na faculdade com objetivo aprimorar a experiência de jogar Magic: The Gathering (MTG) online utilizando cartas físicas.

<h2>Magic: The Gathering (MTG)</h2>
<br></br>
<div align="center">
Magic é um jogo de cartas de estratégia baseado em turnos.
<img src="https://github.com/user-attachments/assets/a480e6ec-28d7-437c-8560-ef33e76757ea"></div>
<br></br>
<h2>Magic em 2020</h2>
Devido à pandemia, a experiência de jogar Magic: The Gathering se tornou um desafio significativo. Em resposta a essa situação, foi criado o <b>SpellTable</b>, uma plataforma que permite que os jogadores continuem desfrutando do jogo com cartas físicas, mas de forma totalmente online. Usando as câmeras posicionadas sobre seus tabuleiros, os jogadores podem se conectar e competir virtualmente, mantendo a essência do jogo físico mesmo à distância.
<br></br>


<img src="https://github.com/user-attachments/assets/4a1edfa7-d9f9-4909-991b-f0c405c33857">

<h2>⚠️ Problemas no SpellTable</h2>
O SpellTable, apesar de oferecer uma solução prática, sofre de um bug crítico que afeta a leitura das cartas em jogo.<br>
O sistema muitas vezes falha em identificar corretamente as cartas na mesa. Essa limitação não só compromete a experiência de jogo, mas também pode levar a jogadas incorretas, prejudicando a competitividade e a diversão dos jogadores.
<br></br>
<h1>Surge o SpellBoar</h1>
Diante dessas dificuldades, eu e meus colegas de grupo decidimos desenvolver o "SpellBoar", um novo programa projetado para aprimorar a experiência de jogar Magic online.
O objetivo principal do SpellBoar é replicar e superar a função de identificação de cartas do SpellTable, utilizando técnicas avançadas de processamento de vídeo para garantir maior precisão na leitura das cartas durante as partidas.
<br></br>

<h2>Modelagem Funcional do Sistema</h2>
<p>O projeto foi dividido em três subsistemas principais:</p>
<ol>
    <li><strong>Entrada/Saída:</strong> Gerencia a conexão com a câmera e a interface gráfica, detectando os cliques dos usuários e enviando as imagens capturadas para os estágios subsequentes.</li>
    <li><strong>Separação das Cartas:</strong> Localiza e isola a carta desejada da imagem capturada, removendo o fundo e outras informações irrelevantes.</li>
    <li><strong>Identificação das Cartas:</strong> Compara a imagem processada com um banco de dados de cartas de referência, exibindo na interface gráfica a melhor correspondência encontrada.</li>
</ol>
<br>
<div align="center"><img src="https://github.com/user-attachments/assets/bb04ecd3-7f3c-4a18-b257-d7162bcfd8ff">
<br>
Neste desenvolvimento, fui responsável pelo pré-processamento das imagens e pela criação de um método de comparação entre as imagens capturadas pela câmera do usuário e as imagens em alta resolução das cartas, usadas como referência</div>

