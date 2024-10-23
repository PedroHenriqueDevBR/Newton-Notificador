import SistemaModel from "@/models/SistemaModel";
import AuthRepository from "./AuthRepository";

class SistemaRepository {
    constructor() {
        this.urlBase = 'http://localhost:8000'
        this.authRepository = new AuthRepository()
    }

    async buscarSistemas() {
        const url = this.urlBase + '/api/v1/sistemas'
        const token = await this.authRepository.token()
        const response = await fetch(url, {
            headers: { 'Content-Type': 'application/json', 'Authorization': token }
        })

        if (response.status >= 200 && response.status < 300) {
            const sistemas = []
            const dados = await response.json()
            for (const dado of dados) {
                sistemas.push(new SistemaModel(dado.id, dado.first_name))
            }
            return sistemas
        }
        return []
    }
}

export default SistemaRepository;