<template>
  <v-main>
    <router-view />
  </v-main>

  <v-footer
    class="d-flex flex-column align-stretch pa-0 white--text text--darken-1 elevation-12"
  >
    <div class="grey darken-3 d-sm-flex flex-row justify-space-between pa-4">
      <div class="pa-2">
        <b>Osada Kinbaku Dojo e.V.</b>
      </div>
      <div class="d-sm-flex flex-row align-right py-2">
        <div class="px-2"><router-link to="datenschutz">Datenschutzerklärung</router-link></div>
      </div>
    </div>
    <div class="grey darken-4 d-md-flex flex-row justify-space-between pa-6">
      <div>
        <p>{{ email }}</p>
        <p>
          Binzstraße 64<br/>
          13189 Berlin-Pankow
        </p>
      </div>
      <div>
        <p>Registernummer</p>
        <p>VR 29488 B at AG Berlin (Charlottenburg)</p>
        <!-- <p>Umsatzsteuer-Identifikationsnummer: </p> -->
      </div>
      <div>
        <p>Vertreten durch</p>
        <p class="white--text text--darken-2">
          Alexander Esser (Vorsitz)<br/>
          Anser Janczyk<br/>
        </p>
      </div>
    </div>
  </v-footer>
</template>

<script>
export default {
  data: () => ({
    email: atob("==QZk5ibpxmclJWL1tWYi5WarB0bm5Wa".split("").reverse().join("") )
  }),
}
</script>
