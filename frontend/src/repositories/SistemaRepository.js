import SistemaModel from "@/models/SistemaModel";
import RequestApi from "./RequestAPI";
import { AuthException, ServerException } from "@/exception/CustomExceptions";

class SistemaRepository {
    constructor() {
        this.requester = new RequestApi()
    }

    async buscarSistemas() {
        const url = '/api/v1/sistemas'
        try {
            const dados = await this.requester.get(url)
            console.log(dados)

            const sistemas = []
            for (const dado of dados) {
                sistemas.push(new SistemaModel(dado.id, dado.first_name))
            }
            return sistemas
        }
        catch (erro) {
            if (erro instanceof AuthException) throw new AuthException()
            if (erro instanceof ServerException) throw new ServerException()
        }

        return []

    }
}

export default SistemaRepository;