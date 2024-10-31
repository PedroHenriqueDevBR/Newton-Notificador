import { ref } from "vue";
import { defineStore } from "pinia";
import NotificacaoRepository from "@/repositories/NotificacaoRepository";

const useEnviarNotificacaoStore = defineStore('Enviar Notificacao', () => {

    const dataAgendamento = ref('')
    const horaAgendamento = ref('')
    const notificacaoRepository = NotificacaoRepository()

    const titulo = ref('')
    const descricao = ref('')
    const destinatarios = ref('')

    const tituloErro = ref('')
    const descricaoErro = ref('')
    const destinatariosErro = ref('')

    function enviarNotificacao() {
        if (!dadosValidos()) return
        // TODO: Implementar
    }

    function dadosValidos() {
        let dadosValidos = true
        if (titulo.value.length === 0) {
            tituloErro.value = 'Informa o título da notificação'
            dadosValidos = false
        } else {
            tituloErro.value = ''
        }

        if (descricao.value.length === 0) {
            descricaoErro.value = 'Descreva a notificação'
            dadosValidos = false
        } else {
            descricaoErro.value = ''
        }

        if (destinatarios.value.length === 0) {
            destinatariosErro.value = 'Informe os destinatarios das notificações'
            dadosValidos = false
        } else if (destinatariosValidos()) {
            destinatariosErro.value = 'Verifique se o destinatário está correto'
            dadosValidos = false
        } else {
            destinatariosErro.value = ''
        }

        return dadosValidos
    }

    function destinatariosValidos() {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        const emails = destinatarios.value.split(';').map(email => email.trim());
        return emails.every(email => emailPattern.test(email));
    }
    
})