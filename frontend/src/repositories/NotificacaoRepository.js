import Notificacao from '@/models/NotificacaoModel'

class NotificacaoRepository {
    constructor() { }

    async buscarNotificacoes(pagina) {
        console.log('Carregando pag: ' + pagina)
        await new Promise(resolve => {
            setTimeout(() => {
                console.log('Tempo fake');
                resolve();
            }, 500)
        })

        console.log('Carregou pag: ' + pagina)
        return [
            new Notificacao(1, 'titulo', 'descricao', 'sistema', []),
            new Notificacao(2, 'titulo', 'descricao', 'sistema', []),
        ]
    }
}

export default NotificacaoRepository
