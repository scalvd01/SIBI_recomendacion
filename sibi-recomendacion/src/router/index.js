import Vue from "vue";
import VueRouter from "vue-router";
//import Home from '../views/Home.vue'
import Principal from "../views/Principal.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Principal",
    component: () => import("../views/Principal.vue"),
  },
  {
    path: "/Login",
    name: "Login",

    component: () => import("../views/Login.vue"),
  },
  {
    path: "/Registro",
    name: "Registro",

    component: () => import("../views/Registro.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
