<template>
  <v-app>
    <v-main>
      <v-btn color="success" @click="printear(s1)">print</v-btn>
      <v-row justify="space-between" class="mt-4 mx-4">
        <v-col>
          <v-stepper v-model="stepper" non-linear vertical>
            <v-stepper-step
              :complete="true"
              step="0"
              editable
              edit-icon="$complete"
            >
              Configuración
              <small>Seleccione sus preferencias</small>
            </v-stepper-step>

            <v-stepper-content step="0">
              <v-card color="grey lighten-4" class="mb-5"
                ><div class="ma-3">
                  Antes de hacerte una recomendación indícanos tus preferencias
                  para poder ser más precisos.
                </div></v-card
              >
              <v-btn color="primary" right @click="stepper = 1">
                Siguiente
              </v-btn>
            </v-stepper-content>

            <v-stepper-step
              :complete="s1"
              step="1"
              editable
              edit-icon="$complete"
            >
              Tamaño
              <small>Seleccione el tamaño de pantalla</small>
            </v-stepper-step>

            <v-stepper-content step="1">
              <v-card class="mb-5" height="200px"
                ><div class="ma-1">
                  <span
                    class="text-h2 font-weight-light"
                    v-text="sliderPantalla[tamPantallaIndex]"
                  ></span>
                  <span class="subheading font-weight-light mr-1"
                    >Pulgadas</span
                  >
                  <v-container fluid grid-list-md>
                    <v-layout row wrap>
                      <v-flex>
                        <v-slider
                          :max="sliderPantalla.length - 1"
                          hint="Tamaño"
                          persistent-hint
                          v-model="tamPantallaIndex"
                          @change="
                            printear(tamPantallaIndex),
                              setRealValueFromSlider(
                                sliderPantalla,
                                tamPantallaIndex,
                                tamPantallaTrueValue
                              )
                          "
                        ></v-slider>
                      </v-flex>
                    </v-layout>
                  </v-container></div
              ></v-card>
              <v-btn color="primary" @click="(stepper = 2), (s1 = true)">
                Siguiente
              </v-btn>
            </v-stepper-content>

            <v-stepper-step
              :complete="s2"
              step="2"
              editable
              edit-icon="$complete"
            >
              Batería <small>Seleccione la capacidad de la batería</small>
            </v-stepper-step>

            <v-stepper-content step="2">
              <v-card
                color="grey lighten-1"
                class="mb-12"
                height="200px"
              ></v-card>
              <v-btn color="primary" @click="(stepper = 3), (s2 = true)">
                Siguiente
              </v-btn>
            </v-stepper-content>

            <v-stepper-step
              :complete="s3"
              step="3"
              editable
              edit-icon="$complete"
            >
              RAM <small>Seleccione la cantidad de RAM</small>
            </v-stepper-step>

            <v-stepper-content step="3">
              <v-card
                color="grey lighten-1"
                class="mb-12"
                height="200px"
              ></v-card>
              <v-btn color="primary" @click="(stepper = 4), (s3 = true)">
                Siguiente
              </v-btn>
            </v-stepper-content>

            <v-stepper-step
              :complete="s4"
              step="4"
              editable
              edit-icon="$complete"
            >
              Cámara <small>Seleccione los megapíxeles de la cámara</small>
            </v-stepper-step>

            <v-stepper-content step="4">
              <v-card
                color="grey lighten-1"
                class="mb-12"
                height="200px"
              ></v-card>
              <v-btn color="primary" @click="(stepper = 5), (s4 = true)">
                Siguiente
              </v-btn>
            </v-stepper-content>

            <v-stepper-step
              :complete="s5"
              step="5"
              editable
              edit-icon="$complete"
              >Expansión
              <small
                >Seleccione si necesita un slot para almacenamiento
                externo</small
              >
            </v-stepper-step>

            <v-stepper-content step="5">
              <v-card
                color="grey lighten-1"
                class="mb-12"
                height="200px"
              ></v-card>
              <v-btn color="primary" @click="(stepper = 6), (s5 = true)">
                Siguiente
              </v-btn>
            </v-stepper-content>

            <v-stepper-step
              :complete="s6"
              step="6"
              editable
              edit-icon="$complete"
            >
              Sistema Operativo
              <small>Seleccione su sistema operativo de preferencia</small>
            </v-stepper-step>

            <v-stepper-content step="6">
              <v-card
                color="grey lighten-1"
                class="mb-12"
                height="200px"
              ></v-card>
              <v-btn color="primary" @click="(stepper = 7), (s6 = true)">
                Siguiente
              </v-btn>
            </v-stepper-content>

            <v-stepper-step step="7"> Recomendacion </v-stepper-step>
            <v-stepper-content step="7">
              <v-card
                color="grey lighten-1"
                class="mb-12"
                height="200px"
              ></v-card>
              <v-btn color="primary" @click="recomendar()"> Siguiente </v-btn>
            </v-stepper-content>
          </v-stepper>
        </v-col>
        <v-col>
          <v-card> Recomendacion </v-card>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "Principal",

  mounted() {
    this.resetStepper();
    //pedir para los sliders
    /*this.cargarPuntos();
    this.cargarSocio();
    this.separar();
    this.$store.dispatch("setStateLogueadoAction", true);*/
  },

  data: () => ({
    //para focusear a un stepper en concreto
    stepper: 0,
    //para manejar el icono de completado de los steppers
    s1: false,
    s2: false,
    s3: false,
    s4: false,
    s5: false,
    s6: false,
    s7: false,
    s8: false,

    //sliders
    sliderPantalla: [
      1.77, 1.8, 2.2, 2.4, 2.8, 3.3, 3.8, 4.0, 4.5, 4.6, 4.7, 4.95, 5.0, 5.09,
      5.1, 5.15, 5.2, 5.3, 5.34, 5.4, 5.45, 5.46, 5.5, 5.6, 5.65, 5.67, 5.7,
      5.71, 5.72, 5.73, 5.8, 5.81, 5.83, 5.84, 5.85, 5.86, 5.88, 5.9, 5.93,
      5.94, 5.95, 5.97, 5.98, 5.99, 6.0, 6.01, 6.09, 6.1, 6.15, 6.18, 6.19, 6.2,
      6.21, 6.22, 6.23, 6.24, 6.26, 6.28, 6.3, 6.35, 6.36, 6.38, 6.39, 6.4,
      6.41, 6.42, 6.43, 6.44, 6.45, 6.47, 6.49, 6.5, 6.51, 6.52, 6.53, 6.55,
      6.56, 6.57, 6.58, 6.59, 6.6, 6.62, 6.63, 6.65, 6.67, 6.7, 6.72, 6.76,
      6.78, 6.8, 6.81, 6.82, 6.85, 6.89, 6.9, 6.92, 6.95, 7.0, 7.09, 7.1, 7.12,
      7.2, 7.3, 7.6, 7.9, 8.0, 8.1, 8.4, 8.88, 9.6, 9.7, 10.0, 10.1, 10.2, 10.3,
      10.36, 10.4, 10.5, 10.8, 10.9, 11.0, 11.5, 12.4, 12.9, 17.3,
    ],
    tamPantallaIndex: 44, //para que por defecto este en un valor medio
    tamPantallaTrueValue: 0,

    /*albumes: [],
    cartas:  [],
    usuario: null,*/
  }),
  methods: {
    printear: function (d) {
      console.log(d);
    },

    setRealValueFromSlider: function (array, index, actualizar) {
      this.actualizar = array[index];
      console.log(this.actualizar);
    },

    resetStepper: function () {
      this.stepper = 1;
      this.s1 = false;
      this.s2 = false;
      this.s3 = false;
      this.s4 = false;
      this.s5 = false;
      this.s6 = false;
      this.s7 = false;
      this.s8 = false;
      console.log("s's reset");
    },

    recomendar: function () {
      //recoger valores
      console.log("hola");
      //hacer peticion
    },

    resetSliders: function () {
      console.log("entra en reset, no reseteado todavia");

      //reset sliders

      /*this.usuario.colecciones.forEach((coleccion) => {
        this.albumes.push(coleccion.album)

        coleccion.cartas.forEach(carta => {
          this.cartas.push(carta)
        });
      });*/
    },

    //Hacer como esta para traer los slders+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    /*cargarSocio: function() {
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
    },*/
  },
};
</script>
