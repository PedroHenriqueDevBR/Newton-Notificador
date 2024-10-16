<h1 align="center">
<img src="docs/imagens/logo.jpeg" alt="Logo Newton Notificador" width="80px">
</h1>
<h1 align="center">
Newton - Notificador
</h1>

Esse sistema foi desenvolvido para facilitar o gerenciamento no envio de e-mails pelos sistema de uma organização, o objetivo principal é fazer com que a configuração de envio de emails seja feita apenas uma vez no sistema de notificações, dessa forma todos os sistemas da organização poderão enviar emails bastando apenas uma chamada HTTP ao Notificador e o mesmo se responsabiliza pelo resto.

## Problemas resolvidos

1. Uma única configuração para que todos os sistemas possam enviar notificações;
2. Facilmente configurável, caso o provedor mude a configuração precisa ser feita apenas uma vez;
3. A requisição de envio de emails e SMS passam a ser facilitadas pois ela é feita por uma chamada HTTP junto com um Token de acesso.
4. Todos os registros de envio de notificações ficam salvos e organizados em um local;
5. Os erros no envio são registrados de forma simples e podem ser visualizados nos detalhes de um envio.

## Descrição detalhada do fluxo das notificações

O fluxo comum para o envio de emails e SMS é a configuração dos provedores em cada um dos sistemas da empresa, portanto, para cada sistema que precisa enviar um email há uma série de configurações que precisam ser feitas que o processo funcione corretamente.

Observe a imagem abaixo para entender melhor:

<img src="docs/imagens/Notificador-fluxo-comum.png" alt="Fluxo comum para envio de emails e SMS">

Observe que na imagem acima temos 3 sistemas que servem de exemplo para a explicação, o primeiro sistema faz envio de emails e SMS, o segundo faz o envio de SMS somente, o terceiro faz envio de emails somente.

Cada um dos sistemas possuem configurações próprias para que o envio de notificações possa ser realizado, se por acaso o segundo sistema precisar enviar email o mesmo deverá ser configurado para isso, o mesmo se aplica ao terceito sistema para o caso de envio de SMS.

## Fluxo do Notificador

O notificador funciona como uma camada que fica entre os sistemas e os provedores de email e SMS.

<img src="docs/imagens/Notificador-fluxo-notificador.png" alt="Fluxo organizado pelo Notificador">

O Notificador configura todas as funcionalidades necessárias para o envio de emails e disponibiliza uma chamada HTTP junto com um Token para que os sistemas possam fazer requisições, dessa forma o Notificador faz todo o serviço de envio de emails e SMS.
