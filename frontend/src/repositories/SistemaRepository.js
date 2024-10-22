import SistemaModel from "@/models/SistemaModel";

class SistemaRepository {
    constructor() { }

    async buscarSistemas() {
        await new Promise(resolve => {
            setTimeout(() => {
                console.log('Tempo fake');
                resolve();
            }, 500)
        })

        return [
            new SistemaModel(1, 'Sistema 01'),
            new SistemaModel(2, 'Sistema 02'),
            new SistemaModel(3, 'Sistema 03'),
            new SistemaModel(4, 'Sistema 04'),
            new SistemaModel(5, 'Sistema 05'),
        ]
    }
}

export default SistemaRepository;