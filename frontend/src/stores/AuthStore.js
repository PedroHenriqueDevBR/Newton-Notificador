import { ref } from "vue";
import { defineStore } from "pinia";
import AuthRepository from "@/repositories/AuthRepository";
import { AuthException, ServerException } from "@/exception/CustomExceptions";

export const useAuthStore = defineStore('AuthStore', () => {
    const logado = ref(false)
    const repository = new AuthRepository()

    async function verificarToken() {
        const token = await repository.token()
        if (token != null) {
            logado.value = true
        } else {
            logado.value = false
        }
        return logado.value
    }

    async function autenticar(username, password) {
        try {
            const response = await repository.autenticar(username, password)

            if (response == true) {
                logado.value = true
            } else {
                logado.value = false
            }
        } catch(erro) {
            if (erro instanceof AuthException) throw new AuthException()
            if (erro instanceof ServerException) throw new ServerException()
            throw new ServerException()
        }
    }

    function encerrarSessao() {
        repository.limparToken()
        this.logado = false
    }

    return { autenticar, encerrarSessao, logado, verificarToken }
})