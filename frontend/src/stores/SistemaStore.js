import { defineStore } from "pinia";
import { ref } from "vue";
import SistemaRepository from "@/repositories/SistemaRepository";

export const useSistemaStore = defineStore('SistemaStore', () => {
    const sistemas = ref([]);
    const repository = new SistemaRepository();

    async function buscarSistemas() {
        if (sistemas.value.length > 0) return;
        const sistemasResponse = await repository.buscarSistemas()
        for (const response of sistemasResponse) { sistemas.value.push(response) }
    }

    return { sistemas, buscarSistemas }

})