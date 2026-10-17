# Apartamentos Praia Grande

Site independente em `dist/`: HTML, CSS, fotos, vídeo e um pequeno JavaScript para a galeria. Sem dependências, banco de dados ou etapa de build. O restante da pasta fernanda-shopee é outro trabalho e não integra este site.

## Visualizar

Na pasta locacoes, execute `python3 -m http.server 4173 --directory dist` e abra http://localhost:4173. Também é possível abrir dist/index.html diretamente.

## Publicar

Site: https://aptospg.com.br/
Repositório: https://github.com/renatoroquejani/apartamentos-praia-grande

Alterações em dist enviadas à main são publicadas automaticamente pelo workflow .github/workflows/pages.yml, sem instalar dependências ou executar build. Só dist é publicado; documentação e arquivos de preparo permanecem no repositório. O Pages está configurado para GitHub Actions. Use links terminados em .html para compartilhar páginas de imóveis.

A configuração .openai/hosting.json preserva a identificação da hospedagem Sites anterior. A publicação atual usa GitHub Pages. Se trocar o domínio, atualize og:image em todos os HTMLs.

## Atualizar imóveis

Duplique kitnet-928.html para criar a página de outro apartamento, troque fotos, conteúdo, metadados e mensagem dos links WhatsApp. Acrescente um article.property em index.html. Não marque um imóvel como disponível em datas específicas sem conferir com Fernanda. Remova da listagem quando sair de locação.

Contato: +55 19 99961-5553, presente nos dois HTMLs e links wa.me/tel. Os links abrem uma mensagem editável; nada é enviado automaticamente.

Os vídeos ficam em assets/kit-928/ambientes.mp4 (478×638, sem as faixas pretas embutidas) e passeio.mp4 (480×848 após rotação). Usam H.264/AAC, faststart e preload none. As fontes anteriores estão em media/originais. Reprodução do preparo: python3 docs/editar-video.py (requer FFmpeg instalado). Não foram enviados ao YouTube. Para usar YouTube, publique na conta escolhida e substitua os players por embeds com título acessível e carregamento lazy. Não é necessário mudar o restante do site.

Fontes e decisões: docs/brief.md. Tokens e direção visual: DESIGN.md.

## Galeria e fotos tratadas

O visualizador usa dialog nativo com gallery.js: setas, Esc, foco restaurado, bloqueio de rolagem e deslize horizontal. Sem suporte a dialog ou sem JavaScript, os links continuam abrindo as fotos. Cada foto tratada tem sufixo -tratada.jpg; arquivos sem sufixo são originais, disponíveis no link do modal. Prompts e seleção estão em docs/imagegen-prompts.md. Tratamento de IA pode alterar detalhes finos, por isso a indicação e os originais ficam disponíveis.

## Kitnet 1027

Página kitnet-1027.html com dois vídeos no início, sem galeria de fotos. A capa do catálogo é um quadro do vídeo. Vídeos e posters em dist/assets/kit-1027; originais em media/originais/kit-1027. A faixa de telefone foi substituída pelo contato da Fernanda com autorização do usuário. Para reproduzir o preparo, execute python3 docs/preparar-kit-1027.py com FFmpeg disponível. A arte do contato fica em media/kit-1027-contato.png.

## Kitnet 2014

Cobertura no 20º andar com sacada em L: kitnet-2014.html. Três fotos originais com galeria, vídeo de passeio e vídeo da vista separados. Mídia em dist/assets/kit-2014. Para reproduzir a substituição da faixa de telefone, execute python3 docs/preparar-kit-2014.py com FFmpeg disponível. Os originais são mantidos em media/originais/kit-2014.

## Apartamento de 1 dormitório — 19º andar

Página apartamento-19-andar.html, sem número de unidade informado. Em reforma, na seção Em preparação do catálogo. Vídeo de referência em assets/apto-19-andar/referencia.mp4; substitua vídeo e poster após a conclusão e revise os avisos antes de anunciar disponibilidade. Capacidade informada pelo usuário: oito pessoas. Preparo reproduzível: python3 docs/preparar-apto-19-andar.py.

## Apartamento de 3 dormitórios — 11º andar

Página apartamento-3-dormitorios.html. Quatorze fotos em assets/apto-11-andar; sete interiores tratados com GPT Image e originais preservados para comparação. Três destaques e miniaturas adicionais expansíveis usam o mesmo modal. Vídeo horizontal preservado sem recompressão, com faststart: python3 docs/preparar-apto-11-andar.py.
