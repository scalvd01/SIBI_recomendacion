<template>
  <v-app>
    <v-main>
      <div class="mt-8 mx-9">
        <v-card class="overflow-x-auto">
          <div class="d-flex flex-no-wrap justify-space-between">
            <v-col>
              <v-avatar class="ma-3" size="350" tile>
                <v-img :src="SmartPhone.picture" contain></v-img>
              </v-avatar>
            </v-col>

            <v-col cols="9"
              ><div>
                <v-card-title
                  class="text-h5"
                  v-text="SmartPhone.name"
                ></v-card-title>

                <v-card-subtitle
                  v-text="SmartPhone.brand_name"
                ></v-card-subtitle>

                <v-card-actions class="ml-2 mt-5">
                  <div>
                    <v-btn text icon @click="addAfavs(SmartPhone)"
                      ><v-icon v-if="!faved" color="red"
                        >mdi-cards-heart-outline</v-icon
                      ><v-icon v-if="faved" color="red"
                        >mdi-cards-heart</v-icon
                      ></v-btn
                    ><v-snackbar v-model="snackbar" :timeout="2000">
                      Debes estar logueado para añadir a favoritos
                    </v-snackbar>

                    <span class="pt-2">{{ SmartPhone.me_gusta }}</span>
                  </div>
                </v-card-actions>

                <div class="mx-5 mt-5 pb-5">
                  <span class="text-h5">Características</span>
                  <div v-for="(spec, index) in specs" :key="index">
                    {{ spec }}
                  </div>
                </div>
              </div></v-col
            >
            <v-col></v-col>
          </div>
        </v-card>
      </div>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "SmartPhone",

  mounted() {
    this.cargarSmartPhone();
    this.cleanSpecs();
  },

  data: () => ({
    faved: false,
    specs: [],
    SmartPhone: {
      name: "",
      picture: "",
      os: "",
      brand_name: "",
      me_gusta: 0,
    },
    snackbar: false,
  }),
  methods: {
    cargarSmartPhone: function () {
      this.SmartPhone = this.$store.getters.currentPhone;
      var user = this.$store.getters.currentUser;
      if (this.$store.getters.logueado) {
        //para ponerlo faveado si ya estaba de antes
        if (user.favoritos.length != 0) {
          user.favoritos.forEach((element) => {
            if (element.id == this.SmartPhone.id) {
              this.faved = true;
            }
          });
        }
      }
    },
    cleanSpecs: function () {
      var s = this.SmartPhone.specifications;
      s = s.split(',"');
      s.forEach((x) => {
        x = x.replace("{", "");
        x = x.replace("}", "");
        x = x.replace("\\", "");
        x = x.replace('"', "");
        x = x.replace(':"', ": ");
        x = x.replace('"', "");
        //console.log(x);
        this.specs.push(x);
      });

      //console.log(s);
    },

    addAfavs: function (tel) {
      var self = this;
      if (this.$store.getters.logueado) {
        this.faved = !this.faved;
        var user = this.$store.getters.currentUser;
        //console.log(user.favoritos);

        if (user.favoritos.length != 0) {
          var yaesta = false;
          user.favoritos.forEach(function (element, index) {
            if (element.id == tel.id) {
              yaesta = true;
              user.favoritos.splice(index, 1);
            }
          });
        }

        if (!yaesta) {
          user.favoritos.push(tel);
          //console.log(query);
          this.$store.dispatch("setCurrentUserAction", user);

          var h = [];
          user.favoritos.forEach((element) => {
            h.push(element.id);
          });

          var query =
            "MATCH (n:user{usuario: '" +
            user.usuario +
            "'}) SET n.favsids = '" +
            h +
            "' RETURN n";
          console.log(query);

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
            //console.log(data);
          }
        } else {

          
          var j = [];
          user.favoritos.forEach((element) => {
            j.push(element.id);
          });

          var query1 =
            "MATCH (n:user{usuario: '" +
            user.usuario +
            "'}) SET n.favsids = '" +
            j +
            "' RETURN n";
          console.log(query1);

          var request1 = new XMLHttpRequest();

          request1.open("POST", "http://localhost:5000/runQuery", false); // `false` makes the request synchronous
          request1.setRequestHeader("Access-Control-Allow-Headers", "*");
          request1.setRequestHeader(
            "Content-type",
            "application/json; charset=utf-8"
          );
          request1.setRequestHeader("Access-Control-Allow-Origin", "*");
          request1.send(JSON.stringify({ query: query1 }));

          if (request1.status === 200) {
            var data1 = JSON.parse(request1.responseText);
            //console.log(data);
          }
        }
        this.updateFavNumBD();
      } else {
        this.snackbar = true;
      }
    },
    
    updateFavNumBD: function () {
      if (this.faved) {
        this.SmartPhone.me_gusta += 1;
      } else {
        this.SmartPhone.me_gusta -= 1;
      }
      //update cambios to bd
      this.peticion(
        "match (n:SmartPhone{id: '" +
          this.SmartPhone.id +
          "'}) set n.me_gusta= " +
          this.SmartPhone.me_gusta +
          " RETURN n"
      );
    },
    peticion: function (query) {
      console.log("ejecutando"+query)
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

        return data[0];
      }
    },
  },
};
</script>
