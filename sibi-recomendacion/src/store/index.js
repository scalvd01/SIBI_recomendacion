import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    logueado: false,
    currentPhone: null,
    currentUser: null,
  },
  mutations: {
    changeStateLogueado(state) {
      state.logueado = !state.logueado;
      console.log("Estado logueado", state.logueado);
    },
    setStateLogueado(state, data) {
      state.logueado = data;
      console.log("Estado logueado", state.logueado);
    },
    setCurrentPhone(state, data) {
      state.currentPhone = data;
      console.log("current coleccion", state.currentPhone);
    },
    setCurrentUser(state, data) {
      console.log(data)
      state.currentUser = data;
      console.log("Current usuario", state.currentUser.nombre);
    },
  },
  actions: {
    //llamamos con el dispatch
    changeStateLogueadoAction(context) {
      context.commit("changeStateLogueado");
    },
    setStateLogueadoAction(context, data) {
      context.commit("setStateLogueado", data);
    },
    setCurrentPhoneAction(context, data) {
      context.commit("setCurrentPhone", data); //a mutations
    },
    setCurrentUserAction(context, data) {
      context.commit("setCurrentUser", data);
    },
  },
  getters: {
    logueado(state) {
      return state.logueado;
    },
    currentPhone(state) {
      return state.currentPhone;
    },
    currentUser(state) {
      return state.currentUser;
    },
  },
  modules: {
  }
})
