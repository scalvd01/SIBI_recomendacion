<template>
  <v-main>
    <!---->

    <v-toolbar flat>
      <v-toolbar-title>
        <v-card flat color="transparent" router to="/">
          <!--<h1 class="font-weight-light">Phone REC·</h1>-->
          <v-img src="../../public/st1Recurso1.png" width="310"> </v-img>
        </v-card>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <!---->
      <!--
      <v-autocomplete
        v-model="values"
        :items="listatels"
        dense
        rounded
        clearable
        solo-inverted
        label="Buscar"
      ></v-autocomplete>-->

      <v-menu
        v-if="$store.getters.logueado"
        rounded="b-lg"
        offset-y
        transition="scroll-y-transition"
      >
        <template v-slot:activator="{ attrs, on }">
          <v-btn
            text
            v-bind="attrs"
            v-on="on"
            height="60"
            outlined
            class="overflow-x-visible mt-2"
            ><v-avatar>
              <img src="https://thispersondoesnotexist.com/image" />
            </v-avatar>
            <div class="d-flex justify-center">
              <h1 class="font-weight-light">
                {{ $store.getters.currentUser.nombre }}
              </h1>
            </div>
          </v-btn>
        </template>

        <v-list>
          <v-list-item link router to="/">
            <v-list-item-title> Inicio </v-list-item-title>
          </v-list-item>
          <v-list-item link router to="/MiPerfil">
            <v-list-item-title> Perfil </v-list-item-title>
          </v-list-item>
          <v-list-item link router to="/Todo">
            <v-list-item-title> Todo </v-list-item-title>
          </v-list-item>
          <v-list-item link>
            <v-list-item-title
              @click="
                changeStateLogueado();
                resetCurrentUser();
              "
            >
              <span>Log Out</span>
              <v-icon right color="red">mdi-logout-variant</v-icon>
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-btn
        v-if="!$store.getters.logueado"
        absolute
        right
        color="primary"
        router
        to="/Login"
      >
        <span>Sign In</span>
        <v-icon right>mdi-login-variant</v-icon>
      </v-btn>

      <template v-slot:extension>
        <v-tabs centered slider-color="blue">
          <v-tab router to="/"> inicio </v-tab>
          <v-tab router to="/Todo"> Todo </v-tab>
          <v-tab router to="/MiPerfil" v-if="$store.getters.logueado">
            perfil
          </v-tab>
        </v-tabs>
      </template>
    </v-toolbar>

    <!--  -->
  </v-main>
</template>

<script>
//import store from "../store";
export default {
  data: () => ({
    listaTels: [],
  }),
  computed: {},
  methods: {
    changeStateLogueado() {
      this.$store.dispatch("changeStateLogueadoAction");
      this.$router.push({ path: "/" });
      console.log("metodo de navbar");
    },
    resetCurrentUser() {
      console.log("Current user reseteado");
      this.$store.dispatch("setCurrentUserAction", null);
    },
  },
};
</script>
