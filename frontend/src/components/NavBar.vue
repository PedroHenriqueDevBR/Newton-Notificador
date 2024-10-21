<template>
    <nav class="uk-navbar-container primary-color">
        <div class="uk-container">
            <div uk-navbar>

                <div class="uk-navbar-left">
                    <a class="uk-navbar-item uk-logo on-primary-color-text" href="/" aria-label="Home">
                        <img src="@/assets/images/logo.jpeg" alt="" width="50">
                        Notificador
                    </a>
                </div>


                <div class="uk-navbar-right ">
                    <button class="uk-button uk-button-default on-primary-color-text">Sair</button>
                </div>

            </div>
        </div>
    </nav>
    <div class="primary-color-light subnav">
        <ul class="uk-flex-center" uk-tab>
            <li class="uk-active"><a href="#">Últimos envios</a></li>
            <li><a href="#">Aguardando</a></li>
            <li><a href="#">Sucesso</a></li>
            <li><a href="#">Erro</a></li>
        </ul>
    </div>
</template>

<style>
.subnav {
    padding-top: 8px;
    padding-bottom: none;
}
</style>