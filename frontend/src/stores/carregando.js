import { ref } from "vue";
import { defineStore } from "pinia";

export const useCarregandoStore = defineStore('carregando Store', () => {
    const carregando = ref(false)

    function alterarStatus(valor) {
        carregando.value = valor
    }

    function estaCarregando() {
        return carregando.value
    }

    return {carregando, alterarStatus, estaCarregando}
});