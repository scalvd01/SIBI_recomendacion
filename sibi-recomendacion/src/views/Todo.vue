<template>
  <v-app>
    <v-main>
      <div class="mt-8 mx-9">
        <div>
          <div
            class="d-flex align-start mb-6"
            color="grey lighten-2"
            flat
            height="100"
            tile
          >
            <div class="pa-2" outlined tile>
              <div>
                <v-expansion-panels>
                  <v-expansion-panel>
                    <v-expansion-panel-header class="font-weight-medium">
                      Orden
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <div>
                        <v-btn color="success" text @click="ordenar(0, 'score')"
                          >Mejores primero</v-btn
                        >
                      </div>
                      <div>
                        <v-btn
                          color="success"
                          text
                          @click="ordenar(0, 'me_gusta')"
                          >Con más "me gusta" primero</v-btn
                        >
                      </div></v-expansion-panel-content
                    > </v-expansion-panel
                  ><v-expansion-panel>
                    <v-expansion-panel-header class="font-weight-medium">
                      Marca
                    </v-expansion-panel-header>

                    <v-expansion-panel-content>
                      <div v-for="(marca, i) in marcas" :key="i">
                        <v-btn
                          color="success"
                          text
                          @click="ordenar(marca.brand_name, 'marca')"
                          >{{ marca.brand_name }}</v-btn
                        >
                      </div></v-expansion-panel-content
                    >
                  </v-expansion-panel>
                </v-expansion-panels>
              </div>
            </div>
            <div class="pa-2" outlined tile>
              <v-row>
                <v-col v-for="(d, i) in mostrar" :key="i" cols="2">
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
                      <v-icon color="red">mdi-cards-heart-outline</v-icon>
                      <span class="pt-2">{{ d.me_gusta }}</span>
                    </div>
                  </v-card>
                </v-col></v-row
              >
            </div>
          </div>
        </div>
      </div>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "Todo",

  mounted() {
    this.cargar();
  },

  data: () => ({
    mostrar: [],
    todos: [],
    marcas: [],
  }),
  methods: {
    peticion: function (query) {
      var request = new XMLHttpRequest();

      request.open("POST", "http://localhost:5000/runQuery", false); // `false` makes the request synchronous
      request.setRequestHeader("Access-Control-Allow-Headers", "*");
      request.setRequestHeader(
        "Content-type",
        "application/json; charset=utf-8"
      );
      request.setRequestHeader("Access-Control-Allow-Origin", "*");
      request.send(JSON.stringify({ query: query }));

      if (request.status === 200) {
        var data = JSON.parse(request.responseText);
        //console.log(data[0])

        return data;
      }
    },
    irASmartPhone: function (SmartPhone) {
      console.log("yendo al smartphone");
      //console.log(SmartPhone);
      this.$store.dispatch("setCurrentPhoneAction", SmartPhone);
      this.$router.push({ path: "/SmartPhone" });
      //console.log(this.$store.getters.currentPhone);
    },
    cargar: function () {
      this.todos = this.peticion("match (n:SmartPhone) return n limit 30 ");
      this.marcas = this.peticion("match (n:brand_name) return n");
      this.mostrar = this.todos;
      this.cargado = true;
    },
    ordenar: function (val, tipo) {
      console.log("ordenar");
      var aux = [];
      if (tipo == "marca") {
        this.todos.forEach((element) => {
          if (element.brand_name == val) {
            aux.push(element);
          }
        });
        console.log(aux);
      }
      if (tipo == "score") {
        aux = this.mostrar.sort(function (a, b) {
          return b["device_score"] - a["device_score"];
        });
      }
      if (tipo == "me_gusta") {
        aux = this.mostrar.sort(function (a, b) {
          return b["me_gusta"] - a["me_gusta"];
        });
      }
      this.mostrar = aux;
    },
  },
};
</script>
