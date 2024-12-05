import Notificacao from '@/models/NotificacaoModel'
import RequestApi from './RequestAPI'
import { AuthException, ServerException } from '@/exception/CustomExceptions'

class NotificacaoRepository {
    constructor() { this.requester = new RequestApi() }

    formatarQueryNotificacoes(listaSistema = [], status = '', pagina) {
        let query = ''
        let primeiro = true

        for (const sistema of listaSistema) {
            if (primeiro) {
                query = query + '?sistema=' + sistema
                primeiro = false
                continue
            }
            query = query + '&sistema=' + sistema
        }

        if (status != '' && primeiro) {
            query = query + '?status=' + status
            primeiro = false
        } else if (status != '') {
            query = query + '&status=' + status
        }

        if (pagina != '' && pagina != 0 && pagina != 1 && primeiro) {
            query = query + '?page=' + pagina
            primeiro = false
        } else if (pagina != '' && pagina != 0 && pagina != 1) {
            query = query + '&page=' + pagina
        }

        return query
    }

    async buscarNotificacoes(listaSistema = [], status = '', pagina='') {
        const query = this.formatarQueryNotificacoes(listaSistema, status, pagina)
        const url = '/api/v1/notificacoes' + query

        try {
            return await this.requester.get(url)
        }
        catch (erro) {
            if (erro instanceof AuthException) throw new AuthException()
            if (erro instanceof ServerException) throw new ServerException()
        }

        return []
    }

    async buscarNotificacaoPorID(id) {
        const url = '/api/v1/notificacoes/' + id
        
        try {
            return await this.requester.get(url)
        }
        catch (erro) {
            if (erro instanceof AuthException) throw new AuthException()
            if (erro instanceof ServerException) throw new ServerException()
        }

        return []
    }

    async notificacaoInstantanea(notificacao, sistema) {
        const url = '/api/v1/notificar/instantanea'
        const body = {
            "sistema": sistema,
            "destinatarios": notificacao.destinatarios,
            "assunto": notificacao.titulo,
            "conteudo": notificacao.descricao
        }
        
        try {
            return await this.requester.post(url, body)
        }
        catch (erro) {
            if (erro instanceof AuthException) throw new AuthException()
            if (erro instanceof ServerException) throw new ServerException()
        }

        return []
    }
}

export default NotificacaoRepository
