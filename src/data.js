import image_tk from '@/assets/tk.jpg'
import image_tk2 from '@/assets/tk2.jpg'
import image_tk3 from '@/assets/tk3.jpg'
import image_strappado from '@/assets/strappado.jpg'
import image_strappado2 from '@/assets/strappado2.jpg'
import image_single_column_tie from '@/assets/single-column-tie.jpg'

export let events = [
        // {title: 'Einführung', date_string: '22 Mar 2025', time: '12-20', location: 'Kinbaku Dojo Binzstraße', audience: 'Für Singles und Paare', image: image_strappado, short_text: 'Einführung in das Training im Dojo, für Einzelpersonen und Switcherpaare. Der Workshop ist für Einzelpersonen die fesseln lernen möchten umgestellt. Wenn ihr euch anmeldet, solltet ihr grundsätzlich bereit sein zu switchen und Partnerübungen mit Teilnehmer:innnen aus der Gruppe durchzuführen.', sign_up_url: 'https://www.joyclub.de/event/1688912.shibari_einfuehrungsworkshop_einzel_switcher_berli.html'},
        // {title: 'Tag des offenen Bondage', date_string: '29 Mar 2025', time: '11', location: 'sinberlin Berlin-Kreuzberg', audience: 'Für alle', image: image_tk, short_text: 'Der Tag des offenen Bondage wurde 2016 durch Ater Crudus ins Leben gerufen. Er bietet Vereinen, Treffs, Clubs und anderen Gruppen, die sich mit Shibari oder Kinbaku auseinandersetzen, die Möglichkeit ihre Türen fuer Interessierte und Neugierige zu öffnen.', sign_up_url: 'https://www.joyclub.de/event/1688042.tag_des_offenen_bondage_berlin_kreuzberg.html'},
        // {title: 'Tag des offenen Bondage - Party', date_string: '29 Mar 2025', time: '20', location: 'sinberlin Berlin-Kreuzberg', audience: 'Für alle', image: image_tk2, short_text: 'Wir lassen den Tag mit einer Bondage Party im Sin Berlin ausklingen. Der Eintritt kostet 15€, alkoholfreie Getränke sind im Eintritt enthalten. Ihr könnt den Abend zum Fesseln, für Sessions oder zum Üben nutzen. Einige unserer Schüler*innen werden vor Ort sein, sodass auch weiterhin Fragen zum Verein gestellt werden können.', sign_up_url: 'https://www.joyclub.de/event/1688069.tag_des_offenen_bondage_party_berlin.html'},
    ];

export let intro_times =  [
    {
        date_string: '09 Aug 2025', time: '12.00 - 20.00',
        title: 'Einführungsworkshop',
        location: 'Kinbaku Dojo Binzstraße',
        audience: 'Einzelpersonen und Switcherpaare',
        action: 'Anmelden',
        href: 'https://www.joyclub.de/event/1688919.shibari_einfuehrungsworkshop_einzel_switcher_berli.html',
        fee_eur_per_person: 40.00,
        people_min: 1,
        people_max: 2,
        image: image_single_column_tie,
    },
    {
        date_string: '30 Aug 2025', time: '12.00 - 18.30',
        title: 'Einführungsworkshop für Paare',
        location: 'Kinbaku Dojo Binzstraße',
        audience: 'Paare',
        action: 'Als Paar anmelden',
        href: 'https://www.joyclub.de/event/1688937.shibari_einfuehrungsworkshop_paare_berlin.html',
        fee_eur_per_person: 32.50,
        people_min: 2,
        people_max: 2,
        image: image_strappado,
    },
  ];

  export let before_you_go = [
    {title: 'Atmosphäre', text: 'Die Workshops und Trainings sind kein Playspace und zielen auf eine sportlich formale und technische Atmosphäre ab.'},
    {title: 'Vorkenntnisse', text: 'Der Einführungsworkshop benötigt keine Vorkenntnisse. Auch Personen mit Vorkenntnissen sind willkommen! Um beim Training zu fesseln, musst du vorher den Einführungsworkshop besucht haben.'},
    {title: 'Bekleidung', text: 'Wir bitten Euch, auf Straßenkleidung zu verzichten. Kommt in bequemer sportlicher Kleidung, idealerweise enganliegend. T-Shirt und Hose sind gut geeignet.'},
    {title: 'Seile', text: 'Ihr könnt Seile von uns leihen. Wir fesseln ausschließlich mit Juteseilen (oder Hanfseilen). Diese müssen jedoch vorher aufwändig bearbeitet werden. Es ist sinnvoll, dass Ihr verschiedene Seile in die Hand nehmt, bevor Ihr eine Kaufentscheidung trefft. Im Training könnt Ihr viele verschiedene Seiltypen sehen und andere Lernende fragen, ob Ihr deren Seile einmal ausprobieren könnt. Verschiedene Personen haben unterschiedliche Vorlieben, was das richtige Seil betrifft und können Euch Tipps geben. '},
    {title: 'Absage', text: 'Um Euch Kosten zu ersparen, versuchen wir, die frei werdenden Plätze aufzufüllen. Trainings finden in Mieträumen statt. Daher bitten wir um Euer Verständnis, dass wir bei kurzfristiger Absage keine Rückerstattung ermöglichen können. Bitte halte eine Frist von mindestens 24 Stunden für eine Absage ein. '},
  ];
