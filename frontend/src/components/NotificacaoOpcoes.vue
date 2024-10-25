<script setup>
import { RouterLink, useRouter } from 'vue-router'
import { useSistemaStore } from '@/stores/SistemaStore';
import { onMounted } from 'vue';
import { AuthException, ServerException } from '@/exception/CustomExceptions';

const sistemaStore = useSistemaStore()
const router = useRouter()

async function carregarSistemas() {
  try {
    await sistemaStore.buscarSistemas()
  } catch (erro) {
    if (erro instanceof AuthException) router.push('/auth')
    if (erro instanceof ServerException) alert('Sem conexão com o servidor!')
  }

}

onMounted(() => {
  carregarSistemas()
})

</script>

<template>
  <h2>Opções</h2>

  <div class="uk-card uk-card-body uk-background-muted">
    <form>
      <fieldset class="uk-fieldset">
        <legend class="uk-legend">Sistemas</legend>

        <div class="uk-margin uk-grid-small uk-child-width-auto uk-grid">
          <label v-for="(item, index) in sistemaStore.sistemas" :key="index"><input class="uk-checkbox" type="checkbox"
              checked />
            {{ item.nome }}</label>
        </div>
      </fieldset>
      <button class="uk-button uk-button-primary">Filtrar</button>
    </form>

    <hr class="uk-divider-icon" />

    <RouterLink to="notificar" class="uk-button uk-button-default uk-width-1-1 uk-margin-small-bottom">
      Notificação instantânea
    </RouterLink>
    <RouterLink to="notificar/agendar" class="uk-button uk-button-default uk-width-1-1 uk-margin-small-bottom">
      Agendar notificação
    </RouterLink>
  </div>
</template>

<style scoped></style>
