# Verificação — 17/10/2026

- HTTP local 200 para início e detalhe.
- Validador HTMLParser: uma h1 por documento, arquivos de mídia e fragmentos presentes, imagens com alt e dimensões, WhatsApp com número autorizado, nenhum script.
- Navegador IAB: navegação catálogo → imóvel; abertura das perguntas frequentes; vídeos com readyState 4, tempos avançando, durações 43,65 s e 78,67 s, sem erros de mídia.
- Capturas desktop e iframes com viewports 390 e 320 px em docs/qa. Conteúdo legível, fotos proporcionais e contato fixo visível. Não houve teste em aparelho físico.
- Auditoria estática frontend premium strict: zero achados (docs/ui-audit.json).
- Revisão visual pelo brief e pelas fotos originais. Não há screenshot de referência de UI para pontuação de fidelidade.
- Lint, typecheck e build de framework não se aplicam: HTML/CSS estáticos sem dependências.
- Sem envio de mensagens de teste ao WhatsApp; verificados destino e texto dos links.
- Originais preservados; fotos do site ~0,74 MB no total e vídeos ~20,3 MB. Vídeos só carregam quando solicitados.
- Valores, datas e condições continuam sujeitos a confirmação com a Fernanda.

## Revisão 2 — título, fotos, galeria e vídeo único

- Marca e metadados: Apartamentos Praia Grande; Fernanda apenas no contato.
- Validação HTMLParser: todos os href/src/poster/data-original e fragmentos resolvem; exatamente um player, um dialog e três links de galeria. Fotos tratadas e originais são arquivos distintos.
- node --check dist/gallery.js: sucesso. Não há linter/typechecker de framework neste projeto estático.
- FFmpeg decodificou o vídeo inteiro sem erros. FFprobe: H.264/AAC, 480×854, 30 fps, 122,323 segundos, 15.893.454 bytes. Blackdetect não detecta mais os intervalos pretos de 0,5 s do primeiro vídeo. O áudio original foi mantido na montagem.
- IAB: vídeo reproduzindo com tempo avançando (3,84 s), dimensão 480×854 e duração 122,323 s.
- Modal real: abrir mantém URL da página, botão próximo troca 1/3 → 2/3; tecla esquerda retorna a 1/3; Esc fecha e devolve foco ao link da foto. Native dialog limita o conteúdo de fundo enquanto aberto.
- Viewports reais de iframe em 390 e 320 px: imagens contidas, fechar e setas sempre visíveis, navegação por botão confirmada. Não houve teste de gesto em aparelho físico.
- Auditoria estática frontend strict: zero achados.
- Fotos: primeira tentativa de sala e vista foi rejeitada por alterar céu. Versões mais discretas selecionadas. O tratamento é generativo; detalhes finos não são garantidos idênticos. Indicação pública e acesso aos originais incluídos. Prompts em imagegen-prompts.md.
- Captura de modal móvel em .omx/qa/revisao-2/galeria-mobile.png. Sem referência visual externa de UI para pontuar fidelidade; inspeção visual do resultado e comparação das fotos realizadas.

## Revisão 3 — proporções dos vídeos

A pedido do usuário, a montagem única foi substituída por dois vídeos com proporções independentes. O primeiro tinha faixas pretas incorporadas: cropdetect identificou imagem útil 478×638 em x=0,y=106. Recorte aplicado somente às faixas, sem cortar conteúdo útil. Após preparo, cropdetect retorna 478×638 em x=0,y=0; duração 43,65 s. Segundo vídeo remuxado integralmente, incluindo áudio e rotação; duração 78,67 s. Posters extraídos dos arquivos finais, sem barras adicionadas pelo CSS. Em telas até 650 px, vídeos empilhados; até 900 px, coluna de conteúdo ampla para evitar players apertados pelo contato lateral.

As verificações anteriores sobre um único player descrevem uma versão substituída. Estado final esperado: dois players, três fotos tratadas e um modal.

## Kitnet 1027 — inclusão da segunda unidade

