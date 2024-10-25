import { defineStore } from 'pinia'
import { ref } from 'vue'
import NotificacaoRepository from '@/repositories/NotificacaoRepository'
import { AuthException, ServerException } from '@/exception/CustomExceptions'

export const useNotificacaoStore = defineStore('NotificacoesStore', () => {
    const notificacoes = ref([])
    const repository = new NotificacaoRepository();

    function adicionar(notificacao) {
        notificacoes.value.push(notificacao)
    }

    async function carregarLista() {
        try {
            const notificacoesResponse = await
                repository.buscarNotificacoes()
            for (const notificacao of notificacoesResponse) {
                notificacoes.value.push(notificacao)
            }
        } catch (erro) {
            if (erro instanceof AuthException) throw new AuthException()
            if (erro instanceof ServerException) throw new ServerException()
        }
        return []
    }

    return { notificacoes, adicionar, carregarLista }
})
