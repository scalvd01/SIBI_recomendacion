<template>
  <v-content>
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
                <v-btn color="blue" @click="mandarDatos()">Registro</v-btn>
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
  </v-content>
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
      console.log("gracias al v-model");
      console.log("Nombre =", this.name);
      console.log("Palabra de paso = ", this.password);

      //peticion post que comprueba el loggueo
      var xhttp = new XMLHttpRequest();
      var url = "http://localhost:5000/baseDatos/registro";
      xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
          console.log(this.responseText);
          window.location.href = "/#/Login";
        }
      };

      xhttp.open("POST", url, true);
      xhttp.setRequestHeader("Access-Control-Allow-Headers", "*");
      xhttp.setRequestHeader("Content-type", "application/json; charset=utf-8");
      xhttp.setRequestHeader("Access-Control-Allow-Origin", "*");

      xhttp.send(
        JSON.stringify({
          usuario: this.name,
          contrasenya: this.password,
          nombre: this.nombre,
          apellidos: this.apellidos,
          DNI: this.DNI,
          saldoPuntos: 20,
          esAdmin: false,
        })
      );
    },
  },
  components: {},
};
</script>
