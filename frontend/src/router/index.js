import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AuthView from '@/views/AuthView.vue'
import NotificacaoInstantanea from '@/views/NotificacaoInstantanea.vue'
import AgendarNotificacao from '@/views/AgendarNotificacao.vue'
import DetalhesNotificacao from '@/views/DetalhesNotificacao.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/auth',
      name: 'auth',
      component: AuthView,
    },
    {
      path: '/detalhes',
      name: 'detalhes',
      component: DetalhesNotificacao,
    },
    {
      path: '/notificar',
      name: 'notificar',
      component: NotificacaoInstantanea,
    },
    {
      path: '/notificar/agendar',
      name: 'agendar-notificacao',
      component: AgendarNotificacao,
    },
  ],
})

export default router
