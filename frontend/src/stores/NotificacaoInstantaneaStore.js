import { ref } from "vue";
import SistemaRepository from "@/repositories/SistemaRepository";
import { defineStore } from "pinia";

export const useNotificacaoInstantaneaStore = defineStore('NotificacaoInstantaneaStore', () => {
    const sistemaRepository = new SistemaRepository();
    const sistemas = ref([])

    async function buscarSistemas() {
        if (sistemas.value.length > 0) return;

        try {
            const sistemasResponse = await sistemaRepository.buscarSistemas()
            for (const response of sistemasResponse) { sistemas.value.push(response) }
        } catch (erro) {
            if (erro instanceof AuthException) throw new AuthException()
            if (erro instanceof ServerException) throw new ServerException()
        }
        return;
    }

    return { sistemas, buscarSistemas }

})