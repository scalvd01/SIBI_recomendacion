<template>
  <v-app>
    <v-main>
      <div class="mt-8 mx-9">
        <v-card>
          <div class="d-flex flex-no-wrap justify-space-between">
            <v-col>
              <v-avatar class="ma-3" size="350" tile>
                <v-img :src="SmartPhone.picture" contain></v-img>
              </v-avatar>
            </v-col>

            <v-col
              ><div>
                <v-card-title
                  class="text-h5"
                  v-text="SmartPhone.name"
                ></v-card-title>

                <v-card-subtitle
                  v-text="SmartPhone.brand_name"
                ></v-card-subtitle>

                <v-card-actions class="ml-2 mt-5">
                  <div v-if="!faved">
                    <v-btn text icon @click="faved = !faved"
                      ><v-icon color="red"
                        >mdi-cards-heart-outline</v-icon
                      ></v-btn
                    >

                    <span class="pt-2">{{ SmartPhone.me_gusta }}</span>
                  </div>
                  <div v-if="faved">
                    <v-btn text icon @click="faved = !faved"
                      ><v-icon color="red">mdi-cards-heart</v-icon></v-btn
                    >

                    <span class="pt-2">{{ SmartPhone.me_gusta }}</span>
                  </div>
                </v-card-actions>
              </div></v-col
            >
            <v-col></v-col>
          </div>
          <div class="mx-16 mt-5 pb-5">
            <span class="text-h5">Características</span>
            <div v-for="(spec, index) in specs" :key="index">{{ spec }}</div>
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
  }),
  methods: {
    cargarSmartPhone: function () {
      this.SmartPhone = this.$store.getters.currentPhone;
      console.log(this.$store.getters.currentPhone);
      console.log(this.SmartPhone);
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
        x = x.replace('"', "");console.log(x);
        this.specs.push(x)
      });
       
      console.log(s);
    },
  },
};
</script>
