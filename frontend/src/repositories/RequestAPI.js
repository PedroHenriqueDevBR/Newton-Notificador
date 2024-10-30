import { AuthException, NotFoundException, ServerException } from "@/exception/CustomExceptions"
import AuthRepository from "./AuthRepository"

export default class RequestApi {

    constructor() {
        this.urlBase = import.meta.env.VITE_APP_API_URL
        this.authRepository = new AuthRepository()
    }

    async get(path, tentativas = 0) {
        const url = this.urlBase + path
        const token = await this.authRepository.token()
        const response = await fetch(url, {
            headers: { 'Content-Type': 'application/json', 'Authorization': token }
        })

        if (response.status == 401 && tentativas > 0) throw new AuthException()
        if (response.status == 401 && tentativas == 0) {
            const sucesso = await this.authRepository.atualizarAccessToken()
            if (!sucesso) throw new AuthException()
            return this.get(path, ++tentativas)
        }
        if (response.status == 404) throw new NotFoundException()
        if (response.status >= 500) throw new ServerException()
        if (response.status >= 200 && response.status < 300) return await response.json()

        return null
    }

    async post(path, body, tentativas = 0) {
        const url = this.urlBase + path
        const token = await this.authRepository.token()
        const response = await fetch(url, {
            method: 'POST', body: JSON.stringify(body), headers: { 'Content-Type': 'application/json', 'Authorization': token }
        })

        if (response.status == 401 && tentativas > 0) throw new AuthException()
        if (response.status == 401 && tentativas == 0) {
            const sucesso = this.authRepository.atualizarAccessToken()
            if (!sucesso) throw new AuthException()
            return this.post(path, body, ++tentativas)
        }
        if (response.status == 404) throw new NotFoundException()
        if (response.status >= 500) throw new ServerException()
        if (response.status >= 200 && response.status < 300) return await response.json()

        return null
    }
}