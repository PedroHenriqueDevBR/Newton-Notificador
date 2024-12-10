export class AuthException extends Error {
    constructor() {
        super('');
        this.name = this.constructor.name;
    }
}

export class NotFoundException extends Error {
    constructor() {
        super('');
        this.name = this.constructor.name;
    }
}

export class ServerException extends Error {
    constructor() {
        super('');
        this.name = this.constructor.name;
    }
}
