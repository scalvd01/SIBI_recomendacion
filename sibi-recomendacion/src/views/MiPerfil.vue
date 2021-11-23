<template>
  <v-app>
    <v-main>
      <div class="mt-8 mx-9">
        <v-card>
        hola perfil
      </v-card>
      </div>
      
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "MiPerfil",

  mounted() {
    
    /*this.sliderPantalla = this.ejecutarQuerySliders(
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
    );*/

    //this.traerDatosSteppers();
    //pedir para los sliders
    /*this.cargarPuntos();
    this.cargarSocio();
    this.separar();
    this.$store.dispatch("setStateLogueadoAction", true);*/
  },

  data: () => ({
    
  }),
  methods: {

  },
};
</script>
