<template>
  <div class="text-center pa-4">
    <v-dialog v-model="dialog" transition="dialog-bottom-transition" :fullscreen="$vuetify.display.mobile" max-width="600">
      <template v-slot:activator="{ props: activatorProps }">
        <v-btn fab dark small color="primary" variant="outlined" :text="event.action" v-bind="activatorProps"></v-btn>
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
            <b>Gebühr:</b> {{ event.fee_eur_per_person * people_num }} EUR <br/>
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
              <v-btn-toggle
                variant="outlined"
                v-model="people_num"
                divided
              >
                <v-btn v-for="num in Array.from(Array(event.people_max + 1).keys()).slice(event.people_min)" :value="num">{{ num }} Person{{ num > 1 ? 'en' : '' }}</v-btn>
              </v-btn-toggle>
            </v-col>

            <v-col cols="12" v-for="idx in people_num">
              <v-text-field v-model="names[idx-1]" :disabled="loading" :label="'Name ' + idx" required></v-text-field>
            </v-col>

            <v-col cols="12">
              <v-text-field v-model="email" :disabled="loading" label="Email Adresse" required></v-text-field>
            </v-col>

            <v-col cols="12">
              <v-text-field v-model="comment" :disabled="loading" label="Kommentar"></v-text-field>
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
            text="Du bist auf der Warteliste! Wir melden uns bei dir mit den organisatorischen Details gesendet."
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
    names: [],
    comment: "",
    email: "",
    people_num: 1,
  }),
  props: [
    'event',
  ],
  methods: {
    register: async function() {
      // better use if (!this.$refs.form.validate()) instead of the following manual checks
      for (let i = 0; i < this.people_num; i++) {
        if (this.names[i].length == 0) {
          this.response = {status: `Bitte gib alle Namen an. (${i})`}
          return
        }
      }
      if (!email_pattern.test(this.email || '')) {
        this.response = {status: 'Die Email-Adresse ist ungültig. Bitte überprüfe die eingegebene Adresse.'}
        return
      }
      let request = {
        names: this.names,
        people_num: this.people_num,
        addr: this.email,
        comment: this.comment,
        event: this.event,
      }
      this.loading = true

      this.response = {}
      try {
        this.response = (await HTTP.post('anmeldung', request)).data
      } catch (ex) {
        this.response = {status: ex + ""}
      }
      this.loading = false;
    },
  },
  mounted: function() {
    this.people_num = Math.min(Math.max(1, this.event.people_min), this.event.people_max)
    this.names = Array(this.event.people_max).fill("")
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