<script setup></script>

<template>
  <main class="uk-padding">
    <div class="uk-container uk-card uk-card-body uk-background-muted">
      <h1>
        <RouterLink
          to="/"
          class="uk-margin-small-right"
          uk-icon="icon: arrow-left; ratio: 2"
        ></RouterLink>
        Título da notificação
      </h1>
      <hr class="uk-divider-small" />
      <p class="uk-margin-remove">
        <b>Sistema:</b> Sistema Selecionado |
        <b>Destinatário:</b> usuario@mail.com
      </p>
      <b>histórico: </b>
      <span class="uk-badge uk-margin-small-right aguardando">Aguardando</span>
      <span class="uk-badge uk-margin-small-right erro">Erro</span>
      <span class="uk-badge uk-margin-small-right enviado">Enviado</span>
      <hr class="uk-divider-small" />

      <article class="uk-article">
        <h1 class="uk-article-title">
          <a class="uk-link-reset" href="">Heading</a>
        </h1>

        <p class="uk-article-meta">
          Written by <a href="#">Super User</a> on 12 April 2012. Posted in
          <a href="#">Blog</a>
        </p>

        <p class="uk-text-lead">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip.
        </p>

        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>
      </article>

      <hr class="uk-divider-icon" />

      <div class="uk-alert-success" uk-alert>
        <p>Solicitação enviada para o destinatário.</p>
      </div>

      <div class="uk-alert-danger" uk-alert>
        <p>Erro: credenciais inválidas.</p>
      </div>

      <div class="uk-alert-primary" uk-alert>
        <p>Solicitação de notificação registrada.</p>
      </div>
    </div>
  </main>
</template>

<style scoped>
.aguardando {
  background-color: #039be5;
}

.erro {
  background-color: #d32f2f;
}

.enviado {
  background-color: #689f38;
}
</style>
