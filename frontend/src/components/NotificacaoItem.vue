<script setup>
import Notificacao from '@/models/NotificacaoModel';


defineProps({
  notificacao: Notificacao
})

</script>

<template>
  <div class="uk-card uk-card-body uk-background-muted uk-card-hover uk-padding-small uk-margin-small">
    <dt>{{ notificacao.titulo }}</dt>
    <dd>{{ notificacao.descricao }}</dd>
    <span v-for="status of notificacao.lista_status" class="aguardando" :class="['uk-badge uk-margin-small-right', status]">{{ status }}</span>
  </div>
</template>

<style scoped>
.aguardando, .Recebido {
  background-color: #039be5;
}

.erro, .Erro {
  background-color: #d32f2f;
}

.enviado, .Enviado {
  background-color: #689f38;
}
</style>
