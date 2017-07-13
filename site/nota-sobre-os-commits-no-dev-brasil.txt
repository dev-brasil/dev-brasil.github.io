title: Nota sobre os commits no dev-brasil
tags: git, normas, dev-brasil

Este post é uma sugestão de padrão para os
commits feitos nos repositórios do dev-brasil
no github. Ela pode (e deve) ser revisada,
podendo ser trocada por uma convenção julgada
mais conveniente pelo time dev-brasil.

[TOC]

## Padrões a serem seguidos em um commit

Cada commit serve para alguma finalidade
específica: resolver um bug, adicionar uma
nova funcionalidade ao código etc. Deve-se
frisar aqui que os commits devem ser curtos
sempre que possível, e devem resolver um problema
apenas. Commits longos, que alteram várias partes
do código ao mesmo tempo, tendem a impactar a revisão
pelos pares de forma negativa. O objetivo
deste post é propor um formato para as mensagens de commit
do repositório.

### O formato da mensagem do commit

[TAG] resumo (deve ser curto)
(linha vazia)
Explicação mais detalhada se necessário

### As tags
* [DEV] commits normais de desenvolvimento
* [DEBUG] commits de debug
* [BUILD] para problemas de compilação
* [WARNINGFIX] para commits que eliminam warnings de compilação

Outras tags poderão ser sugeridas, dentro do espírito acima.
