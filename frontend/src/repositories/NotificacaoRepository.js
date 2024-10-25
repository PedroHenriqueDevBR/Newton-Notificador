import Notificacao from '@/models/NotificacaoModel'
import RequestApi from './RequestAPI'
import { AuthException, ServerException } from '@/exception/CustomExceptions'

class NotificacaoRepository {
    constructor() { this.requester = new RequestApi() }

    async buscarNotificacoes() {
        const url = '/api/v1/notificacoes'
        try {
            const dados = await this.requester.get(url)
            const notificacoes = []
            for (const dado of dados) {
                const lista_status = []
                for (const item of dado.status) lista_status.push(item.get_status_display);
                notificacoes.push(new Notificacao(dado.id, dado.assunto, dado.conteudo, dado.sistema.first_name, lista_status))
            }
            return notificacoes
        }
        catch (erro) {
            if (erro instanceof AuthException) throw new AuthException()
            if (erro instanceof ServerException) throw new ServerException()
        }

        return []
    }
}

export default NotificacaoRepository
