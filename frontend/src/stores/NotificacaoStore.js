import { defineStore } from 'pinia'
import { ref } from 'vue'
import NotificacaoRepository from '@/repositories/NotificacaoRepository'

export const useNotificacaoStore = defineStore('NotificacoesStore', () => {
    const notificacoes = ref([])
    const repository = new NotificacaoRepository();

    function adicionar(notificacao) {
        notificacoes.value.push(notificacao)
    }

    async function carregarLista(paginaAtual) {
        let notificacoesResponse = await
            repository.buscarNotificacoes(paginaAtual)
        for (const notificacao of notificacoesResponse) {
            notificacoes.value.push(notificacao)
        }
    }

    return { notificacoes, adicionar, carregarLista }
})
