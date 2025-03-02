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
      <v-divider></v-divider>
      <v-list-item to="infos" title="Infos"></v-list-item>
      <v-list-item to="training-und-workshops" title="Training und Workshops"></v-list-item>
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
