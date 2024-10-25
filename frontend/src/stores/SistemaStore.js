import { defineStore } from "pinia";
import { ref } from "vue";
import SistemaRepository from "@/repositories/SistemaRepository";
import { AuthException, ServerException } from "@/exception/CustomExceptions";

export const useSistemaStore = defineStore('SistemaStore', () => {
    const sistemas = ref([]);
    const repository = new SistemaRepository();

    async function buscarSistemas() {
        if (sistemas.value.length > 0) return;


        try {
            const sistemasResponse = await repository.buscarSistemas()
            for (const response of sistemasResponse) { sistemas.value.push(response) }
        } catch (erro) {
            if (erro instanceof AuthException) throw new AuthException()
            if (erro instanceof ServerException) throw new ServerException()
        }
        return;
    }

    return { sistemas, buscarSistemas }

})