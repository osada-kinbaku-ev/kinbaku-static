<template>
  <v-card tile elevation="16">
      <v-img
      cover
      max-height="240px"
      src="@/assets/dojo.jpg"
    ></v-img>
  </v-card>
  <v-container>
    <p class="mt-3 text-center">
      Das Kinbaku Dojo Berlin lehrt die japanischen Fesselkünste Shibari (縛り, Festbinden, Fesseln) / Kinbaku (緊縛, straffes Festbinden) nach Osada-ryu (長田流).
    </p>
    <p class="mt-3 text-center">
        Der Eingetragene Verein besteht bereits seit 2010 und war das erste Dojo Europas dieser Art.
        Unser Training zielt darauf ab, das Handwerk hinter der Kunst zu verinnerlichen.
        Dafür bieten wir eine sehr hohe Regelmäßigkeit an Trainings pro Woche,
        welche unter Aufsicht von erfahrenen Trainern und Trainerinnen stattfinden und individuell besucht werden können.
    </p>
    <p class="mt-3 text-center">
        Wir sind davon überzeugt, dass niemand Shibari an einem Tag lernt.
        Bis man Handgriffe flüssig und sicher reproduzieren kann, werden Wiederholung benötigt und Fehler,
        welche sich manchmal unbemerkt mit der Zeit einschleichen sollten regelmäßig korrigiert werden.
    </p>
  </v-container>
  <v-container fluid class="m-0 p-0" style="background: #eee;">
    <h1 class="text-center mb-1">Trainingstermine</h1>
    <p class="mt-3 text-center">
      Bevor du beim Training fesseln kannst, musst du einen
      <router-link to="intro">Einführungsworkshop</router-link> besuchen. Alle Teilnehmer müssen die <router-link to="vereinsregeln">Vereinsregeln</router-link> kennen.
    </p>
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
        href="https://www.joyclub.de/party/veranstaltungen/4277291.kinbaku_dojo_berlin.html"
        color="primary"
        variant="outlined"
        size="large"
        class="mb-3"
      >Anmeldung über Joyclub</v-btn>
      <v-btn
        href="mailto:info@kinbaku-berlin.de?subject=Anmeldung Training&body=Bitte folgende Felder ausfüllen%0D%0A%0D%0AName(n): <bitte ausfüllen>%0D%0ADatum und Uhrzeit: <TT.MM.YYYY> um <HH:MM> Uhr ggf. und <HH:MM> Uhr%0D%0A%0D%0ABitte nicht ändern:%0D%0A%0D%0APersonen: 2%0D%0AKosten: 20 EUR%0D%0A%0D%0A"
        color="primary"
        variant="outlined"
        size="large"
        class="ml-3 mb-3"
      >Anmeldung per Email</v-btn>
    </p>
  </v-container>
  <!-- <v-container fluid class="m-0 p-0" style="background: #eee;">
    <v-container>
      <h1 class="text-center mb-1">Trainingsinhalte</h1>
      <v-row>
        <v-col cols="12" md="4" v-for="p, idx in pattern">
          <v-card
            v-bind:key="idx"
            class="mx-auto my-3"
          >

            <v-carousel height="250" :show-arrows="p.images.length > 1">
              <v-carousel-item
                v-for="image, idx in p.images" v-bind:key="idx"
                :src="image"
                height="250"
                cover
              ></v-carousel-item>
            </v-carousel>

            <v-card-item>
              <v-card-title>{{ p.name }}</v-card-title>

              <v-card-subtitle>
                <span class="me-1">{{ p.subtitle }}</span>

              </v-card-subtitle>
            </v-card-item>

            <v-card-text>

              <div class="mb-3 text-subtitle-1">
                <v-icon
                  icon="mdi-stairs"
                  size="small"
                ></v-icon>
                {{ p.level }}
              </div>

              <div>{{ p.desc }}</div>
            </v-card-text>

          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-container> -->
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
import { training_times } from '@/data'

export default {
  data: () => ({
    video: video,
    pattern: [
      {name: 'Einhandfesselung', level: '9. Kyu', subtitle: 'Single Column Tie', images: [image_single_column_tie], desc: 'Grundelement vieler Fesselungen, die um 9. Kyu intensiv geübt wird, um später sicheres und zügiges Fesseln von komplizierteren Mustern zu ermöglichen.'},
      {name: 'Strappado', level: '9. Kyu', subtitle: 'Armfesselung', images: [image_strappado, image_strappado2], desc: 'Einsteigerfesselung, die Schülern des 9. Kyu sowohl sichere und schnelle Handhabung des Seils als auch aufmerksamen Umgang mit der gefesselten Person näher bringt.'},
      {name: 'Takate Kote', level: '8. Kyu', subtitle: 'Oberkörperfesselung', images: [image_tk, image_tk2, image_tk3], desc: 'Als grundlegendes Element vieler Sessions wird beim TK auf Präzision beim Fesseln großer Wert gelegt. Diese Fesselung ist zentrales Element des 8. Kyu und bildet die Grundlage für Einsteigersuspensions.'},
    ],
    training_times,
  }),
  components: {
    VideoBackground,
  }
}
</script>
