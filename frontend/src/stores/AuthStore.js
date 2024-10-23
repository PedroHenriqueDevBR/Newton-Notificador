import { ref } from "vue";
import { defineStore } from "pinia";
import AuthRepository from "@/repositories/AuthRepository";

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
        const response = await repository.autenticar(username, password)
        if (response == true) {
            logado.value = true
        } else {
            logado.value = false
        }
    }

    function encerrarSessao() {
        repository.limparToken()
        this.logado = false
    }

    verificarToken();

    return { autenticar, encerrarSessao, logado, verificarToken }
})