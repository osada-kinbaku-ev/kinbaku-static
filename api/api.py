#!/usr/bin/env python3
# <?php  # just in case

import os
import json
import sys
import smtplib
from email.message import EmailMessage

try:
    with open(".env") as f:
        for line in f.read().split("\n"):
            if line.strip():
                k, v = line.strip().split("=", 1)
                os.environ[k] = v
except FileNotFoundError:
    pass


EVENT_ADMIN_EMAIL_ADDR = os.environ["KINBAKU_EVENT_ADMIN_EMAIL_ADDR"]


def template_email_register_participant(people_num: int, event: dict) -> tuple[str, str]:
    event_str = event.get("title", "<kein Name>") + f" ({event.get('date_string', '')} {event.get('time', '')})"
    return (
        f"Registrierung für {event_str} bestätigt",
        f"Hallo,\n"
        f"vielen Dank für deine Anmeldung von {people_num} Person(en) zu {event_str}."
        f"\n\n"
        f"Um Euch Kosten zu ersparen, versuchen wir, die frei werdenden Plätze aufzufüllen. "
        f"Die Workshops finden in Mieträumen statt. "
        f"Daher bitten wir um Euer Verständnis, dass wir bei kurzfristiger Absage keine Rückerstattung ermöglichen können. "
        f"Bitte halte eine Frist von mindestens 24 Stunden für eine Absage ein. "
        f"\n"
        f"Dein Team vom Osada Kinbaku Dojo\n\n"
        f"--\n"
        f"Osada Kinbaku Dojo e.V. · Binzstraße 64 · 13189 Berlin-Pankow\n"
        f"\n"
        f"Vorstandsvorsitz: Alexander Esser\n"
        f"Registergericht: AG Berlin (Charlottenburg) VR 29488 B\n"
    )


def template_email_register_event_admin(
    names: list[str], people_num: int, addr: str, comment: str, event: dict
) -> tuple[str, str]:
    event_str = event.get("title", "<kein Name>") + f" ({event.get('date_string', '')} {event.get('time', '')})"
    return (
        f"Registrierung für {event_str}",
        f"Hallo,\n"
        f"{people_num} Person(en) haben sich mit der Adresse {addr} soeben zu {event_str} angemeldet. Namen:\n\n"
        + ", ".join(names) +
        "\n\nKommentar:\n\n"
        + comment +
        "\n\nEvent details:\n\n"
        + json.dumps(event, indent=4, ensure_ascii=False)
    )


def email(recp: str, subject: str, body: str) -> None:
    msg = EmailMessage()
    msg["From"] = EVENT_ADMIN_EMAIL_ADDR
    msg["To"] = recp
    msg["Subject"] = subject
    msg.set_content(body)

    s = smtplib.SMTP("localhost")
    s.send_message(msg)
    s.quit()


def register(names: list[str], people_num: int, addr: str, comment: str, event: dict) -> dict:
    """
    Register `people_num` participant(s) identified by `email` and `names` to the `event`.

    Sends to emails:
    1. Email to event admin (environment config `EVENT_ADMIN_EMAIL_ADDR`)
    2. Email to participant (`email`)

    If either fails, an exception is raised.
    """
    if people_num < 1 or people_num > 10:
        return dict(status="Anzahl angemeldeter Personen inkorrekt.")
    if len(names) < people_num or any(n == "" for n in names[:people_num]):
        return dict(status="Alle Namen werden für die Anmeldung benötigt.")
    if not addr:
        return dict(status="Email-Adresse für Anmeldung benötigt.")
    if not event:
        return dict(status="Event-Information für Anmeldung benötigt.")

    email(addr, *template_email_register_participant(people_num, event))
    email(
        EVENT_ADMIN_EMAIL_ADDR, *template_email_register_event_admin(names, people_num, addr, comment, event)
    )
    return dict(status="success")


def process_request(query: str, post_data) -> dict:
    match query:
        case "anmeldung":
            post_data = post_data or {}
            names = post_data.get("names", [])
            people_num = post_data.get("people_num", 0)
            addr = post_data.get("addr")
            comment = post_data.get("comment")
            event = post_data.get("event", {})

            return register(names, people_num, addr, comment, event)
        case _:
            return dict(error=f"unknown query `{query}`")


try:
    stdin = sys.stdin.read()
    output_dict = process_request(
        query=os.environ.get("QUERY"),
        post_data=json.loads(stdin) if stdin else None,
    )
    output = json.dumps(output_dict)
    print(output)
    exit(0 if output_dict.get("status") == "success" else 2)
except Exception as e:
    output = json.dumps(dict(status="exception: " + repr(e)))
    print(output)
    exit(1)
