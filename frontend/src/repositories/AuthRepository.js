import { AuthException, ServerException, NotFoundException } from "@/exception/CustomExceptions"

class AuthRepository {

    constructor() {
        this.urlBase = import.meta.env.VITE_APP_API_URL
        this.access_key = 'ACCESS_KEY'
        this.refresh_key = 'REFRESH_KEY'
    }

    async autenticar(username, password) {
        const url = this.urlBase + '/api/v1/auth/token'
        const body = {
            "username": username,
            "password": password
        }

        const response = await fetch(url, {
            method: 'POST', body: JSON.stringify(body), headers: { 'Content-Type': 'application/json' }
        })

        if (response.status == 401) throw new AuthException()
        if (response.status == 404) throw new NotFoundException()
        if (response.status >= 500) throw new ServerException()
        if (response.status >= 200 && response.status < 300) {
            const json = await response.json()
            this.salvarCredenciais(json.access, json.refresh)
            return true
        }

        return false
    }

    async atualizarAccessToken() {
        const url = this.urlBase + '/api/v1/auth/refresh'
        const refresh = await this.refreshToken()
        const body = { "refresh": refresh }

        const response = await fetch(url, {
            method: 'POST', body: JSON.stringify(body), headers: { 'Content-Type': 'application/json' }
        })

        if (response.status >= 200 && response.status < 300) {
            const json = await response.json()
            this.salvarNovoAccessToken(json.access)
            return true
        }

        this.limparToken()
        return false
    }

    salvarNovoAccessToken(access) {
        localStorage.setItem(this.access_key, access)
    }

    async token() {
        const token = await localStorage.getItem(this.access_key)
        return 'Bearer ' + token
    }

    async refreshToken() {
        return await localStorage.getItem(this.refresh_key)
    }

    salvarCredenciais(access, refresh) {
        localStorage.setItem(this.access_key, access)
        localStorage.setItem(this.refresh_key, refresh)
    }

    limparToken() {
        localStorage.removeItem(this.access_key)
        localStorage.removeItem(this.refresh_key)
    }
}

export default AuthRepository