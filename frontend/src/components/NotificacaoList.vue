<script setup>
import { RouterLink, useRouter } from 'vue-router'
import NotificacaoItem from './NotificacaoItem.vue'
import { useNotificacaoStore } from '@/stores/NotificacaoStore'
import { onMounted, ref } from 'vue'
import { AuthException, ServerException } from '@/exception/CustomExceptions'
import { useCarregandoStore } from '@/stores/carregando'

const notificacaoStore = useNotificacaoStore()
const carregandoStore = useCarregandoStore()

const router = useRouter()

async function carregarNotificacoes() {
    carregandoStore.alterarStatus(true)

    try {
        await notificacaoStore.carregarLista()
    } catch (erro) {
        if (erro instanceof AuthException) router.push('/auth')
        if (erro instanceof ServerException) alert('Sem conexão com o servidor!')
    } finally {
        carregandoStore.alterarStatus(false);
    }

}

function mostrarCarregando() {
    return carregandoStore.estaCarregando() && notificacaoStore.notificacoes.length === 0;
}

function mostrarContainerNotificacoes() {
    return !carregandoStore.estaCarregando() || notificacaoStore.notificacoes.length > 0;
}

function mostrarBotaoCarregarMais() {
    return !carregandoStore.estaCarregando() && notificacaoStore.limite == false && notificacaoStore.notificacoes.length > 0
}

onMounted(() => { if (notificacaoStore.notificacoes.length == 0) carregarNotificacoes() })
</script>

<template>
    <h2>Notificações</h2>
    <div v-if="mostrarCarregando()" class="preencher-pagina uk-flex uk-flex-middle uk-flex-center uk-flex-column">
        <span uk-icon="icon: refresh; ratio: 2" class="carregando"></span>
        <p>Carregando...</p>
    </div>

    <div v-if="mostrarContainerNotificacoes()">
        <div v-if="notificacaoStore.notificacoes.length === 0">
            <p>Nenhuma notificação registrada</p>
            <button class="uk-button uk-button-default" @click="carregarNotificacoes()">
                <span uk-icon="icon: refresh"></span>
                recarregar
            </button>
        </div>
        <dl class="uk-description-list">
            <RouterLink :to="{path: 'detalhes/' + notificacao.id}" class="remove-decoration" v-for="notificacao in notificacaoStore.notificacoes"
                :key="notificacao.id">
                <NotificacaoItem :notificacao="notificacao" />
            </RouterLink>
        </dl>

        <div class="uk-flex uk-flex-center">
            <button v-if="mostrarBotaoCarregarMais()" class="uk-button uk-button-default"
                @click="carregarNotificacoes()">Carregar mais</button>
        </div>
    </div>
</template>

<style scoped>
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
    height: 80%;
}
</style>
