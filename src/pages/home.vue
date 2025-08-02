<template>
  <v-card tile elevation="16">
    <video-background
      :src="video"
      style="height: 70vh;"
      >
      <v-container>
        <div class="px-10" style="color: white;">
          <h1 style="color: white; font-size: 50px; margin-top: 20px">Shibari lernen</h1>
          <strong>Das Osada Kinbaku Dojo Berlin unterrichtet Shibari an fünf wöchtenlichen Terminen und veranstaltet Workshops sowie Events.</strong>
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
      </v-container>
    </video-background>
  </v-card>
  <v-container>
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
import {events} from '@/data'

export default {
  data: () => ({
    video: video,
    events: events,
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
