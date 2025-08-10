<template>
  <v-img
    cover
    max-height="240px"
    src="@/assets/dojo.jpg"
    class="mb-4"
  ></v-img>

  <v-container v-if="events.length == 0">
    <h1>Keine Events geplant! 😭</h1>
    <p class="text-center">Manche Events werden nur bei Joyclub angekündigt.</p>
    <p class="text-center mt-4">
      <v-btn
          href="https://www.joyclub.de/party/veranstaltungen/4277291.kinbaku_dojo_berlin.html"
          color="primary"
          variant="outlined"
          size="large"
          class="mb-3"
        >Bei Joyclub suchen</v-btn>
    </p>
  </v-container>

  <v-container>
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
import {events} from '@/data'

export default {
  data: () => ({
    events: events,
    date_locale_options: {
      weekday: 'short',
      month: 'numeric',
      day: 'numeric',
    }
  }),
  mounted: function() {
    for (const d of this.events) {
      d.date = new Date(Date.parse(d.date_string));
    }
  },
}
</script>
