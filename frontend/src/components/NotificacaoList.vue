<script setup>
import { RouterLink } from 'vue-router'
import NotificacaoItem from './NotificacaoItem.vue'
import { useNotificacaoStore } from '@/stores/NotificacaoStore'
import { ref } from 'vue'

const notificacaoStore = useNotificacaoStore()
let paginaAtual = 0
let carregando = ref(false)
let haMaisNotificacoes = ref(true)

async function carregarNotificacoes() {
    carregando.value = true;
    const quantidadeAtual = notificacaoStore.notificacoes.length
    await notificacaoStore.carregarLista(paginaAtual)
    const novaQuantidade = notificacaoStore.notificacoes.length
    if (quantidadeAtual == novaQuantidade) haMaisNotificacoes.value = false
    carregando.value = false;
}

function mostrarCarregando() {
    return carregando.value && notificacaoStore.notificacoes.length === 0;
}

function mostrarContainerNotificacoes() {
    return !carregando.value || notificacaoStore.notificacoes.length > 0;
}

function mostrarBotaoCarregarMais() {
    return !carregando.value && haMaisNotificacoes && notificacaoStore.notificacoes.length > 0;
}
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
            <RouterLink to="detalhes" class="remove-decoration" v-for="notificacao in notificacaoStore.notificacoes"
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
