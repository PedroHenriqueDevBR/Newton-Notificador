<script setup>

import { RouterLink } from 'vue-router';
</script>

<template>
    <h2>Opções</h2>

    <div class="uk-card uk-card-body uk-background-muted">
        <form>
            <fieldset class="uk-fieldset">

                <legend class="uk-legend">Sistemas</legend>

                <div class="uk-margin uk-grid-small uk-child-width-auto uk-grid">
                    <label><input class="uk-checkbox" type="checkbox" checked> Sistema 01</label>
                    <label><input class="uk-checkbox" type="checkbox"> Sistema 02</label>
                    <label><input class="uk-checkbox" type="checkbox"> Sistema 03</label>
                    <label><input class="uk-checkbox" type="checkbox"> Sistema 04</label>
                    <label><input class="uk-checkbox" type="checkbox"> Sistema 05</label>
                    <label><input class="uk-checkbox" type="checkbox"> Sistema 06</label>
                    <label><input class="uk-checkbox" type="checkbox"> Sistema 07</label>
                    <label><input class="uk-checkbox" type="checkbox"> Sistema 08</label>
                    <label><input class="uk-checkbox" type="checkbox"> Sistema 09</label>
                </div>
            </fieldset>
            <button class="uk-button uk-button-primary">Filtrar</button>
        </form>

        <hr class="uk-divider-icon">

        <RouterLink to="notificar" class="uk-button uk-button-default uk-width-1-1 uk-margin-small-bottom">
            Notificação instantânea
        </RouterLink>
        <RouterLink to="notificar/agendar" class="uk-button uk-button-default uk-width-1-1 uk-margin-small-bottom">
            Agendar notificação
        </RouterLink>

    </div>
</template>

<style scoped></style>
