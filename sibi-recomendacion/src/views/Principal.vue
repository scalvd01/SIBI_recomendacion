<template>
  <v-app>
    <v-main>
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
              <v-card class="mb-5"
                ><div class="ma-1">
                  <span
                    class="text-h2 font-weight-light ml-2"
                    v-text="sliderPantalla[tamPantallaIndex]"
                  ></span>
                  <span class="subheading font-weight-light mr-1 ml-1"
                    >Pulgadas</span
                  >
                  <v-container fluid grid-list-md>
                    <v-layout row wrap>
                      <v-flex>
                        <v-slider
                          :max="sliderPantalla.length - 1"
                          persistent-hint
                          v-model="tamPantallaIndex"
                          @change="printear(tamPantallaIndex)"
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
              <v-card class="mb-5"
                ><div class="ma-1">
                  <span
                    class="text-h2 font-weight-light ml-2"
                    v-text="sliderBateria[bateriaIndex]"
                  ></span>
                  <span class="subheading font-weight-light mr-1 ml-1"
                    >mAh</span
                  >
                  <v-container fluid grid-list-md>
                    <v-layout row wrap>
                      <v-flex>
                        <v-slider
                          :max="sliderBateria.length - 1"
                          persistent-hint
                          v-model="bateriaIndex"
                          @change="printear(bateriaIndex)"
                        ></v-slider>
                      </v-flex>
                    </v-layout>
                  </v-container></div
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
              <v-card class="mb-5"
                ><div class="ma-1">
                  <span
                    class="text-h2 font-weight-light ml-2"
                    v-text="sliderRam[ramIndex]"
                  ></span>
                  <span class="subheading font-weight-light mr-1 ml-1">GB</span>
                  <v-container fluid grid-list-md>
                    <v-layout row wrap>
                      <v-flex>
                        <v-slider
                          :max="sliderRam.length - 1"
                          persistent-hint
                          v-model="ramIndex"
                          @change="printear(ramIndex)"
                        ></v-slider>
                      </v-flex>
                    </v-layout>
                  </v-container></div
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
              <v-card class="mb-5"
                ><div class="ma-1">
                  <span
                    class="text-h2 font-weight-light ml-2"
                    v-text="sliderCamara[camaraIndex]"
                  ></span>
                  <span class="subheading font-weight-light mr-1 ml-1"
                    >Megapíxeles</span
                  >
                  <v-container fluid grid-list-md>
                    <v-layout row wrap>
                      <v-flex>
                        <v-slider
                          :max="sliderCamara.length - 1"
                          persistent-hint
                          v-model="camaraIndex"
                          @change="printear(camaraIndex)"
                        ></v-slider>
                      </v-flex>
                    </v-layout>
                  </v-container></div
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
              <v-card class="mb-5"
                ><div class="ma-1">
                  <span
                    class="text-h2 font-weight-light ml-2"
                    v-text="expansionTrueValue ? 'Sí' : 'No'"
                  ></span>
                  <span class="subheading font-weight-light mr-1 ml-1"
                    >Slot de almacenamiento</span
                  >
                  <v-switch
                    class="ml-4"
                    v-model="expansionTrueValue"
                    inset
                  ></v-switch></div
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
              Sistema Operativo/Marca
              <small
                >Seleccione su sistema operativo o marca de preferencia</small
              >
            </v-stepper-step>

            <v-stepper-content step="6">
              <v-card class="mb-5"
                ><div class="ma-1">
                  <v-select
                    v-model="osTrueValue"
                    :items="osList"
                    :menu-props="{ maxHeight: '400' }"
                    multiple
                    hint="Elige una o varias preferencias"
                    persistent-hint
                  ></v-select
                  ><v-select
                    v-model="brandTrueValue"
                    :items="brandList"
                    :menu-props="{ maxHeight: '400' }"
                    multiple
                    hint="Elige una o varias preferencias"
                    persistent-hint
                  ></v-select></div
              ></v-card>
              <v-btn color="primary" @click="(stepper = 7), (s6 = true)">
                Siguiente
              </v-btn>
            </v-stepper-content>

            <v-stepper-step
              :complete="s7"
              step="7"
              editable
              edit-icon="$complete"
            >
              Recomendacion
            </v-stepper-step>
            <v-stepper-content step="7">
              <v-card color="grey lighten-4" class="mb-5"
                ><div class="ma-3">
                  ¡Lísto! <br />
                  Ahora ya podemos hacerte una recomendación más precisa.
                </div></v-card
              >
              <v-btn
                color="primary"
                @click="recogerSliderData(), (s7 = true), recomendar()"
              >
                Recomendar
              </v-btn>
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
    this.sliderPantalla = this.ejecutarQuerySliders(
      "MATCH (n:n_display_size) RETURN n",
      "n_display_size"
    );
    this.sliderBateria = this.ejecutarQuerySliders(
      "MATCH (n:Capacidad_bateria) RETURN n",
      "capacidad"
    );
    this.sliderRam = this.ejecutarQuerySliders(
      "MATCH (n:n_ram) RETURN n",
      "n_ram"
    );
    this.sliderCamara = this.ejecutarQuerySliders(
      "MATCH (n:n_camera_pixels) RETURN n",
      "n_camera_pixels"
    );
    this.expansionList= this.ejecutarQuerySliders(
      "MATCH (n:expansion) RETURN n",
      "Has_expansion"
    );
    this.osList = this.ejecutarQuerySliders(
      "MATCH (n:os) RETURN n",
      "os"
    );
    this.brandList = this.ejecutarQuerySliders(
      "MATCH (n:brand_name) RETURN n",
      "brand_name"
    );

    //this.traerDatosSteppers();
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

    //sliders
    sliderPantalla: [],
    sliderBateria: [],
    sliderRam: [],
    sliderCamara: [],
    expansionList: [],
    osList: ["apple", "samsung", "motorola", "huawei"],
    brandList: ["1apple", "2samsung", "3motorola", "4huawei"],

    tamPantallaIndex: 44, //para que por defecto este en un valor medio
    tamPantallaTrueValue: 0,
    bateriaIndex: 0,
    bateriaTrueValue: 0,
    ramIndex: 0,
    ramTrueValue: 0,
    camaraIndex: 0,
    camaraTrueValue: 0,
    expansionTrueValue: false,
    osTrueValue: "",
    brandTrueValue: "",

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
    recogerSliderData: function () {
      this.tamPantallaTrueValue = this.sliderPantalla[this.tamPantallaIndex];
      this.bateriaTrueValue = this.sliderBateria[this.bateriaIndex];
      this.ramTrueValue = this.sliderRam[this.ramIndex];
      this.camaraTrueValue = this.sliderCamara[this.camaraIndex];
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
      console.log("steppers reset");
    },

    recomendar: function () {
      //recoger valores
      console.log(
        "Tamaño: " +
          this.tamPantallaTrueValue +
          "\nBatería: " +
          this.bateriaTrueValue +
          "\nRAM: " +
          this.ramTrueValue +
          "\nCámara: " +
          this.camaraTrueValue +
          "\nExpansión: " +
          this.expansionTrueValue +
          "\nOS: " +
          this.osTrueValue +
          "\nMarca: " +
          this.brandTrueValue
      );
      //hacer peticion
    },

    /*traerDatosSteppers: function () {
      console.log("pidiendo datos de steppers");
      var request = new XMLHttpRequest();
      request.open("GET", "http://localhost:5000/getDatosSteppers", false); // `false` makes the request synchronous
      request.send(null);

      if (request.status === 200) {
        var steppers = JSON.parse(request.responseText);
        console.log(steppers);
        console.log("datos de steppers obtenidos");

        steppers.forEach((element) => {
          element.forEach((e) => {});
        });
      }
    },*/

    ejecutarQuerySliders: function (query, name) {
      console.log("ejecutando " + query);
      var request = new XMLHttpRequest();
      console.log(JSON.stringify(query));

      request.open("POST", "http://localhost:5000/runQuery", false); // `false` makes the request synchronous
      request.setRequestHeader("Access-Control-Allow-Headers", "*");
      request.setRequestHeader(
        "Content-type",
        "application/json; charset=utf-8"
      );
      request.setRequestHeader("Access-Control-Allow-Origin", "*");
      request.send(JSON.stringify({ query: query, name: name }));

      if (request.status === 200) {
        var data = JSON.parse(request.responseText);
        console.log(data);
        
        return data;
      }
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
