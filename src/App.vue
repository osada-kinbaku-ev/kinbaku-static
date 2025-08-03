<template>
  <v-app>
    <v-app-bar>
      <template v-slot:prepend>
        <v-app-bar-nav-icon v-if="$vuetify.display.mobile" variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      </template>
      <v-toolbar-title style="cursor: pointer" @click="$router.push('home')" >Osada Kinbaku Dojo e.V.</v-toolbar-title>

      <v-btn v-if="!$vuetify.display.mobile" class="mx-3" variant="text" v-for="label, to in menu" v-bind:key="label" :to="to" :text="label" slim></v-btn>

      <v-spacer></v-spacer>
    </v-app-bar>

    <v-navigation-drawer
        v-model="drawer"
        :location="left"
        temporary
      >
      <v-list-item v-for="label, to in menu" v-bind:key="label" :to="to" :title="label"></v-list-item>
    </v-navigation-drawer>

    <router-view />
  </v-app>
</template>

<script>
  export default {
    data: () => ({
      drawer: false,
      menu: {
        verein: "Verein",
        training: "Training",
        intro: "Einführungsveranstaltung",
        events: "Events",
        vereinsregeln: "Vereinsregeln",
        galerie: "Galerie",
      }
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
.indent.v-list-item--variant-text .v-list-item__overlay {
  opacity: 0;
}

.v-toolbar-title__placeholder {
  overflow: visible !important;
}
</style>