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


def template_email_register_participant(event: dict) -> tuple[str, str]:
    title = event.get("title", "<kein Name>")
    return (
        f"Registrierung für {title} bestätigt",
        f"Hallo,\n"
        f"vielen Dank für eine Anmeldung zu {event.get('title', '<kein Name>')}.",
    )


def template_email_register_event_admin(
    addr: str, name: str, event: dict
) -> tuple[str, str]:
    title = event.get("title", "<kein Name>")
    return (
        f"Registrierung für {title}",
        f"Hallo,\n" f"{name} <{addr}> hat sich soeben zu {title} angemeldet.\n",
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


def register(addr: str, name: str, event: dict) -> dict:
    """
    Register participant identified by `email` and `name` to the `event`.

    Sends to emails:
    1. Email to event admin (environment config `EVENT_ADMIN_EMAIL_ADDR`)
    2. Email to participant (`email`)

    If either fails, an exception is raised.
    """
    if not name:
        return dict(status="Name für Anmeldung benötigt.")
    if not addr:
        return dict(status="Email-Adresse für Anmeldung benötigt.")
    if not event:
        return dict(status="Event-Information für Anmeldung benötigt.")

    email(addr, *template_email_register_participant(event))
    email(
        EVENT_ADMIN_EMAIL_ADDR, *template_email_register_event_admin(addr, name, event)
    )
    return dict(status="success")


def process_request(query: str, post_data) -> dict:
    match query:
        case "anmeldung":
            post_data = post_data or {}
            addr = post_data.get("addr")
            name = post_data.get("name")
            event = post_data.get("event", {})
            return register(addr, name, event)
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
