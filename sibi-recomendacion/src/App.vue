<template>
  <v-app app>
    <navbar />

    <v-main class="mx-2 mb-4 pt-0">
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import Navbar from "./components/Navbar.vue";

import store from "./store";

export default {
  components: { Navbar },
  name: "App",
  store,
};
</script>
