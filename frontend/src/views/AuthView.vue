<script setup></script>

<template>
  <main class="uk-flex uk-flex-center uk-flex-middle">
    <div class="uk-card uk-card-default uk-background-muted uk-padding">
      <form>
        <h1>Autenticação</h1>
        <hr class="uk-divider-small">
        <div class="uk-margin">
          <label for="username" class="uk-form-label">Nome de usuário</label>
          <div class="uk-form-controls">
            <input type="text" class="uk-input" id="username" name="username" placeholder="username">
          </div>
        </div>

        <div class="uk-margin">
          <label for="password" class="uk-form-label">Senha</label>
          <div class="uk-form-controls">
            <input type="text" class="uk-input" id="password" name="password" placeholder="********">
          </div>
        </div>

        <button class="uk-button uk-button-primary">Entrar</button>
      </form>
    </div>
  </main>
</template>

<style scoped>
main {
  height: 100vh;
  width: 100%;
}

form {
  min-width: 400px;
}
</style>
