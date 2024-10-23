class AuthRepository {

    constructor() {
        this.urlBase = 'http://localhost:8000'
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

        if (response.status >= 200 && response.status < 300) {
            const json = await response.json()
            this.salvarCredenciais(json.access, json.refresh)
            return true
        }
        return false
    }

    async token() {
        return await localStorage.getItem(this.access_key)
    }

    atualizarAccess(access) {
        localStorage.setItem(this.access_key, access)
    }

    salvarCredenciais(access, refresh) {
        localStorage.setItem(this.access_key, access)
        localStorage.setItem(this.refresh_key, refresh)
    }

    limparToken() {
        localStorage.removeItem(this.access_key)
        localStorage.removeItem(this.refresh)
    }
}

export default AuthRepository