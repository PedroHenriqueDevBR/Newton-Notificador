import { defineStore } from 'pinia'
import { ref } from 'vue'
import NotificacaoRepository from '@/repositories/NotificacaoRepository'
import { AuthException, ServerException } from '@/exception/CustomExceptions'

export const useNotificacaoStore = defineStore('NotificacoesStore', () => {
    const notificacoes = ref([])
    const repository = new NotificacaoRepository();
    const ultimoStatus = ref('')
    const statusSelecionado = ref('')

    function adicionar(notificacao) {
        notificacoes.value.push(notificacao)
    }

    function selecionarStatus(status){
        statusSelecionado = status
    }

    async function carregarLista() {
        if (ultimoStatus != statusSelecionado) notificacoes.value = []
        try {
            const notificacoesResponse = await
                repository.buscarNotificacoes([], statusSelecionado.value)
            for (const notificacao of notificacoesResponse) {
                notificacoes.value.push(notificacao)
            }
            ultimoStatus = statusSelecionado
        } catch (erro) {
            if (erro instanceof AuthException) throw new AuthException()
            if (erro instanceof ServerException) throw new ServerException()
        }
        return []
    }

    return { notificacoes, adicionar, carregarLista, statusSelecionado }
})
