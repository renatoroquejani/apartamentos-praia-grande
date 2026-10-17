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
