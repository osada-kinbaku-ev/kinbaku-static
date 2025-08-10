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
    <h1 class="text-center mb-1">Über uns</h1>
    <p class="mt-3 text-center">
      Das Kinbaku Dojo Berlin lehrt die japanischen Fesselkünste Shibari (縛り, Festbinden, Fesseln) / Kinbaku (緊縛, straffes Festbinden) nach Osada-ryu (長田流).
      Wir sind davon überzeugt, dass niemand Shibari an einem Tag lernt.
      Unser regelmäßiges Training zielt darauf ab, das Handwerk hinter der Kunst zu verinnerlichen.
    </p>
    <p class="text-center mt-6">
      <v-btn
        to="vordemerstenbesuch"
        color="primary"
        variant="outlined"
        size="large"
        class="mb-3"
      >Vor dem ersten Besuch</v-btn>
    </p>
    <p class="text-center">
      <v-btn
        to="ueberuns"
        color="primary"
        variant="outlined"
        size="large"
        class="mb-3"
      >Mehr über uns</v-btn>
    </p>
  </v-container>
  <v-container fluid class="m-0 p-0" style="background: #eee;">
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

          <v-card-title v-if="event.date">{{ event.date }} {{ event.time }} Uhr</v-card-title>

          <v-card-actions>
            <EventRegister :event="event"></EventRegister>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <p class="text-center">
      <v-btn
        to="events"
        color="primary"
        variant="outlined"
        size="large"
        class="mb-3"
      >Alle Events</v-btn>
    </p>
  </v-container>
  <v-container>
    <h1 class="text-center mb-1">Trainingstermine</h1>
    <p class="my-8">
      <v-data-table class="text-center"
        style="background: transparent;"
        :items="training_times"
        hide-default-header
        hide-default-footer
      ></v-data-table>
    </p>
    <p class="text-center">
      <v-btn
        to="training"
        color="primary"
        variant="outlined"
        size="large"
        class="mb-3"
      >Anmelden</v-btn>
    </p>
  </v-container>
</template>

<script>
import VideoBackground from 'vue-responsive-video-background-player'
import video from '@/assets/rope.mp4'
import {events, intro_times, training_times} from '@/data'

export default {
  data: () => ({
    video: video,
    events: events.concat(intro_times),
    training_times,
  }),
  components: {
    VideoBackground,
  }
}
</script>
