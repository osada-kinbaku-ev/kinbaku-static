<template>
  <v-card tile elevation="16">
    <video-background 
      :src="video"
      style="max-height: 400px; height: 100vh;"
      >
        <div class="px-10" style="color: white;">
          <h1 style="color: white; font-size: 50px; margin-top: 20px">Shibari lernen</h1>
          <strong>Das Osada Kinbaku Dojo Berlin unterrichten Shibari an fünf wöchtenlichen Terminen und veranstaltet Workshops und Events.</strong>
          <p class="mt-15">
            <v-btn 
              class="mr-5 mb-5"
              variant="outlined" 
              to="intro"
              append-icon="mdi-chevron-right">
              Einführungsveranstaltung
            </v-btn>
            <v-btn 
              class="mb-5"
              variant="outlined" 
              to="training"
              append-icon="mdi-chevron-right">
              Training
            </v-btn>            
          </p>
        </div>
    </video-background>
  </v-card>
  <v-container fluid>
    <h2 class="text-center mb-0">Aktuelle Workshops und Events</h2>
    <v-row>
      <v-col cols="12" md="4" v-for="event, idx in events">
        <v-card
          v-bind:key="idx"
          class="mx-auto my-12"
        >

          <v-img
            height="250"
            :src="event.image"
            cover
          ></v-img>

          <v-card-item>
            <v-card-title>{{ event.title }}</v-card-title>

            <v-card-subtitle>
              <span class="me-1">{{ event.audience }}</span>

            </v-card-subtitle>
          </v-card-item>

          <v-card-text>

            <div class="mb-3 text-subtitle-1">
              <v-icon
                icon="mdi-map-marker"
                size="small"
              ></v-icon>
              {{ event.location }}
            </div>

            <div>{{ event.short_text }}</div>
          </v-card-text>

          <v-divider class="mx-4 mb-1"></v-divider>

          <v-card-title v-if="event.date">{{ event.date.toLocaleDateString("de-DE", date_locale_options) }} {{ event.time }} Uhr</v-card-title>

          <v-card-actions>
            <v-btn
              color="deep-purple-lighten-2"
              text="Anmelden"
              block
              border
              :href="event.sign_up_url"
            ></v-btn>
          </v-card-actions>
        </v-card>
      </v-col>  
    </v-row>
  </v-container>

</template>

<script>
import VideoBackground from 'vue-responsive-video-background-player'
import video from '@/assets/rope.mp4'
import image_tk from '@/assets/tk.jpg'
import image_tk2 from '@/assets/tk2.jpg'
import image_tk3 from '@/assets/tk3.jpg'
import image_strappado from '@/assets/strappado.jpg'
import image_strappado2 from '@/assets/strappado2.jpg'
import image_single_column_tie from '@/assets/single-column-tie.jpg'

export default {
  data: () => ({
    video: video,
    events: [
      {title: 'Einführung', date_string: '22 Mar 2025', time: '12-20', location: 'Kinbaku Dojo Binzstraße', audience: 'Für Singles und Paare', image: image_strappado, short_text: 'Einführung in das Training im Dojo, für Einzelpersonen und Switcherpaare. Der Workshop ist für Einzelpersonen die fesseln lernen möchten umgestellt. Wenn ihr euch anmeldet, solltet ihr grundsätzlich bereit sein zu switchen und Partnerübungen mit Teilnehmer:innnen aus der Gruppe durchzuführen.', sign_up_url: 'https://www.joyclub.de/event/1688912.shibari_einfuehrungsworkshop_einzel_switcher_berli.html'},
      {title: 'Tag des offenen Bondage', date_string: '29 Mar 2025', time: '11', location: 'sinberlin Berlin-Kreuzberg', audience: 'Für alle', image: image_tk, short_text: 'Der Tag des offenen Bondage wurde 2016 durch Ater Crudus ins Leben gerufen. Er bietet Vereinen, Treffs, Clubs und anderen Gruppen, die sich mit Shibari oder Kinbaku auseinandersetzen, die Möglichkeit ihre Türen fuer Interessierte und Neugierige zu öffnen.', sign_up_url: 'https://www.joyclub.de/event/1688042.tag_des_offenen_bondage_berlin_kreuzberg.html'},
      {title: 'Tag des offenen Bondage - Party', date_string: '29 Mar 2025', time: '20', location: 'sinberlin Berlin-Kreuzberg', audience: 'Für alle', image: image_tk2, short_text: 'Wir lassen den Tag mit einer Bondage Party im Sin Berlin ausklingen. Der Eintritt kostet 15€, alkoholfreie Getränke sind im Eintritt enthalten. Ihr könnt den Abend zum Fesseln, für Sessions oder zum Üben nutzen. Einige unserer Schüler*innen werden vor Ort sein, sodass auch weiterhin Fragen zum Verein gestellt werden können.', sign_up_url: 'https://www.joyclub.de/event/1688069.tag_des_offenen_bondage_party_berlin.html'},
    ],
    date_locale_options: {
      weekday: 'short',
      month: 'numeric',
      day: 'numeric',
    },
  }),
  mounted: function() {
    for (const d of this.events) {
      d.date = new Date(Date.parse(d.date_string));
    }
  },
  components: {
    VideoBackground,
  }
}
</script>
