<template>
  <v-app>
    <v-main>
      <v-container fluid class="pa-8">
        <div class="mt-8 mx-9">
          <h3>Mis datos:</h3>
          <div class="d-flex pl-1 py-3">
            <v-card
              ><div class="ma-3">
                Nombre: {{ usuario.nombre }} <br />
                Apellidos: {{ usuario.apellidos }}<br />
                Usuario: {{ usuario.usuario }}
              </div>
            </v-card>
          </div>
          <h3 class="mb-4">Mis favoritos:</h3>

          <!---->
          <v-slide-group show-arrows>
            <v-slide-item v-for="(d, i) in favs" :key="i">
              <v-card class="ma-2">
                <v-img
                  :src="d.picture"
                  class="mt-1"
                  height="250"
                  contain
                ></v-img>

                <v-card-title> {{ d.name }} </v-card-title>
                <div class="d-flex justify-center pb-3">
                  <v-btn
                    color="success"
                    text
                    elevation="1"
                    @click="irASmartPhone(d)"
                  >
                    ver teléfono
                  </v-btn>
                </div>
              </v-card>
            </v-slide-item>
          </v-slide-group>
          <br />

          <h3 class="mb-4">Historial:</h3>

          <v-slide-group show-arrows>
            <v-slide-item v-for="(d, i) in historial" :key="i">
              <v-card class="ma-2">
                <v-img
                  :src="d.picture"
                  class="mt-1"
                  height="250"
                  contain
                ></v-img>

                <v-card-title> {{ d.name }} </v-card-title>
                <div class="d-flex justify-center pb-3">
                  <v-btn
                    color="success"
                    text
                    elevation="1"
                    @click="irASmartPhone(d)"
                  >
                    ver teléfono
                  </v-btn>
                </div>
              </v-card>
            </v-slide-item>
          </v-slide-group>

          <!--<v-row>
            <v-col v-for="(d, i) in historial" :key="i" cols="2">
              <v-card max-width="250">
                <v-img :src="d.picture" class="mx-2"></v-img>

                <v-card-title> {{ d.name }} </v-card-title>
                <div class="d-flex justify-center pb-3">
                  <v-btn
                    color="success"
                    text
                    elevation="1"
                    @click="irASmartPhone(d)"
                  >
                    ver teléfono
                  </v-btn>
                </div>
              </v-card>
            </v-col></v-row
          >-->
        </div>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "MiPerfil",

  mounted() {
    this.getDatos();
  },

  data: () => ({
    usuario: [],
    favs: [],
    historial: [],
  }),
  methods: {
    getDatos: function () {
      var user = this.$store.getters.currentUser;
      this.usuario = user;
      this.favs = user.favoritos;
      console.table(this.favs, ["me_gusta", "device_score", "name"]);
      this.historial = user.historial;
    },
    irASmartPhone: function (SmartPhone) {
      console.log("yendo al smartphone");
      //console.log(SmartPhone);
      this.$store.dispatch("setCurrentPhoneAction", SmartPhone);
      this.$router.push({ path: "/SmartPhone" });
      //console.log(this.$store.getters.currentPhone);
    },
  },
};
</script>
