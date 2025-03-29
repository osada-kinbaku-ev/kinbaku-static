<template>
  <div class="text-center pa-4">
    <v-dialog v-model="dialog" transition="dialog-bottom-transition" :fullscreen="$vuetify.display.mobile" max-width="600">
      <template v-slot:activator="{ props: activatorProps }">
        <v-btn fab dark small color="primary" variant="outlined" text="Anmelden" v-bind="activatorProps"></v-btn>
      </template>

      <v-card>
        <v-toolbar>
          <v-btn icon="mdi-close" @click="dialog = false"></v-btn>
          <v-toolbar-title>Anmeldung {{ event.title }}</v-toolbar-title>
        </v-toolbar>

        <v-card-text>
          <p>
            <b>Zeit:</b> {{ event.date }} {{ event.time }} <br/>
            <b>Ort:</b> {{ event.location }} <br/>
            <b>Zielgruppe:</b> {{ event.audience }} <br/>
            <b>Gebühr:</b> {{ event.price }} <br/>
          </p>
          <p>
            Für deine Anmeldung benötigen wir deinen Namen, den du beim Workshop verwenden möchtest, sowie eine Email-Adresse, 
            unter der du weitere Informationen zum Workshop empfangen kannst um deine Anmeldung zu bestätigen.
          </p>
        </v-card-text>
        
        <v-divider></v-divider>

        <v-card-text>
          <v-row dense>
            <v-col cols="12">
              <v-text-field label="Name" required></v-text-field>
            </v-col>

            <v-col cols="12">
              <v-text-field label="Email Adresse" required></v-text-field>
            </v-col>
          </v-row>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn block size="large" color="primary" text="Verbindlich Anmelden" variant="outlined" @click="dialog = false"></v-btn>
        </v-card-actions>

      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  data: () => ({
    dialog: false,

  }),
  props: [
    'event',
  ],
}
</script>