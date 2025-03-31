<template>
  <v-card tile elevation="16">
      <v-img
      cover
      max-height="240px"
      src="@/assets/dojo.jpg"
    ></v-img> 
  </v-card>
  <v-container>
    <h1 class="text-center mb-1">Einführungsworkshops</h1>
    <p class="mt-3 text-center">
      Die Einführungsveranstaltung dient als Grundlage für den <router-link to="training">Unterricht im Kinbaku Dojo Berlin</router-link>, kann aber auch eigenständig als Workshop für Fesselinteressierte wahrgenommen werden. Durch die Einführungsveranstaltung wollen wir sicherstellen, dass alle, die bei uns unterrichtet werden, über sicherheitsrelevante Aspekte informiert sind, aber auch vereinsinterne Regelungen kennen. Dies nimmt vorab etwas Zeit in Anspruch. Daher gliedern wir die Einführungsveranstaltung vom regulären Training ab. Die Einführungsveranstaltung ist die Voraussetzung, um an unserem Training für die Grundstufe teilnehmen zu können.
    </p>

    <p class="mt-3 text-center">
      Die Einführungsveranstaltung wird überwiegend frontal unterrichtet und unterscheidet sich daher sehr vom üblichen Trainingskonzept. Wir nehmen uns also etwas mehr Zeit - wir machen kurze Pausen - bringt Euch also gern einen Snack mit.
    </p>

    <v-timeline align="start" class="mt-4" side="end">
      <v-timeline-item
        v-for="(item, i) in items"
        :key="i"
        fill-dot
      >
        <v-card>
          <v-card-title :class="['text-h6', `bg-${item.color}`]">
            {{ item.title }}
          </v-card-title>
          <v-card-text class="bg-white text--primary">
            <p>{{ item.text }}</p>
          </v-card-text>
        </v-card>
      </v-timeline-item>
    </v-timeline>
  </v-container>
  <v-container class="m-0 p-0" fluid style="background: #eee;">
    <v-container>
      <h1 class="text-center mb-5">Termine</h1>
      <p class="text-center">
        <v-data-table 
          style="background: transparent;" 
          class="text-center"
          :items="intro_times"
          :headers="intro_headers"
          hide-default-header
          hide-default-footer
        >
          <template v-slot:item.controls="props">
            <EventRegister :event="props.item"></EventRegister>
          </template>    
        </v-data-table>
      </p>
    </v-container>
  </v-container>
  <v-container>
    <h1 class="text-center mb-1">Vor dem Besuch</h1>
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
import EventRegister from '@/components/EventRegister.vue';

export default {
  data: () => ({
    intro_times: [
      {date_string: '22 Mar 2025', time: '12.00 - 20.00', title: 'Einführungsworkshop', location: 'Kinbaku Dojo Binzstraße', audience: 'Einzelpersonen und Switcherpaare', href: 'https://www.joyclub.de/event/1688912.shibari_einfuehrungsworkshop_einzel_switcher_berli.html'},
      {date_string: '12 Apr 2025', time: '12.00 - 20.00', title: 'Einführungsworkshop', location: 'Kinbaku Dojo Binzstraße', audience: 'Einzelpersonen und Switcherpaare', href: 'https://www.joyclub.de/event/1688913.shibari_einfuehrungsworkshop_einzel_switcher_berli.html'},
      {date_string: '26 Apr 2025', time: '12.00 - 20.00', title: 'Einführungsworkshop', location: 'Kinbaku Dojo Binzstraße', audience: 'Einzelpersonen und Switcherpaare', href: 'https://www.joyclub.de/event/1688914.shibari_einfuehrungsworkshop_einzel_switcher_berli.html'},
      {date_string: '10 May 2025', time: '12.00 - 20.00', title: 'Einführungsworkshop', location: 'Kinbaku Dojo Binzstraße', audience: 'Einzelpersonen und Switcherpaare', href: 'https://www.joyclub.de/event/1688916.shibari_einfuehrungsworkshop_einzel_switcher_berli.html'},
    ],
    intro_headers: [
      {value: "date"},
      {value: "time"},
      {value: "location"},
      {value: "audience"},
      {value: "controls"},
    ],
    before_you_go: [
      {title: 'Atmosphäre', text: 'Die Einführungsworkshops sind kein Playspace und zielen auf eine sportlich formale und technische Atmosphäre ab.'},
      {title: 'Vorkenntnisse', text: 'Der Einführungsworkshop benötigt keine Vorkenntnisse. Auch Personen mit Vorkenntnissen sind willkommen!'},
      {title: 'Bekleidung', text: 'Wir bitten Euch, auf Straßenkleidung zu verzichten. Kommt in bequemer sportlicher Kleidung, idealerweise enganliegend. T-Shirt und Hose sind gut geeignet.'},
      {title: 'Seile', text: 'Ihr könnt Seile von uns leihen. Wir fesseln ausschließlich mit Juteseilen (oder Hanfseilen). Diese müssen jedoch vorher aufwändig bearbeitet werden. Es ist sinnvoll, dass Ihr verschiedene Seile in die Hand nehmt, bevor Ihr eine Kaufentscheidung trefft. Im Training könnt Ihr viele verschiedene Seiltypen sehen und andere Lernende fragen, ob Ihr deren Seile einmal ausprobieren könnt. Verschiedene Personen haben unterschiedliche Vorlieben, was das richtige Seil betrifft und können Euch Tipps geben. '},
      {title: 'Absage', text: 'Um Euch Kosten zu ersparen, versuchen wir, die frei werdenden Plätze aufzufüllen. Trainings finden in Mieträumen statt. Daher bitten wir um Euer Verständnis, dass wir bei kurzfristiger Absage keine Rückerstattung ermöglichen können. Bitte halte eine Frist von mindestens 24 Stunden für eine Absage ein. '},
    ],
    items: [
      {title: 'Sicherheit und Consent', text: 'Ein respektvolles Miteinander und gegenseitige Zustimmung sind essentiell für unsere Trainingskultur.'},
      {title: 'Materialkunde', text: 'Zuerst'},
      {title: 'Vereinsleben', text: 'Zuerst'},
      {title: 'Trainingsmethoden', text: 'Zuerst'},
      {title: 'Prüfungssystem', text: 'Zuerst'},
      {title: 'Praxis: Single Column Tie', text: 'Ihr lernt Elemente der ersten Stufe (Kyu9) in unserem Schulsystem kennen. Wir empfehlen diese Techniken in unseren Trainingsstunden zu vertiefen.'},
      {title: 'Demo', text: 'Kurze Demo, wie man die gelernten Elemente einsetzten könnte.'},
    ]
  }),
  components: {
  },
  mounted: function() {
    let date_locale_options = {
      weekday: 'short',
      month: 'numeric',
      day: 'numeric',
      year: 'numeric',
    }
    for (const d of this.intro_times) {
      d.date = new Date(Date.parse(d.date_string)).toLocaleDateString("de-DE", date_locale_options)
    }
  },  
}
</script>
