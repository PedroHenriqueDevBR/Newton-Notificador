<script setup>
import { RouterLink } from 'vue-router';
import NotificacaoItem from './NotificacaoItem.vue';
</script>

<template>
    <h2>Notificações</h2>
    <dl class="uk-description-list">
        <RouterLink to="detalhes">
            <NotificacaoItem />
        </RouterLink>
        <RouterLink to="detalhes">
            <NotificacaoItem />
        </RouterLink>
        <RouterLink to="detalhes">
            <NotificacaoItem />
        </RouterLink>
        <RouterLink to="detalhes">
            <NotificacaoItem />
        </RouterLink>
        <RouterLink to="detalhes">
            <NotificacaoItem />
        </RouterLink>
        <RouterLink to="detalhes">
            <NotificacaoItem />
        </RouterLink>
    </dl>
</template>

<style scoped></style>
