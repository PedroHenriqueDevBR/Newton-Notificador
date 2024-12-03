<script setup>
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'
import { useNotificacaoInstantaneaStore } from '@/stores/NotificacaoInstantaneaStore';

import { RouterLink } from 'vue-router'
import { onMounted } from 'vue';

const notificacaoStore = useNotificacaoInstantaneaStore()

async function carregarDados() {
    try {
        await notificacaoStore.buscarSistemas()
    } catch (erro) {
        if (erro instanceof AuthException) router.push('/auth')
        if (erro instanceof ServerException) alert('Sem conexão com o servidor!')
    } finally {
        carregandoStore.alterarStatus(false);
    }
}

onMounted(() => { carregarDados() })

</script>

<template>
  <main class="uk-padding">
    <div class="uk-container uk-card uk-card-body uk-background-muted">
      <h1>
        <RouterLink
          to="/"
          class="uk-margin-small-right"
          uk-icon="icon: arrow-left; ratio: 2"
        ></RouterLink>
        Notificação Instantânea
      </h1>
      <hr class="uk-divider-small" />

      <form class="uk-form-stacked">
        <div class="uk-margin">
          <label class="uk-form-label" for="form-stacked-text"
            >Destinatário:</label
          >
          <div class="uk-form-controls">
            <input
              class="uk-input"
              id="form-stacked-text"
              type="text"
              placeholder="usuario@emai.com"
            />
          </div>
        </div>

        <div class="uk-margin">
          <label class="uk-form-label" for="form-stacked-text">Título</label>
          <div class="uk-form-controls">
            <input
              class="uk-input"
              id="form-stacked-text"
              type="text"
              placeholder="Título do envio"
            />
          </div>
        </div>

        <div class="uk-margin">
          <label class="uk-form-label" for="form-stacked-text">Sistema</label>
          <div class="uk-form-controls">
            <select class="uk-select" aria-label="Select">
              <option v-for="sistema of notificacaoStore.sistemas" :value="sistema.id">{{ sistema.nome }}</option>
            </select>
          </div>
        </div>

        <div class="uk-margin">
          <QuillEditor theme="snow" style="height: 500px" />
        </div>

        <hr class="uk-divider-small" />
        <RouterLink to="/" class="uk-button uk-button-default"
          >Cancelar</RouterLink
        >
        <button class="uk-button uk-button-primary">Enviar</button>
      </form>
    </div>
  </main>
</template>

<style scoped></style>