- Catálogo lista 928 e 1027; navegação real pelo link da nova unidade confirmada no IAB.
- Nova página: 10º andar, até 6 pessoas, mesmo endereço; dois vídeos no início e sem galeria de fotos fictícia. Capa e posters extraídos dos vídeos.
- Os dois MP4 decodificados integralmente sem erros. H.264/AAC, 480×848, 29,257 s e 38,290 s; controles nativos, preload none, sem autoplay. Cropdetect dos originais retorna quadro inteiro, sem faixas a recortar.
- Faixa de telefone anterior coberta no rodapé direito por Contato Fernanda e (19) 99961-5553, conforme escolha explícita do usuário. Posters dos dois arquivos finais inspecionados visualmente. Demais legendas e áudio preservados.
- IAB: ambos reproduzindo com avanço de tempo e durações corretas.
- Todos os HTMLs do catálogo passaram em validação de arquivos, fragmentos e uma h1 por página. WhatsApp da nova página referencia Kitnet 1027 e número autorizado.
- Layout de 320 px conferido por iframe real: título, capacidade, andar e contato sem corte. Em celular os vídeos ficam empilhados. Sem teste em aparelho físico.
- Auditoria estática frontend strict: zero achados. git diff --check sem erros. Sem novos scripts no navegador ou dependências.
- FFmpeg disponível não tem filtro drawtext; a faixa gráfica de contato foi renderizada com biblioteca já instalada e incorporada por overlay. Script de preparo e PNG preservados no projeto.

## Kitnet 2014 — terceira unidade

- Catálogo contém 928, 1027 e 2014; navegação real pelo link Conheça a cobertura confirmada no IAB.
- Nova página identifica 20º andar, cobertura, sacada em L e até seis pessoas; capacidade confirmada no texto incorporado ao vídeo.
- Três fotos originais, sem tratamento generativo. Galeria percorre 1/3 → 2/3 → 3/3 por teclado e Esc fecha com foco restaurado ao link original.
- Dois vídeos independentes H.264/AAC, 480×848, 59,582 s e 15,023 s. Decodificação integral dos dois sem erros. Cropdetect indica quadro inteiro, sem faixas pretas a remover.
- IAB confirmou reprodução com tempo avançando: primeiro 3,68 s, segundo 0,13 s, ambos sem erros de mídia.
- Inspeção do poster final confirma o contato da Fernanda na faixa do primeiro vídeo; segundo vídeo sem telefone original preservado. Arquivos de compartilhamento copiados e conferidos por tamanho em Downloads/Kitnet 2014 - Videos para WhatsApp.
- Telas de 390 e 320 px conferidas em iframes reais; título, galeria e contato visíveis e proporcionais. Sem teste de gesto em aparelho físico.
- Todos os quatro HTMLs passam em validação de arquivos, fragmentos e uma h1 por página. Nova página tem três links de foto, dois vídeos e WhatsApp com unidade 2014 e número correto.
- Auditoria estática frontend strict: zero achados. Sem dependências ou alterações em CSS/JS compartilhados.

## Apartamento de 1 dormitório — 19º andar, em reforma

- Nova página e entrada separada Em preparação; sem prometer liberação para locação. Navegação real do catálogo confirmada.
- Vídeo inteiro decodificado por FFmpeg sem erros. IAB reproduziu por 7,01 s, duração 60,070 s, 480×848, sem erro de mídia. Controles nativos, preload none, sem autoplay.
- Poster inspecionado: máscara cobre capacidade e contato anteriores; mostra Em reforma, até 8 pessoas e Fernanda (19) 99961-5553. Original preservado. Cópia para WhatsApp conferida byte a byte.
- Layouts reais de iframe de 320 e 390 px inspecionados: título, status e contato sem corte. Sem teste em aparelho físico.
- Cinco HTMLs validados: arquivos e fragmentos resolvem, uma h1 por página; nova página com um player e contatos corretos.
- Reutilizados template e controles existentes; sem dependências novas ou build/typecheck de framework.

