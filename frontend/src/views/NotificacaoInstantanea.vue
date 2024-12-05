<script setup>
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'
import { useNotificacaoInstantaneaStore } from '@/stores/NotificacaoInstantaneaStore';

import { RouterLink } from 'vue-router'
import { onMounted } from 'vue';

const notificacaoStore = useNotificacaoInstantaneaStore()

async function enviarNotificacao() {
    if (!dadosValidos()) return;
    try {
        const notificacao = new Notificacao(null, titulo.value, descricao.value, null, [], destinatarios.value)
        const sistema = sistemaSelecionado.value;
        const response = await notificacaoRepository.notificacaoInstantanea(notificacao, sistema)
        console.log(response)
    } catch (erro) {
        if (erro instanceof AuthException) throw new AuthException()
        if (erro instanceof ServerException) throw new ServerException()
    }
}


async function carregarDados() {
    try {
        await notificacaoStore.buscarSistemas()
    } catch (erro) {
        if (erro instanceof AuthException) router.push('/auth')
        if (erro instanceof ServerException) alert('Sem conexão com o servidor!')
    } finally {
        // carregandoStore.alterarStatus(false);
        console.log('Dados carregados')
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
              :class="['uk-input', {'uk-form-danger': notificacaoStore.destinatariosErro != ''}]"
              id="form-stacked-text"
              type="text"
              placeholder="usuario@emai.com"
              v-model="notificacaoStore.destinatarios"
            />
            <span class="uk-text-meta uk-text-danger">{{ notificacaoStore.destinatariosErro }}</span>
          </div>
        </div>

        <div class="uk-margin">
          <label class="uk-form-label" for="form-stacked-text">Título</label>
          <div class="uk-form-controls">
            <input
              :class="['uk-input', {'uk-form-danger': notificacaoStore.tituloErro != ''}]"
              id="form-stacked-text"
              type="text"
              placeholder="Título do envio"
              required
              v-model="notificacaoStore.titulo"
            />
            <span class="uk-text-meta uk-text-danger">{{ notificacaoStore.tituloErro }}</span>
          </div>
        </div>

        <div class="uk-margin">
          <label class="uk-form-label" for="form-stacked-text">Sistema</label>
          <div class="uk-form-controls">
            <select class="uk-select" aria-label="Select" required v-model="notificacaoStore.sistemaSelecionado">
              <option v-for="sistema of notificacaoStore.sistemas" :key="sistema.id" :value="sistema.id">{{ sistema.nome }}</option>
            </select>
            <span class="uk-text-meta uk-text-danger">{{ notificacaoStore.sistemaSelecionadoErro }}</span>
          </div>
        </div>

        <div class="uk-margin">
          <quill-editor theme="snow" style="height: 500px" v-model:content="notificacaoStore.descricao" content-type="html" />
        </div>

        <hr class="uk-divider-small" />
        <RouterLink to="/" class="uk-button uk-button-default"
          >Cancelar</RouterLink
        >
        <button type="button" v-on:click="notificacaoStore.enviarNotificacao()" class="uk-button uk-button-primary">Enviar</button>
      </form>
    </div>
  </main>
</template>

<style scoped></style>
