<script setup>
import { useAuthStore } from '@/stores/AuthStore';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const username = ref('')
const password = ref('')
const erro = ref('')

const authStore = useAuthStore()
const router = useRouter()

async function autenticar() {
  await authStore.autenticar(username.value, password.value)
  if (authStore.logado) {
    router.push('/')
  } else {
    erro.value = 'Problemas com a requisição'
  }
}

</script>

<template>
  <main class="uk-flex uk-flex-center uk-flex-middle">
    <div class="uk-card uk-card-default uk-background-muted uk-padding">
      <form>
        <h1>Autenticação</h1>
        <hr class="uk-divider-small">
        <div class="uk-margin">
          <label for="username" class="uk-form-label">Nome de usuário</label>
          <div class="uk-form-controls">
            <input type="text" class="uk-input" id="username" name="username" placeholder="username" v-model="username">
          </div>
        </div>

        <div class="uk-margin">
          <label for="password" class="uk-form-label">Senha</label>
          <div class="uk-form-controls">
            <input type="password" class="uk-input" id="password" name="password" placeholder="********"
              v-model="password">
          </div>
        </div>

        <label>{{ erro }}</label>
        <hr v-if="erro" class="uk-divider-small">

        <button type="button" class="uk-button uk-button-primary" @click="autenticar()">Entrar</button>
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
