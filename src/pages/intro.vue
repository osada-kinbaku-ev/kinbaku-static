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
      Die Einführungsveranstaltung dient als Grundlage für den <router-link to="training">Unterricht im Kinbaku Dojo Berlin</router-link>, kann aber auch als Schnupperkurs für fesselinteressierte wahrgenommen werden. Durch die Einführungsveranstaltung wollen wir sicherstellen, dass alle, die bei uns unterrichtet werden, über z.B.: sicherheitsrelevante Aspekte Informiert sind, aber auch vereinsinterne Regelungen kennen. Dies nimmt vorab etwas Zeit in Anspruch. Daher gliedern wir die Einführungsveranstaltung vom regulären Training ab. Die Einführungsveranstaltung ist die Voraussetzung um bei unserem Grundstufen Training teilnehmen zu können.
    </p>

    <p class="mt-3 text-center">
      Die Einführungsveranstaltung wird überwiegend frontal unterrichtet und unterscheidet sich daher vom üblichen Trainingskonzept. Wir nehmen uns etwas mehr Zeit - wir machen kurze Pausen - bringt euch gern einen Snack mit.
    </p>

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
          :expanded="Array.from(Array(intro_times.length))"
        >
          <template v-slot:item.controls="props">
            <EventRegister :event="props.item"></EventRegister>
          </template>
          <template v-slot:expanded-row="{columns, item}">
            <tr v-if="mobile" class="extension mt-0">
              <td :colspan="columns.length" class="pt-0 pb-0">{{ item.audience }}</td>
            </tr>
            <tr v-if="mobile" class="extension mt-0">
                <td :colspan="columns.length" class="pt-0 pb-2"><EventRegister :event="item"></EventRegister></td>
            </tr>
          </template>
        </v-data-table>
      </p>
    </v-container>
  </v-container>
  <v-container>
    <p class="mt-3 text-center">
      Die Einführungsveranstaltung wird in zwei Varianten angeboten.
    </p>

    <v-row>
      <v-col md="6" sm="12">
        <h2>Für Paare, die nicht switchen wollen</h2>
        <p>
          Anmeldung zu zweit mit fester Rollenverteilung während des Workshops, denn durch die relativ kurze Dauer des Workshops besteht keine Möglichkeit zu switchen.
        </p>
        <p>
          Der Workshop gliedert sich in einen Theorie- und einen Praxisteil. Der Theorieteil nimmt etwa zwei Stunden in Anspruch. Inhalte des Workshops:
        </p>

        <h3>Inhalte</h3>
        <ul>
          <li>Sicherheit und Consent</li>
          <li>Materialkunde</li>
          <li>Vereinsinfos und Trainingstermine</li>
          <li>Praxis: Single-column-tie</li>
          <li>Praxis: Double-column-tie</li>
          <li>Praxis: Strappado</li>
          <li>Einführung Fesselintensionen</li>
        </ul>

        <h3>Zielgruppe</h3>
        <p>
          Paare von zwei Personen (romantisch, intim oder nicht) mit für den Workshop festgelegter Rollenverteilung, die Fesseln ausprobieren möchten oder am Training teilnehmen möchten.
        </p>
      </v-col>

      <v-col md="6" sm="12">
        <h2>Für alle anderen</h2>
        <p>
          Anmeldung einzeln für alle die fesseln lernen möchten. Wenn ihr euch anmeldet, solltet ihr grundsätzlich bereit sein zu switchen (und beide Rollen einzunehmen) und Partnerübungen mit anderen aus der Gruppe durchzuführen.
        </p>
        <p>
          Der Workshop gliedert sich in einen Theorie- und einen Praxisteil. Der Theorieteil nimmt etwa zwei Stunden in Anspruch. Inhalte des Workshops:
        </p>

        <h3>Inhalte</h3>
        <ul>
          <li>Sicherheit und Consent</li>
          <li>Materialkunde</li>
          <li>Vereinsinfos und Trainingstermine</li>
          <li>Praxis: erste Knoten (einzeln)</li>
          <li>Kennenlernen und Consent</li>
          <li>Praxis: Single-column-tie (mit Partner)</li>
          <li>Praxis: Double-column-tie (mit Partner)</li>
          <li>Praxis: Strappado (mit Partner)</li>
        </ul>

        <h3>Zielgruppe</h3>
        <ul>
          <li>Fesselinteressierte Personen (ohne Vorkenntnisse)</li>
          <li>Personen (mit oder ohne Vorkenntnisse), die an unserem wöchentlichen Training teilnehmen möchten</li>
          <li>Paare die untereinander switchen wollen, aber nicht mit anderen Teilnehmern</li>
          <li>Paare die switchen wollen und gerne Übungen mit anderen Teilnehmern ausprobieren</li>
          <li>Paare die nicht switchen wollen, sich aber über die zusätzliche Übungszeit freuen</li>
        </ul>
      </v-col>
    </v-row>
  </v-container>

</template>

<script>
import EventRegister from '@/components/EventRegister.vue';
import {intro_times} from '@/data'
import { useDisplay } from 'vuetify'

export default {
  data: () => ({
    intro_times: intro_times,
    items: [
      {title: 'Sicherheit und Consent', text: 'Ein respektvolles Miteinander und gegenseitige Zustimmung sind essentiell für unsere Trainingskultur.'},
      {title: 'Materialkunde', text: 'Zuerst'},
      {title: 'Vereinsleben', text: 'Zuerst'},
      {title: 'Trainingsmethoden', text: 'Zuerst'},
      {title: 'Prüfungssystem', text: 'Zuerst'},
      {title: 'Praxis: Single Column Tie', text: 'Ihr lernt Elemente der ersten Stufe (Kyu9) in unserem Schulsystem kennen. Wir empfehlen diese Techniken in unseren Trainingsstunden zu vertiefen.'},
      {title: 'Demo', text: 'Kurze Demo, wie man die gelernten Elemente einsetzten könnte.'},
    ],
    mobile: useDisplay({ mobileBreakpoint: 700 }).mobile,
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
  computed: {
    intro_headers: function () {
      return this.mobile ?
      [
        {value: "date"},
        {value: "time"},
        {value: "location"},
      ] :
      [
        {value: "date"},
        {value: "time"},
        {value: "location"},
        {value: "audience"},
        {value: "controls"},
      ];
    },
  },
}
</script>

<style lang="css">
.v-table .v-table__wrapper > table > tbody > tr:not(:last-child):has(+tr.extension) > td {
  border-bottom: none;
}
</style>