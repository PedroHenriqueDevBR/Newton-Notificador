<script setup>
import { useRoute } from 'vue-router'
import { useNotificacaoStore } from '@/stores/NotificacaoStore';
import { onMounted, ref } from 'vue';

const route = useRoute()
const notificacaoStore = useNotificacaoStore()
const id = route.params.id
let notificacao = ref(null)

async function carregarDetalhesNotificacao() {
  try {
        const response = await notificacaoStore.notificacaoPorID(id)
        notificacao.value = response
    } catch (erro) {
        if (erro instanceof AuthException) router.push('/auth')
        if (erro instanceof ServerException) alert('Sem conexão com o servidor!')
    }
}

onMounted(() => {
  carregarDetalhesNotificacao()
})

</script>

<template>
  <div v-if="notificacao == null" class="preencher-pagina">
      <div class="uk-flex uk-flex-center uk-flex-column uk-flex-middle">  
        <span uk-icon="icon: refresh; ratio: 2" class="carregando"></span>
        <p>Carregando...</p>
      </div>
    </div>
  
  <main v-if="notificacao != null" class="uk-padding">
    <div class="uk-container uk-card uk-card-body uk-background-muted">
      <h1>
        <RouterLink
          to="/"
          class="uk-margin-small-right"
          uk-icon="icon: arrow-left; ratio: 2"
        ></RouterLink>
        {{ notificacao.titulo }}
      </h1>
      <hr class="uk-divider-small" />
      <p class="uk-margin-remove">
        <b>Sistema:</b> {{ notificacao.sistema }} |
        <b>Destinatário:</b> {{ notificacao.destinatarios }}
      </p>
      <b>histórico: </b>

      <span v-for="status of notificacao.lista_status" :key="status"
      :class="['uk-badge uk-margin-small-right', status]">
        {{ status }}
      </span>
      <hr class="uk-divider-small" />

      <article class="uk-article">
        <div v-html="notificacao.descricao"></div>
      </article>

    </div>
  </main>
</template>

<style scoped>
.aguardando,
.Recebido {
  background-color: #039be5;
}

.erro,
.Erro {
  background-color: #d32f2f;
}

.enviado,
.Enviado {
  background-color: #689f38;
}

@keyframes girar {
    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(360deg);
    }
}

.carregando {
    animation: girar 1s linear infinite;
}


.remove-decoration {
    text-decoration: none !important;
    color: inherit;
}

.preencher-pagina {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
