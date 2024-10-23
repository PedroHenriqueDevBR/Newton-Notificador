<script setup>
import NavBar from '@/components/NavBar.vue'
import NotificacaoList from '@/components/NotificacaoList.vue'
import NotificacaoOpcoes from '@/components/NotificacaoOpcoes.vue'

import { useAuthStore } from '@/stores/AuthStore';
import { useRouter } from 'vue-router';

const authStore = useAuthStore()
const router = useRouter()

async function usuarioLogado() {
  const logado = await authStore.verificarToken()
  console.log('logado: ' + logado)
  if (!logado) router.push('/auth');
  console.log('Usuário logado')
}

usuarioLogado()
</script>

<template>
  <NavBar />

  <main class="uk-container">
    <div uk-grid class="uk-grid-divider uk-child-width-expand@s">
      <div class="uk-width-1-3@m">
        <NotificacaoOpcoes />
      </div>

      <div class="uk-width-expand@m">
        <NotificacaoList />
      </div>
    </div>
  </main>
</template>

<style scoped>
main {
  padding-bottom: 32px;
}
</style>
