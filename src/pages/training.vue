<template>
  <v-card tile elevation="16">
      <v-img
      cover
      max-height="240px"
      src="@/assets/dojo.jpg"
    ></v-img> 
  </v-card>
  <v-container>
    <h1 class="text-center mb-1">Trainingstermine</h1>
    <p class="mt-3 text-center">
      Bevor du beim Training fesseln kannst, musst du einen Einführungsworkshop besuchen.
    </p>
    <p class="my-8">
      <v-data-table class="text-center"
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
      >Anmeldung</v-btn>
    </p>
  </v-container>
  <v-container fluid style="background: #eee;">
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
  <v-container fluid>
    <h1 class="text-center mb-1">Vor dem ersten Besuch</h1>
    <v-row>
      <v-col cols="12" md="4" v-for="byg, idx in before_you_go">
        <v-card
          v-bind:key="idx"
          class="mx-auto my-3"
        >

          <v-card-item>
            <v-card-title>{{ byg.title }}</v-card-title>
          </v-card-item>

          <v-card-text>
            {{ byg.text }}
          </v-card-text>

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
    pattern: [
      {name: 'Einhandfesselung', level: '9. Kyu', subtitle: 'Single Column Tie', images: [image_single_column_tie], desc: 'Grundelement vieler Fesselungen, die um 9. Kyu intensiv geübt wird, um später sicheres und zügiges Fesseln von komplizierteren Mustern zu ermöglichen.'},
      {name: 'Strappado', level: '9. Kyu', subtitle: 'Armfesselung', images: [image_strappado, image_strappado2], desc: 'Einsteigerfesselung, die Schülern des 9. Kyu sowohl sichere und schnelle Handhabung des Seils als auch aufmerksamen Umgang mit der gefesselten Person näher bringt.'},
      {name: 'Takate Kote', level: '8. Kyu', subtitle: 'Oberkörperfesselung', images: [image_tk, image_tk2, image_tk3], desc: 'Als grundlegendes Element vieler Sessions wird beim TK auf Präzision beim Fesseln großer Wert gelegt. Diese Fesselung ist zentrales Element des 8. Kyu und bildet die Grundlage für Einsteigersuspensions.'},
    ],
    training_times: [
      {day: 'montags', time: '18.00 - 19.30', location: 'Kreuzberg'},
      {day: 'montags', time: '20.00 - 21.30', location: 'Kreuzberg'},
      {day: 'mittwochs', time: '18.00 - 19.30', location: 'Neukölln'},
      {day: 'mittwochs', time: '20.00 - 21.30', location: 'Neukölln'},
      {day: 'donnerstag', time: '18.00 - 21.30', location: 'Pankow'},
    ],
    before_you_go: [
      {title: 'Atmosphäre', text: 'Unsere Trainings sind kein Playspace und zielen auf eine sportlich formale und technische Atmosphäre ab.'},
      {title: 'Vorkenntnisse', text: 'Bevor du beim Training fesseln kannst, musst du den Einführungsworkshop besuchen.  Begleitet Ihr jemanden zum Training als zu fesselnde Person, müsst Ihr den Einführungs-Workshop selbst nicht besucht haben. Andere Vorkenntnisse werden vorausgesetzt.'},
      {title: 'Bekleidung', text: 'Daher trainieren wir in sportlicher Kleidung ohne Schuhe. Trainiert wird barfuß oder in Socken. Wir bitten Euch, auf Straßenkleidung zu verzichten. Kommt in bequemer sportlicher Kleidung, idealerweise enganliegend. T-Shirt und Hose sind gut geeignet.'},
      {title: 'Individuelles Lernen', text: 'Es ist Gruppenunterricht, aber alle lernen in ihrem eigenen Tempo. Unterschiedliche Level trainieren nebeneinander. Unsere Trainerinnen und Trainer korrigieren im direkten Kontakt, geben Tipps zu Technik und Körperhaltung und wiederholen die Elemente mit Euch oder zeigen den nächsten Schritt.'},
      {title: 'Seile', text: 'Ihr könnt anfangs Seile von uns leihen. Wir fesseln ausschließlich mit Juteseilen (oder Hanfseilen). Diese müssen jedoch vorher aufwändig bearbeitet werden. Es ist sinnvoll, dass Ihr verschiedene Seile in die Hand nehmt, bevor Ihr eine Kaufentscheidung trefft. Im Training könnt Ihr viele verschiedene Seiltypen sehen und andere Lernende fragen, ob Ihr deren Seile einmal ausprobieren könnt. Verschiedene Personen haben unterschiedliche Vorlieben, was das richtige Seil betrifft und können Euch Tipps geben. '},
      {title: 'Absage', text: 'Um Euch Kosten zu ersparen, versuchen wir, die frei werdenden Plätze aufzufüllen. Trainings finden in Mieträumen statt. Daher bitten wir um Euer Verständnis, dass wir bei kurzfristiger Absage keine Rückerstattung ermöglichen können. Bitte halte eine Frist von mindestens 24 Stunden für eine Absage ein. '},
    ]
  }),
  components: {
    VideoBackground,
  }
}
</script>
