import './assets/css/main.css'
import './assets/css/uikit.min.css'
import './assets/js/uikit.min.js'
import './assets/js/uikit-icons.min.js'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

// Quill RichText
// import { QuillEditor } from '@vueup/vue-quill'
// import '@vueup/vue-quill/dist/vue-quill.snow.css';

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

// Quill RichText
// app.component('QuillEditor', QuillEditor)

app.mount('#app')
