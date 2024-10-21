<script setup></script>

<template>
    <div class="uk-card uk-card-body uk-background-muted uk-card-hover uk-padding-small uk-margin-small">
        <dt>Description term</dt>
        <dd>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</dd>
        <span class="uk-badge uk-margin-small-right aguardando">Aguardando</span>
        <span class="uk-badge uk-margin-small-right erro">Erro</span>
        <span class="uk-badge uk-margin-small-right enviado">Enviado</span>
    </div>
</template>

<style scoped>
.aguardando {
    background-color: #039be5;
}

.erro {
    background-color: #d32f2f;
}

.enviado {
    background-color: #689f38;
}
</style>
