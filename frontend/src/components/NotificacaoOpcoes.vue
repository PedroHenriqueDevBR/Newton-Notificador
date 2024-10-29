<script setup>
import { RouterLink, useRouter } from 'vue-router'
import { useSistemaStore } from '@/stores/SistemaStore';
import { onMounted } from 'vue';
import { AuthException, ServerException } from '@/exception/CustomExceptions';
import { useNotificacaoStore } from '@/stores/NotificacaoStore';
import { useCarregandoStore } from '@/stores/carregando';

const sistemaStore = useSistemaStore()
const notificacaoStore = useNotificacaoStore()
const carregandoStore = useCarregandoStore()

const router = useRouter()

async function carregarSistemas() {
  try {
    await sistemaStore.buscarSistemas()
  } catch (erro) {
    if (erro instanceof AuthException) router.push('/auth')
    if (erro instanceof ServerException) alert('Sem conexão com o servidor!')
  }

}

async function carregarNotificacoes() {
    carregandoStore.alterarStatus(true)
    const idSistemas = sistemaStore.idSelecionados()
    
    try {
        await notificacaoStore.carregarLista(idSistemas)
    } catch (erro) {
        if (erro instanceof AuthException) router.push('/auth')
        if (erro instanceof ServerException) alert('Sem conexão com o servidor!')
    } finally {
        carregandoStore.alterarStatus(false);
    }

}

onMounted(() => {
  carregarSistemas()
})

</script>

<template>
  <h2>Opções</h2>

  <div class="uk-card uk-card-body uk-background-muted">
    
      <fieldset class="uk-fieldset">
        <legend class="uk-legend">Sistemas</legend>

        <div class="uk-margin uk-grid-small uk-child-width-auto uk-grid">
          <label v-for="(item, index) in sistemaStore.sistemas" :key="index"><input class="uk-checkbox" type="checkbox" @change="sistemaStore.selecionarSistema(index)" />
            {{ item.nome }}</label>
        </div>
      </fieldset>
      <button class="uk-button uk-button-primary" @click="carregarNotificacoes()">Filtrar</button>
    
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
