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
    let selecionados = []

    function adicionar(notificacao) {
        notificacoes.value.push(notificacao)
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

    function formatarSelecionados(sistemas) {
        // Se o tamanho das listas forem diferentes as variaveis devem ser reiniciadas
        if (selecionados.length !== sistemas.length) {
            if (selecionados.length > 0 && sistemas.length === 0) return selecionados
            selecionados = sistemas
            restaurarVariaveis()
            return sistemas
        }

        // verifica se as listas são iguais, se nao reinicia as variaveis
        for (let i = 0; i < sistemas.length; i++) {
            if (sistemas[i] !== selecionados[i]) {
                selecionados = sistemas
                restaurarVariaveis()
                return sistemas
            }
        }
   
        return selecionados
    }

    function restaurarVariaveis() {
        notificacoes.value = []
        pagina = 1
        limite.value = false
    }

    async function carregarLista(listaSistemas = []) {
        if (ultimoStatus.value != statusSelecionado.value) restaurarVariaveis()
        const sistemas = formatarSelecionados(listaSistemas)
        if (limite.value) return []

        console.log(sistemas)

        try {
            const notificacoesResponse = await repository.buscarNotificacoes(
                sistemas, 
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