## Apartamento de 3 dormitórios — 11º andar

- Catálogo e nova página testados por navegação real. Galeria com 14 fotos, setas, retorno 1 → 14 → 1 e Esc com foco restaurado; miniaturas adicionais expandem.
- Sete interiores tratados com GPT Image: inspeção lado a lado dos ambientes, móveis e vistas, sem alteração material identificada. Os originais estão disponíveis em cada foto; detalhes finos continuam sujeitos às limitações de tratamento generativo.
- Viewports de iframe de 320 e 390 px: título e contato fixo legíveis; modal de 320 px exibe foto inteira, fechar e setas. Próximo confirmou foto tratada e link para original. Sem teste em aparelho físico.
- Vídeo H.264/AAC horizontal, 848×480, 33,855 s; sem telefone ou barras nas amostras. Remux preserva conteúdo e qualidade, full decode sem erros; IAB reproduzindo em 6,89 s. Não mostra quartos ou banheiros e está descrito como sala/vista. Cópia para WhatsApp verificada por SHA-256.
- Seis HTMLs validados: arquivos e fragmentos resolvem, uma h1 por página. Nova página tem 14 fotos, um modal, um player e WhatsApp com contato/unidade descritiva corretos. node --check gallery.js e git diff --check passaram. Auditoria premium strict: zero achados.
- Reutilizados template, dialog e galeria existentes; sem novas dependências. CSS adicional só para miniaturas e player horizontal. Build/typecheck de framework não se aplicam.

## Migração para GitHub Pages

Repositório público renatoroquejani/apartamentos-praia-grande criado a pedido do usuário; origin configurado e histórico enviado sem sobrescrever repositórios existentes. GitHub Pages com fonte GitHub Actions e HTTPS ativado. Workflow Publish GitHub Pages concluiu com sucesso no commit 69149749e19f6dfd057ec582c21f9aa84a4bd9b5 (run 39079216857). Publica somente dist; metadados de compartilhamento atualizados nos seis HTMLs para a nova origem. Actions fixadas aos SHAs das versões oficiais verificadas. Navegação catálogo → apartamento de três dormitórios e modal com foto tratada/original confirmados na URL publicada. Monitor auxiliar ci_monitor.cjs não está instalado nesta cópia do skill; status verificado pela API oficial do GitHub via gh.

## Guilhermina e ordenação do catálogo

- Sete HTMLs validados: arquivos e fragmentos locais resolvem, uma h1 por página. Pegasus tem oito fotos únicas, quatro tratadas com originais distintos, um modal e dois players. Links WhatsApp identificam Pegasus/Guilhermina e o contato correto.
- Dados copiados do Maschietto removidos: não há andar/endereço/CEP/quantidade de banheiros presumidos. Mapa é busca pelo edifício e bairro.
- Comparação visual das quatro fotos tratadas com as originais: enquadramento, mobiliário e aparência preservados; tratamento generativo pode alterar detalhes finos. Link de original e indicação de IA disponíveis.
- Galeria desktop: 2/8 → 3/8 → 2/8 por botão/teclado; Esc restaura foco. Modal em 320 px contém imagem inteira, fechar, setas e original. Layout em 320/390 px inspecionado; sem aparelho físico.
- Dois vídeos horizontais H.264/AAC 848×480, 97,059 s e 68,569 s. Decode integral sem erros, originais preservados e cópias WhatsApp verificadas por SHA-256. IAB reproduziu ambos em 13,75 e 13,48 s, sem erro de mídia. Sem faixas pretas ou contato antigo nas amostras revisadas.
- Ordem de seis cards validada em código e no navegador: 3 dormitórios Maschietto, 928, 1027, 2014, Guilhermina, reforma. Imagem de abertura agora representa o primeiro imóvel.
- node --check gallery.js, git diff --check e auditoria premium strict passaram, zero achados. Reutilizado o template e galeria existentes; sem dependências ou CSS/JS adicionais.
