<script setup>
import { useCarregandoStore } from '@/stores/carregando';
import { useNotificacaoStore } from '@/stores/NotificacaoStore';

const notificacaoStore = useNotificacaoStore()
const carregandoStore = useCarregandoStore()

async function carregarNotificacoes(status) {
  carregandoStore.alterarStatus(true)
  notificacaoStore.statusSelecionado = status

  try {
      await notificacaoStore.carregarLista()
  } catch (erro) {
      if (erro instanceof AuthException) router.push('/auth')
      if (erro instanceof ServerException) alert('Sem conexão com o servidor!')
  } finally {
    carregandoStore.alterarStatus(false)
  }
}
</script>

<template>
  <nav class="uk-navbar-container primary-color">
    <div class="uk-container">
      <div uk-navbar>
        <div class="uk-navbar-left">
          <a
            class="uk-navbar-item uk-logo on-primary-color-text"
            href="/"
            aria-label="Home"
          >
            <img src="@/assets/images/logo.jpeg" alt="" width="50" />
            Notificador
          </a>
        </div>

        <div class="uk-navbar-right">
          <button class="uk-button uk-button-default on-primary-color-text">
            Sair
          </button>
        </div>
      </div>
    </div>
  </nav>
  <div class="primary-color-light subnav">
    <ul class="uk-flex-center" uk-tab>
      <li class="uk-active"><a @click="carregarNotificacoes('')">Últimos envios</a></li>
      <li><a @click="carregarNotificacoes('1')">Aguardando</a></li>
      <li><a @click="carregarNotificacoes('2')">Sucesso</a></li>
      <li><a @click="carregarNotificacoes('3')">Erro</a></li>
    </ul>
  </div>
</template>

<style>
.subnav {
  padding-top: 8px;
  padding-bottom: none;
}
</style>
