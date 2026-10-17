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
