<template>
  <v-container fluid class="pa-8">
    <h1>Mi Perfil</h1>
    <h3 class="pb-2" id="puntos"> Saldo de puntos: {{ $store.getters.currentUser.saldoPuntos }}</h3>
    <br />
    <h3>Mis Álbumes:</h3>

    <!---->
    <v-row>
      <v-col v-for="(album, i) in usuario.colecciones" :key="i" cols="4">
        <v-card max-width="344">
          <v-img :src="album.album.imagen" class="mx-2"></v-img>

          <v-card-title> {{ album.album.nombre }} </v-card-title>
        </v-card>
      </v-col>
    </v-row>
    <br />
    <h3>Mis cartas:</h3>

    <v-row>
      <v-col v-for="(carta, i) in cartas" :key="i" cols="2">
        <v-card max-width="250">
          <v-img :src="carta.imagen" class="mx-2"></v-img>

          <v-card-title> {{ carta.nombre }} </v-card-title>
        </v-card>
      </v-col></v-row
    >
  </v-container>
</template>

<!-- -->

<script>
export default {
  name: "Principal",

  mounted() {
    //this.cargarPuntos();
    this.cargarSocio();
    this.separar();
    this.$store.dispatch("setStateLogueadoAction", true);
  },

  data: () => ({
    puntos: 0,
    albumes: [],
    cartas:  [],
    usuario: null,
  }),
  methods: {
    separar: function() {
      this.usuario.colecciones.forEach((coleccion) => {
        this.albumes.push(coleccion.album)

        coleccion.cartas.forEach(carta => {
          this.cartas.push(carta)
        });
      });
    },

    cargarSocio: function() {
      var self = this;
      //traemos al socio
      var xhttp1 = new XMLHttpRequest();
      var url = "http://localhost:5000/baseDatos/traerUsrLoggeado";
      xhttp1.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          var user = JSON.parse(this.responseText);

          console.log("Current usuario", user);

          self.$store.dispatch("setCurrentUserAction", user);
          console.log("Guardado current user desde miperfil");

          self.usuario = user;
        }
      };

      xhttp1.open("GET", url, false);
      xhttp1.send();
    },
  },
};
</script>
