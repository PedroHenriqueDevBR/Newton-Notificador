import { ref } from "vue";
import SistemaRepository from "@/repositories/SistemaRepository";
import NotificacaoRepository from "@/repositories/NotificacaoRepository";
import { defineStore } from "pinia";
import Notificacao from "@/models/NotificacaoModel";
import { AuthException, ServerException } from "@/exception/CustomExceptions";
import { useRouter } from 'vue-router';

export const useNotificacaoInstantaneaStore = defineStore('NotificacaoInstantaneaStore', () => {
    const sistemaRepository = new SistemaRepository()
    const notificacaoRepository = new NotificacaoRepository()
    const router = useRouter()
    
    const sistemas = ref([])
    const sistemaSelecionado = ref(0)
    
    const titulo = ref('')
    const descricao = ref('')
    const destinatarios = ref('')

    const tituloErro = ref('')
    const descricaoErro = ref('')
    const destinatariosErro = ref('')
    const sistemaSelecionadoErro = ref('')

    async function enviarNotificacao() {
        if (!dadosValidos()) return;
        try {
            const notificacao = new Notificacao(null, titulo.value, descricao.value, null, [], destinatarios.value)
            const sistema = sistemaSelecionado.value;
            await notificacaoRepository.notificacaoInstantanea(notificacao, sistema)
            router.push('/')
        } catch (erro) {
            if (erro instanceof AuthException) throw new AuthException()
            if (erro instanceof ServerException) throw new ServerException()
        }
    }

    function dadosValidos() {
        let dadosValidos = true
        if (titulo.value === '') {
            tituloErro.value = 'Informa o título da notificação'
            dadosValidos = false
        } else {
            tituloErro.value = ''
        }

        if (descricao.value === '') {
            descricaoErro.value = 'Descreva a notificação'
            dadosValidos = false
        } else {
            descricaoErro.value = ''
        }

        if (destinatarios.value === '') {
            destinatariosErro.value = 'Informe os destinatarios das notificações'
            dadosValidos = false
        } else if (!destinatariosValidos()) {
            destinatariosErro.value = 'Verifique se o destinatário está correto'
            dadosValidos = false
        } else {
            destinatariosErro.value = ''
        }

        if (sistemaSelecionado.value == 0) {
            sistemaSelecionadoErro.value = 'Selecione um sistema'
            dadosValidos = false
        } else {
            sistemaSelecionadoErro.value = ''
        }

        return dadosValidos
    }

    function destinatariosValidos() {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        const emails = destinatarios.value.split(';').map(email => email.trim());
        for (const email of emails) {
            if (!emailPattern.test(email)) {
                return false;
            }
        }

        return true;
    }

    async function buscarSistemas() {
        if (sistemas.value.length > 0) return;

        try {
            const sistemasResponse = await sistemaRepository.buscarSistemas()
            for (const response of sistemasResponse) { sistemas.value.push(response) }
            if (sistemas.value.length > 0) { sistemaSelecionado.value = sistemas.value[0].id }
        } catch (erro) {
            if (erro instanceof AuthException) throw new AuthException()
            if (erro instanceof ServerException) throw new ServerException()
        }
        return;
    }

    return { 
        sistemas,
        buscarSistemas,
        sistemaSelecionado,
        sistemaSelecionadoErro,
        titulo,
        descricao,
        destinatarios,
        tituloErro,
        descricaoErro,
        destinatariosErro,
        enviarNotificacao,
    }

})