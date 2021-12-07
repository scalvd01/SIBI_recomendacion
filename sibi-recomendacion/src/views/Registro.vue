<template>
  <v-main>
    <v-container class="fill-height" fluid>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="4">
          <v-card
            width="600"
            class="mx-auto mt-5"
            justify="center"
            color="grey lighten-3"
          >
            <v-card-title>
              <h1 class="font-weight-medium">Registro</h1>
            </v-card-title>
            <v-card-text>
              <v-form>
                <v-text-field
                  v-model="nombre"
                  label="Nombre"
                  prepend-icon="mdi-account"
                  type="text"
                  :rules="[rules.required, rules.counter]"
                />
                <v-text-field
                  v-model="apellidos"
                  label="Apellidos"
                  prepend-icon="mdi-account"
                  type="text"
                  :rules="[rules.required, rules.counter]"
                />
                <v-text-field
                  v-model="name"
                  label="Usuario"
                  prepend-icon="mdi-account-circle"
                  type="text"
                  :rules="[rules.required, rules.counter]"
                />
                <v-text-field
                  v-model="password"
                  :type="showPassword ? 'text' : 'password'"
                  label="Password"
                  prepend-icon="mdi-lock"
                  :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                  @click:append="showPassword = !showPassword"
                  :rules="[rules.required, rules.counter]"
                />
              </v-form>
            </v-card-text>

            <v-card-actions>
              <template>
                <v-btn color="primary" @click="mandarDatos()">Registro</v-btn>
                <v-snackbar v-model="snackbar" :timeout="2000">
                  Registrado
                </v-snackbar>
              </template>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>

    <!--:to="{ path: '/' }"-->

    <v-footer>
      <v-card-text class=".font-italic font-weight-bold text-center">
        &copy;2021 — <strong>Phone REC</strong>
      </v-card-text>
    </v-footer>
  </v-main>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      showPassword: false,
      name: "",
      password: "",
      nombre: "",
      apellidos: "",
      DNI: "",
      snackbar: false,
      rules: {
        required: (value) => !!value || "Required.",
        counter: (value) => value.length <= 20 || "Max 20 characters",
        email: (value) => {
          const pattern =
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || "Invalid e-mail.";
        },
      },
    };
  },
  methods: {
    login: function () {
      console.log("loggeado");
    },

    mandarDatos: function () {
      console.log("entrado");
      var query = "";
      query +=
        "CREATE (n:user {nombre: '" +
        this.nombre +
        "', apellidos: '" +
        this.apellidos +
        "', usuario: '" +
        this.name +
        "', pass: '" +
        this.password +
        "', historial:[], favoritos:[], histids:'', favsids:''}) RETURN n";

      console.log("ejecutando " + query);

      var request = new XMLHttpRequest();

      request.open("POST", "http://localhost:5000/registrar", false); // `false` makes the request synchronous
      request.setRequestHeader("Access-Control-Allow-Headers", "*");
      request.setRequestHeader(
        "Content-type",
        "application/json; charset=utf-8"
      );
      request.setRequestHeader("Access-Control-Allow-Origin", "*");
      request.send(
        JSON.stringify({
          query: query,
        })
      );

      if (request.status === 200) {
        var data = JSON.parse(request.responseText);
        //devolver el user meterlo en la store y volver a login
        console.log("hecho");

        console.log(data);
        this.snackbar = true;

        this.$router.push({ path: "/Login" });
      }
    },
  },
  components: {},
};
</script>
