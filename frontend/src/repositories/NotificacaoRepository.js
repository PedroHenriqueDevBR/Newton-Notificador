import Notificacao from '@/models/NotificacaoModel'
import AuthRepository from './AuthRepository'

class NotificacaoRepository {
    constructor() {
        this.urlBase = 'http://localhost:8000'
        this.authRepository = new AuthRepository()
    }

    async buscarNotificacoes(pagina) {
        const url = this.urlBase + '/api/v1/notificacoes'
        const token = await this.authRepository.token()
        const response = await fetch(url, {
            headers: { 'Content-Type': 'application/json', 'Authorization': token }
        })

        if (response.status >= 200 && response.status < 300) {
            const notificacoes = []
            const dados = await response.json()
            for (const dado of dados) {
                const lista_status = []
                for (const item of dado.status) lista_status.push(item.get_status_display);
                notificacoes.push(new Notificacao(dado.id, dado.assunto, dado.conteudo, dado.sistema.first_name, lista_status))
            }
            return notificacoes
        }
        return []
    }
}

export default NotificacaoRepository
