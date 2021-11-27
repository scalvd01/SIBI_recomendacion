<template>
  <v-app>
    <v-main>
      <v-row justify="space-between" class="mt-4 mx-4">
        <v-col
          ><h2>Modo de recomendación</h2>
          <v-expansion-panels>
            <v-expansion-panel>
              <v-expansion-panel-header> Normal </v-expansion-panel-header>
              <v-expansion-panel-content>
                <v-divider></v-divider>
                <div class="mt-4">
                  Gama:
                  <v-btn
                    color="red lighten-1"
                    class="ml-2"
                    @click="queriesNormal(1)"
                    >Baja</v-btn
                  >
                  <v-btn
                    color="yellow lighten-1"
                    class="ml-2"
                    @click="queriesNormal(2)"
                    >media</v-btn
                  >
                  <v-btn
                    color="green lighten-1"
                    class="ml-2"
                    @click="queriesNormal(3)"
                    >alta</v-btn
                  >
                </div>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
              <v-expansion-panel-header> Avanzado </v-expansion-panel-header>
              <v-expansion-panel-content>
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
                        Antes de hacerte una recomendación indícanos tus
                        preferencias para poder ser más precisos.
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
                                @change="
                                  printear(tamPantallaIndex), (s1 = true)
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
                                @change="printear(bateriaIndex), (s2 = true)"
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
                        <span class="subheading font-weight-light mr-1 ml-1"
                          >GB</span
                        >
                        <v-container fluid grid-list-md>
                          <v-layout row wrap>
                            <v-flex>
                              <v-slider
                                :max="sliderRam.length - 1"
                                persistent-hint
                                v-model="ramIndex"
                                @change="printear(ramIndex), (s3 = true)"
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
                    Cámara
                    <small>Seleccione los megapíxeles de la cámara</small>
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
                                @change="printear(camaraIndex), (s4 = true)"
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
                          @change="s5 = true"
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
                      >Seleccione su sistema operativo o marca de
                      preferencia</small
                    >
                  </v-stepper-step>

                  <v-stepper-content step="6">
                    <v-card class="mb-5"
                      ><div class="ma-1">
                        <v-select
                          v-model="osTrueValue"
                          :items="osList"
                          :menu-props="{ maxHeight: '400' }"
                          hint="Elige un OS"
                          persistent-hint
                          @change="s6 = true"
                        ></v-select
                        ><v-select
                          v-model="brandTrueValue"
                          :items="brandList"
                          :menu-props="{ maxHeight: '400' }"
                          hint="Elige una marca"
                          persistent-hint
                          @change="s6 = true"
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
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-col>
        <!---->
        <v-col v-if="preparado">
          <v-card class="pa-6 mt-9">
            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-card height="180">
                    <div class="d-flex flex-no-wrap justify-space-between">
                      <v-avatar class="ma-3" size="150" tile>
                        <v-img
                          :src="telefonoRecomendado.picture"
                          contain
                        ></v-img>
                      </v-avatar>
                      <v-col
                        ><div>
                          <v-card-title
                            class="text-h5"
                            v-text="telefonoRecomendado.name"
                          ></v-card-title>

                          <v-card-subtitle
                            v-text="telefonoRecomendado.brand_name"
                          ></v-card-subtitle>

                          <v-card-actions class="ml-2 mt-5">
                            <div>
                              <v-btn
                                color="success"
                                text
                                elevation="1"
                                @click="irASmartPhone(telefonoRecomendado)"
                              >
                                ver teléfono
                              </v-btn>

                              <v-icon color="red"
                                >mdi-cards-heart-outline</v-icon
                              >
                              <span>{{ telefonoRecomendado.me_gusta }}</span>
                            </div>
                          </v-card-actions>
                        </div></v-col
                      >
                    </div>
                  </v-card>
                </v-col>
              </v-row>
            </v-container>
            <v-expansion-panels class="px-3">
              <v-expansion-panel>
                <v-expansion-panel-header
                  >Más recomendaciones</v-expansion-panel-header
                >
                <v-expansion-panel-content>
                  <v-card
                    height="180"
                    class="mb-3"
                    v-for="(item, index) in otrasRecomendaciones"
                    :key="index"
                  >
                    <div class="d-flex flex-no-wrap justify-space-between">
                      <v-avatar class="ma-3" size="150" tile>
                        <v-img
                          :src="otrasRecomendaciones[index].picture"
                          contain
                        ></v-img>
                      </v-avatar>
                      <v-col
                        ><div>
                          <v-card-title
                            class="text-h5"
                            v-text="otrasRecomendaciones[index].name"
                          ></v-card-title>

                          <v-card-subtitle
                            v-text="otrasRecomendaciones[index].brand_name"
                          ></v-card-subtitle>

                          <v-card-actions class="ml-2 mt-5">
                            <div>
                              <v-btn
                                color="success"
                                text
                                elevation="1"
                                @click="
                                  irASmartPhone(otrasRecomendaciones[index])
                                "
                              >
                                ver teléfono
                              </v-btn>

                              <v-icon color="red"
                                >mdi-cards-heart-outline</v-icon
                              >
                              <span>{{
                                otrasRecomendaciones[index].me_gusta
                              }}</span>
                            </div>
                          </v-card-actions>
                        </div></v-col
                      >
                    </div>
                  </v-card>
                </v-expansion-panel-content>
              </v-expansion-panel>
            </v-expansion-panels>
          </v-card>
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
    this.expansionList = this.ejecutarQuerySliders(
      "MATCH (n:expansion) RETURN n",
      "Has_expansion"
    );
    this.osList = this.ejecutarQuerySliders("MATCH (n:os) RETURN n", "os");
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
    preparado: false,
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
    osList: [],
    brandList: [],

    tamPantallaIndex: 44, //para que por defecto este en un valor medio
    tamPantallaTrueValue: 0,
    bateriaIndex: 0,
    bateriaTrueValue: 0,
    ramIndex: 0,
    ramTrueValue: 0,
    camaraIndex: 0,
    camaraTrueValue: 0,
    expansionTrueValue: false,
    expansionTrueValueString: "",
    osTrueValue: "",
    brandTrueValue: "",
    telefonoRecomendado: [
      {
        name: "",
        picture: "",
        os: "",
        brand_name: "",
        me_gusta: 0,
      },
    ],
    otrasRecomendaciones: [
      {
        name: "",
        picture: "",
        os: "",
        brand_name: "",
        me_gusta: 0,
      },
    ],
  }),
  methods: {
    printear: function (a) {
      console.log(a);
    },

    recogerSliderData: function () {
      this.tamPantallaTrueValue = this.sliderPantalla[this.tamPantallaIndex];
      this.bateriaTrueValue = this.sliderBateria[this.bateriaIndex];
      this.ramTrueValue = this.sliderRam[this.ramIndex];
      this.camaraTrueValue = this.sliderCamara[this.camaraIndex];
      if (this.expansionTrueValue) {
        this.expansionTrueValueString = "expansion";
      } else {
        this.expansionTrueValueString = "no_expansion";
      }
    },

    resetStepper: function () {
      this.stepper = 0;
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

      console.log(
        "tam " +
          this.s1 +
          "\nbat " +
          this.s2 +
          "\nram " +
          this.s3 +
          "\ncam " +
          this.s4 +
          "\nexp " +
          this.s5 +
          "\nos/brand " +
          this.s6
      );

      //formar query
      var a = "";
      if (this.s1) {
        console.log("tam");
        a +=
          "match (n:SmartPhone)-[:HAS_DISPLAY_SIZE]-(a) where a.n_display_size='" +
          this.tamPantallaTrueValue +
          "'  ";
      }
      if (this.s2) {
        console.log("bat");
        a +=
          "match (n:SmartPhone)-[:HAS_BATTERY]-(b) where b.capacidad='" +
          this.bateriaTrueValue +
          "'  ";
      }
      if (this.s3) {
        console.log("ram");
        a +=
          "match (n:SmartPhone)-[:HAS_RAM]-(c) where c.n_ram='" +
          this.ramTrueValue +
          "'  ";
      }
      if (this.s4) {
        console.log("cam");
        a +=
          "match (n:SmartPhone)-[:HAS_CAMERA_PIXELS]-(d) where d.n_camera_pixels='" +
          this.camaraTrueValue +
          "'  ";
      }
      if (this.s5) {
        console.log("exp");
        a +=
          "match (n:SmartPhone)-[:HAS]-(e) where e.Has_expansion='" +
          this.expansionTrueValueString +
          "'  ";
      }
      if (this.osTrueValue != "") {
        console.log("os");
        var letr = ["f", "g", "h", "i", "j", "k"]; //por si se usa con multiple opción
        var aaa = this.osTrueValue + "";
        var lis = [];
        lis = aaa.split(",");
        lis.forEach(function (element, i) {
          a +=
            "match (n:SmartPhone)-[:HAS_OS]-(" +
            letr[i] +
            ") where " +
            letr[i] +
            ".os='" +
            element +
            "'  ";
        });
      }
      if (this.brandTrueValue != "") {
        console.log("brand");
        var letr1 = [
          "l",
          "m",
          "n",
          "o",
          "p",
          "q",
          "r",
          "s",
          "t",
          "u",
          "v",
          "w",
          "x",
          "y",
          "z",
          "aa",
          "bb",
          "cc",
          "dd",
          "ee",
          "ff",
          "gg",
          "hh",
          "ii",
          "jj",
          "kk",
          "ll",
          "mm",
          "nn",
          "oo",
          "pp",
          "qq",
          "rr",
          "ss",
          "tt",
          "uu",
          "vv",
          "ww",
          "xx",
          "yy",
          "zz",
          "aaa",
          "bbb",
          "ccc",
          "ddd",
          "eee",
          "fff",
          "ggg",
          "hhh",
          "iii",
          "jjj",
          "kkk",
          "lll",
          "mmm",
          "nnn",
          "ppp",
          "qqq",
          "rrr",
          "sss",
          "ttt",
          "uuu",
          "vvv",
          "www",
          "xxx",
          "yyy",
          "zzz",
        ]; //por si se usa con multiple opción
        console.log(letr1.length);
        var xxx = this.brandTrueValue + "";
        lis = xxx.split(",");
        lis.forEach(function (element, i) {
          a +=
            "match (n:SmartPhone)-[:HAS_BRAND]-(" +
            letr1[i] +
            ") where " +
            letr1[i] +
            ".brand_name='" +
            element +
            "'  ";
        });
      }

      if (a.length == 0) {
        console.log("no hay nada");
        a +=
          "MATCH (n:SmartPhone) RETURN n ORDER BY n.device_score DESC LIMIT 10";
      } else {
        a += "RETURN n ORDER BY n.device_score DESC LIMIT 10";
      }

      console.log(a);

      //hacer peticion

      var request = new XMLHttpRequest();

      request.open("POST", "http://localhost:5000/runQuery", false); // `false` makes the request synchronous
      request.setRequestHeader("Access-Control-Allow-Headers", "*");
      request.setRequestHeader(
        "Content-type",
        "application/json; charset=utf-8"
      );
      request.setRequestHeader("Access-Control-Allow-Origin", "*");
      request.send(JSON.stringify({ query: a }));

      if (request.status === 200) {
        var data = JSON.parse(request.responseText);

        if (data.length == 0) {
          console.log("vacio");
          data = this.recomendacionCombinada(a);
        }
        this.telefonoRecomendado = data.shift();
        this.otrasRecomendaciones = data;
        this.preparado = true;
        console.log(data);
        console.log(this.telefonoRecomendado);
        console.log(this.otrasRecomendaciones);

        //return data;
      }
    },

    recomendacionCombinada: function (query) {
      console.log("recomendacion Combinada");
      var aux = query.split("  ");
      var r = aux.pop();
      r = r.replace("LIMIT 10", "");
      var aux1 = [];
      aux.forEach((elem) => {
        elem += " " + r;
        aux1.push(elem);
      });

      var nuevaQuery = aux1.join(" UNION ALL ").replace(/, ([^,]*)$/, " $1"); //para intercalar un union all entre todas las query menos en la ultima
      console.log("ejecutando " + nuevaQuery);

      //hacemos la peticion con la nueva query
      var request = new XMLHttpRequest();

      request.open("POST", "http://localhost:5000/runQuery", false); // `false` makes the request synchronous
      request.setRequestHeader("Access-Control-Allow-Headers", "*");
      request.setRequestHeader(
        "Content-type",
        "application/json; charset=utf-8"
      );
      request.setRequestHeader("Access-Control-Allow-Origin", "*");
      request.send(JSON.stringify({ query: nuevaQuery }));

      if (request.status === 200) {
        var data = JSON.parse(request.responseText);
        //console.log(data); //ya esta ordenado desc

        var arr_ids = []; //obtenemos un array de ids de data
        data.forEach(function (elem, index) {
          arr_ids.push(elem.id);
        });
        //console.log(arr_ids);

        //contamos las ocurrencias en el array de ids
        const occurrences = arr_ids.reduce(function (acc, curr) {
          return acc[curr] ? ++acc[curr] : (acc[curr] = 1), acc;
        }, {});

        //console.log(occurrences); //nos devuelve un obj y lo devolvemos a arr
        var ar = Object.entries(occurrences);
        //console.log(ar);
        //ordenamos ese array segun las ocurrencias
        var sortedArray = ar.sort(function (a, b) {
          return b[1] - a[1];
        });
        //console.log(sortedArray);
        //ahora coger todos los tel que tengan el mismo n de ocurrencias que el primero, ver a ver si los scores estan bien y si no ordenarlos y devolverlos
        var topOcurr = sortedArray[0][1];
        var topOcurrArray = [];
        sortedArray.forEach((element) => {
          if (element[1] == topOcurr) {
            topOcurrArray.push(element[0]);
          }
        });
        //console.log(topOcurrArray);

        //buscamos cada objeto que tiene el id de topocurraray y lo metemos en otro
        var topOcurrObjArray = [];

        topOcurrArray.forEach((id) => {
          for (let i = 0; i < data.length; i++) {
            const obj = data[i];
            if (id == obj["id"]) {
              topOcurrObjArray.push(obj);
              break;
            }
          }
        });
        //console.log(topOcurrObjArray);

        //ordenamos por score
        var clean = topOcurrObjArray.sort(function (a, b) {
          return b["device_score"] - a["device_score"];
        });
        if (clean.length >= 10) {
          //si tiene mas de 10 devolvemos solo 10

          clean.length = 10;
        }
        console.log("clean");
        console.log(clean);
        return clean;
      }
    },

    queriesNormal: function (val) {
      var query = "";
      if (val == 1) {
        console.log("baja");
        query +=
          "MATCH (n:SmartPhone) WHERE n.device_score<784 RETURN n ORDER BY n.device_score DESC  ";
      }
      if (val == 2) {
        console.log("media");
        query +=
          "MATCH (n:SmartPhone) WHERE n.device_score>784 AND n.device_score<1459 RETURN n ORDER BY n.device_score DESC  ";
      }
      if (val == 3) {
        console.log("alta");
        query +=
          "MATCH (n:SmartPhone) WHERE n.device_score>1459 RETURN n ORDER BY n.device_score DESC  ";
      }
      //si hay un usuario logueado hacer combinada si no no
      // console.log(this.$store.getters.logueado)
      if (this.$store.getters.logueado) {
        console.log("combi");

        //hacer peticion combinada

        //hacer funcion para sacar los datos de los favoritos del usuario
        
      } else {
        //hacer peticion normal

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
          if (data.length > 10) {
            data.length = 10;
          }
          this.telefonoRecomendado = data.shift();
          this.otrasRecomendaciones = data;
          this.preparado = true;
          console.log(data);

          //return data;
        }
      }
    },
    irASmartPhone: function (SmartPhone) {
      console.log("yendo al smartphone");
      //console.log(SmartPhone);
      this.$store.dispatch("setCurrentPhoneAction", SmartPhone);
      this.$router.push({ path: "/SmartPhone" });
      //console.log(this.$store.getters.currentPhone);
    },

    cambiarEstadoOnchange: function (s) {
      this.s = true;
    },

    ejecutarQuerySliders: function (query, name) {
      console.log("ejecutando " + query);
      var request = new XMLHttpRequest();
      //console.log(JSON.stringify(query));

      request.open("POST", "http://localhost:5000/runQuerySliders", false); // `false` makes the request synchronous
      request.setRequestHeader("Access-Control-Allow-Headers", "*");
      request.setRequestHeader(
        "Content-type",
        "application/json; charset=utf-8"
      );
      request.setRequestHeader("Access-Control-Allow-Origin", "*");
      request.send(JSON.stringify({ query: query, name: name }));

      if (request.status === 200) {
        var data = JSON.parse(request.responseText);
        //console.log(data);

        return data;
      }
    },
  },
};
</script>
