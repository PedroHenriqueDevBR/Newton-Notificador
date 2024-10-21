<script setup>
import NavBar from '@/components/NavBar.vue';
import NotificacaoList from '@/components/NotificacaoList.vue';
import NotificacaoOpcoes from '@/components/NotificacaoOpcoes.vue';
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