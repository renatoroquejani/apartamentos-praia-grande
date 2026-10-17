# Apartamentos Praia Grande

Site independente em `dist/`: HTML, CSS, fotos, vídeo e um pequeno JavaScript para a galeria. Sem dependências, banco de dados ou etapa de build. O restante da pasta fernanda-shopee é outro trabalho e não integra este site.

## Visualizar

Na pasta locacoes, execute `python3 -m http.server 4173 --directory dist` e abra http://localhost:4173. Também é possível abrir dist/index.html diretamente.

## Publicar

Publique o conteúdo de dist em qualquer hospedagem estática. A configuração .openai/hosting.json registra a hospedagem Sites usada nesta conversa. Se trocar o domínio, atualize og:image nos dois HTMLs.

## Atualizar imóveis

Duplique kitnet-928.html para criar a página de outro apartamento, troque fotos, conteúdo, metadados e mensagem dos links WhatsApp. Acrescente um article.property em index.html. Não marque um imóvel como disponível em datas específicas sem conferir com Fernanda. Remova da listagem quando sair de locação.

Contato: +55 19 99961-5553, presente nos dois HTMLs e links wa.me/tel. Os links abrem uma mensagem editável; nada é enviado automaticamente.

O vídeo único está em assets/kit-928/passeio-completo.mp4, H.264/AAC, vertical 480 × 854, com faststart e preload none. As fontes anteriores estão em media/originais. Reprodução da montagem: python3 docs/editar-video.py (requer FFmpeg instalado). Não foram enviados ao YouTube. Para usar YouTube, publique na conta escolhida e substitua o player por embeds com título acessível e carregamento lazy. Não é necessário mudar o restante do site.

Fontes e decisões: docs/brief.md. Tokens e direção visual: DESIGN.md.

## Galeria e fotos tratadas

O visualizador usa dialog nativo com gallery.js: setas, Esc, foco restaurado, bloqueio de rolagem e deslize horizontal. Sem suporte a dialog ou sem JavaScript, os links continuam abrindo as fotos. Cada foto tratada tem sufixo -tratada.jpg; arquivos sem sufixo são originais, disponíveis no link do modal. Prompts e seleção estão em docs/imagegen-prompts.md. Tratamento de IA pode alterar detalhes finos, por isso a indicação e os originais ficam disponíveis.
