<template>
  <v-app>
    <v-app-bar title="Osada Kinbaku Dojo e.V.">
      <template v-slot:prepend>
        <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>    
      </template>
    </v-app-bar>

    <v-navigation-drawer
        v-model="drawer"
        :location="left"
      >
      <v-list-item to="verein" title="Verein"></v-list-item>
      <v-list-item class="indent" to="verein#ziele" title="Ziele des Vereins"></v-list-item>
      <v-list-item class="indent" to="verein#mitgliedschaften" title="Mitgliedschaften"></v-list-item>
      <!-- <v-list-item class="indent" to="verein#trainerinnen" title="Trainerinnen und Trainer"></v-list-item> -->

      <v-list-item to="infos" title="Infos"></v-list-item>
      <v-list-item class="indent" to="infos#besuch" title="Vor dem ersten Besuch"></v-list-item>
      <v-list-item class="indent" to="infos#sicherheit" title="Sicherheit und Risiken"></v-list-item>
      <v-list-item class="indent" to="infos#consent" title="Consent"></v-list-item>
      <v-list-item class="indent" to="infos#consent-training" title="Consent im Training"></v-list-item>


      <v-list-item to="training-und-workshops" title="Training und Workshops"></v-list-item>
      <v-list-item class="indent" to="training-und-workshops#training" title="Training"></v-list-item>
      <v-list-item class="indent" to="training-und-workshops#workshops" title="Workshops"></v-list-item>
      <v-list-item class="indent" to="training-und-workshops#einführungsveranstaltung" title="Einführungsveranstaltung"></v-list-item>
      <v-list-item class="indent" to="training-und-workshops#einzelunterricht" title="Einzelunterricht"></v-list-item>

      <v-list-item to="galerie" title="Galerie"></v-list-item>

      <v-list-item to="kurse" title="Kurse"></v-list-item>

      <v-divider></v-divider>

      <v-list-item to="impressum" title="Impressum"></v-list-item>
      <v-list-item to="datenschutz" title="Datenschutz"></v-list-item>
    </v-navigation-drawer>    

    <router-view />
  </v-app>
</template>

<script>
  export default {
    data: () => ({
      drawer: true,
    }),
  }
</script>

<style>
p {
  margin-bottom: .5em;
}

h1 {
  margin-top: 1.2em;
  margin-bottom: 1em;
}
h2 {
  margin-top: 1.1em;
  margin-bottom: .7em;
}
h3 {
  margin-top: .8em;
  margin-bottom: .5em;
}
.indent {
  margin-left: 2em;
}
</style>