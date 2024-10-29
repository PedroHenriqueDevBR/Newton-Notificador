import { defineStore } from "pinia";
import { ref } from "vue";
import SistemaRepository from "@/repositories/SistemaRepository";
import { AuthException, ServerException } from "@/exception/CustomExceptions";

export const useSistemaStore = defineStore('SistemaStore', () => {
    const repository = new SistemaRepository();
    const sistemas = ref([]);
    const indicesSelecionados = ref([]);

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

    function formatarSistemasSelecionados(){
        let selecionados = []
        for (const indice of indicesSelecionados.value) {
            selecionados.push(sistemas.value[indice])
        }
        return selecionados
    }

    function idSelecionados(){
        let selecionados = []
        for (const indice of indicesSelecionados.value) {
            selecionados.push(sistemas.value[indice].id)
        }
        return selecionados
    }

    function selecionarSistema(indice) {
        const posicaoEncontrada = indicesSelecionados.value.indexOf(indice);
        if (posicaoEncontrada > -1) {
            indicesSelecionados.value.splice(posicaoEncontrada, 1);
        } else {
            indicesSelecionados.value.push(indice)
        }
    }

    return { sistemas, buscarSistemas, selecionarSistema, formatarSistemasSelecionados, idSelecionados }

})
