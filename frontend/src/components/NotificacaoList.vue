<script setup>
import { RouterLink } from 'vue-router';
import NotificacaoItem from './NotificacaoItem.vue';
</script>

<template>
    <h2>Notificações</h2>
    <dl class="uk-description-list">
        <RouterLink to="detalhes" class="remove-decoration">
            <NotificacaoItem />
        </RouterLink>
        <RouterLink to="detalhes" class="remove-decoration">
            <NotificacaoItem />
        </RouterLink>
        <RouterLink to="detalhes" class="remove-decoration">
            <NotificacaoItem />
        </RouterLink>
        <RouterLink to="detalhes" class="remove-decoration">
            <NotificacaoItem />
        </RouterLink>
        <RouterLink to="detalhes" class="remove-decoration">
            <NotificacaoItem />
        </RouterLink>
        <RouterLink to="detalhes" class="remove-decoration">
            <NotificacaoItem />
        </RouterLink>
    </dl>
</template>

<style scoped>
.remove-decoration {
    text-decoration: none !important;
    color: inherit;
}
</style>
