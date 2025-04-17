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

        <v-card-text v-if="step1">
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
        
        <v-divider v-if="step1"></v-divider>

        <v-card-text v-if="step1">
          <v-row dense>
            <v-col cols="12" v-if="step1 && error">
              <v-alert
                class="mb-5"
                density="compact"
                :text="response.status"
                title="Das hat nicht geklappt"
                type="warning"
              ></v-alert>
            </v-col>

            <v-col cols="12">
              <v-text-field v-model="name" :disabled="loading" label="Name" required></v-text-field>
            </v-col>

            <v-col cols="12">
              <v-text-field v-model="email" :disabled="loading" label="Email Adresse" required></v-text-field>
            </v-col>
          </v-row>
        </v-card-text>

        <v-divider v-if="step1"></v-divider>

        <v-card-actions v-if="step1">
          <v-spacer></v-spacer>
          <v-btn block size="large" color="primary" :loading="loading" text="Verbindlich Anmelden" variant="outlined" @click="register()"></v-btn>
        </v-card-actions>
        
        <v-card-text v-if="step2">
          <p>
            <b>Zeit:</b> {{ event.date }} {{ event.time }} <br/>
            <b>Ort:</b> {{ event.location }} <br/>
            <b>Zielgruppe:</b> {{ event.audience }} <br/>
            <b>Gebühr:</b> {{ event.price }} <br/>
          </p>
          <v-alert
            class="mb-5"
            density="compact"
            text="Du bist angemeldet! Wir haben dir eine Email mit den organisatorischen Details gesendet."
            title="Wir freuen uns auf dich"
            type="success"
          ></v-alert>
        </v-card-text>

      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from 'axios';

const email_pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,})$/;

const HTTP = axios.create({
  baseURL: '/api/',
  headers: {},
});

export default {
  data: () => ({
    dialog: false,
    loading: false,
    response: {},
    name: "",
    email: "",
  }),
  props: [
    'event',
  ],
  methods: {
    register: async function() {
      // better use if (!this.$refs.form.validate()) instead of the following manual checks
      if (this.name.length < 2) {
        this.response = {status: 'Bitte gib einen Namen an.'}
        return
      }
      if (!email_pattern.test(this.email || '')) {
        this.response = {status: 'Die Email-Adresse ist ungültig. Bitte überprüfe die eingegebene Adresse.'}
        return
      }
      let request = {
        name: this.name,
        addr: this.email,
        event: this.event,
      }
      this.loading = true // TODO contact server

      this.response = {}
      try {
        this.response = (await HTTP.post('anmeldung', request)).data
      } catch (ex) {
        this.response = {status: ex + ""}
      }
      this.loading = false;
    },
  },
  computed: {
    step1: function() {
      return this.response.status != 'success'
    },
    error: function() {
      return this.response.status != undefined && this.response.status != 'success'
    },
    step2: function() {
      return this.response.status == 'success'
    }
  },
}
</script>