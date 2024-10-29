import { defineStore } from 'pinia'
import { ref } from 'vue'
import NotificacaoRepository from '@/repositories/NotificacaoRepository'
import { AuthException, ServerException } from '@/exception/CustomExceptions'
import Notificacao from '@/models/NotificacaoModel'

export const useNotificacaoStore = defineStore('NotificacoesStore', () => {
    const notificacoes = ref([])
    const repository = new NotificacaoRepository();
    const ultimoStatus = ref('')
    const statusSelecionado = ref('')
    let pagina = 1
    let limite = ref(false)

    function adicionar(notificacao) {
        notificacoes.value.push(notificacao)
    }

    function selecionarStatus(status){
        statusSelecionado = status
    }

    function extrairNotificacoes(results) {
        for (const dado of results) {
            const lista_status = []
            for (const item of dado.status) lista_status.push(item.get_status_display);
            adicionar(
                new Notificacao(
                    dado.id, 
                    dado.assunto, 
                    dado.conteudo, 
                    dado.sistema.first_name, 
                    lista_status,
                )
            )
        }
    }

    async function carregarLista() {
        const lista_sistemas = []
        if (ultimoStatus.value != statusSelecionado.value) {
            notificacoes.value = []
            pagina = 1
            limite.value = false
        }
        if (limite.value) return []

        try {
            const notificacoesResponse = await repository.buscarNotificacoes(
                lista_sistemas, 
                statusSelecionado.value,
                pagina,
            )
            extrairNotificacoes(notificacoesResponse.results)
            if (notificacoesResponse.next == null) limite.value = true
            ultimoStatus.value = statusSelecionado.value
            pagina = pagina + 1
        } catch (erro) {
            if (erro instanceof AuthException) throw new AuthException()
            if (erro instanceof ServerException) throw new ServerException()
        }
        return []
    }

    return { notificacoes, adicionar, carregarLista, statusSelecionado, limite }
})
