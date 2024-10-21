import './assets/css/main.css'
import './assets/css/uikit.min.css'
import './assets/js/uikit.min.js'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
