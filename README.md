# Fernanda · catálogo de locações

Site independente em `dist/`: HTML, CSS, fotos e vídeos. Sem JavaScript, dependências, banco de dados ou etapa de build. O restante da pasta fernanda-shopee é outro trabalho e não integra este site.

## Visualizar

Na pasta locacoes, execute `python3 -m http.server 4173 --directory dist` e abra http://localhost:4173. Também é possível abrir dist/index.html diretamente.

## Publicar

Publique o conteúdo de dist em qualquer hospedagem estática. A configuração .openai/hosting.json registra a hospedagem Sites usada nesta conversa. Se trocar o domínio, atualize og:image nos dois HTMLs.

## Atualizar imóveis

Duplique kitnet-928.html para criar a página de outro apartamento, troque fotos, conteúdo, metadados e mensagem dos links WhatsApp. Acrescente um article.property em index.html. Não marque um imóvel como disponível em datas específicas sem conferir com Fernanda. Remova da listagem quando sair de locação.

Contato: +55 19 99961-5553, presente nos dois HTMLs e links wa.me/tel. Os links abrem uma mensagem editável; nada é enviado automaticamente.

Vídeos estão em assets/kit-928, H.264/AAC com faststart e preload none. Não foram enviados ao YouTube. Para usar YouTube, publique na conta escolhida e substitua os players por embeds com título acessível e carregamento lazy. Não é necessário mudar o restante do site.

Fontes e decisões: docs/brief.md. Tokens e direção visual: DESIGN.md.
