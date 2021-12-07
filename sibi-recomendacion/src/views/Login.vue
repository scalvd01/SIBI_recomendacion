<template>
  <v-app>
    <v-main>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <v-card
              width="600"
              class="mx-auto mt-5"
              justify="center"
              color="cardAnalisis"
            >
              <v-card-title>
                <h1 class="font-weight-medium">Login</h1>
              </v-card-title>
              <v-card-text>
                <v-form>
                  <v-text-field
                    v-model="name"
                    label="Usuario"
                    prepend-icon="mdi-account-circle"
                    type="text"
                  />
                  <v-text-field
                    v-model="password"
                    :type="showPassword ? 'text' : 'password'"
                    label="Password"
                    prepend-icon="mdi-lock"
                    :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append="showPassword = !showPassword"
                  />
                </v-form>
              </v-card-text>
              <v-divider></v-divider>

              <v-alert id="error" type="error" v-show="visible"
                >El usuario y contraseña no son correctos</v-alert
              >

              <v-card-actions>
                <template>
                  <div class="text-center">
                    <v-menu
                      v-model="menu"
                      :close-on-content-click="false"
                      :nudge-width="200"
                      offset-x
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-btn
                          text
                          v-bind="attrs"
                          v-on="on"
                          class="text-decoration-underline"
                        >
                          Recuperar contraseña
                        </v-btn>

                        <v-btn
                          right
                          absolute
                          color="success"
                          @click="
                            login();
                            mandarDatos();
                          "
                          >Login</v-btn
                        >
                      </template>

                      <v-card>
                        <v-list>
                          <v-list-item>
                            <v-list-item-content>
                              <v-list-item-title
                                >¿Cómo recuperar contraseña?</v-list-item-title
                              >
                              <v-list-item-subtitle
                                >Para recuperar la contraseña, llama al numero
                                +666666666
                              </v-list-item-subtitle>
                            </v-list-item-content>
                          </v-list-item>
                        </v-list>

                        <v-divider></v-divider>
                      </v-card>
                    </v-menu>
                  </div>
                </template>
              </v-card-actions>
            </v-card>
            <v-spacer class="pt-2"></v-spacer>
            <v-card width="600" class="mx-auto">
              <v-card-title
                style="font-size: 20px; padding-top: 15px; padding-left: 10px"
                >¿Aún no está registrado?
                <v-btn
                  right
                  absolute
                  color="blue"
                  class="white--text"
                  route
                  to="/Registro"
                  >Registrarse</v-btn
                >
                <v-snackbar v-model="snackbar" :timeout="2000">
                  Datos incorrectos
                </v-snackbar>
              </v-card-title>
            </v-card>
          </v-col>
        </v-row>
      </v-container></v-main
    >

    <!--:to="{ path: '/' }"-->

    <v-footer class="toolbarLogin">
      <v-card-text class=".font-italic font-weight-bold text-center">
        &copy;2021 — <strong>Phone REC</strong>
      </v-card-text>
    </v-footer>
  </v-app>
</template>

<script>
import store from "../store";

export default {
  name: "Login",

  data() {
    return {
      menu: null,
      visible: false,
      showPassword: false,
      name: "",
      password: "",
      snackbar: false,
    };
  },
  methods: {
    mandarDatos: function () {
      console.log("Nombre =", this.name);
      console.log("Pass = ", this.password);

      var query =
        "MATCH (n:user) WHERE n.usuario='" +
        this.name +
        "' AND n.pass='" +
        this.password +
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

        if (data.length == 0) {
          this.snackbar = true;
        } else {

          var u = data[0]
          var f = u.favsids.split(',')
          var h = u.histids.split(',')

          
          f.forEach(id => {
            u.favoritos.push(this.peticion("match (n:SmartPhone) where n.id='"+id+"' return n"))
          });
          h.forEach(id => {
            u.historial.push(this.peticion("match (n:SmartPhone) where n.id='"+id+"' return n"))
          });

          this.$store.dispatch("setCurrentUserAction", u);
          this.$store.dispatch("changeStateLogueadoAction");
          this.$router.push({ path: "/" });
        }

        console.log(data[0]);
      }
    },

    login: function () {
      console.log("loggeando");
    },
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

        return data[0]
      }
      
    },
  },
  components: {},
};
</script>
