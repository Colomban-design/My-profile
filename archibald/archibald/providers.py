"""Canaux sortants : SMS, appel vocal, e-mail des fiches.

Le prototype n'envoie rien pour de vrai : chaque fournisseur « console » garde ce
qu'il aurait envoyé dans une liste `sent`, que la démo affiche et que les tests
vérifient. Pour la production, implémenter les mêmes méthodes avec l'opérateur
SMS/voix choisi (numéros français, voix IA en français à faible latence).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


class SmsProvider(Protocol):
    def send(self, to: str, text: str) -> None: ...


class VoiceProvider(Protocol):
    def start_call(self, to: str, lead_id: str) -> None: ...


class Mailer(Protocol):
    def send(self, to: str, subject: str, body: str) -> None: ...


@dataclass
class ConsoleSms:
    sent: list[tuple[str, str]] = field(default_factory=list)
    echo: bool = False

    def send(self, to: str, text: str) -> None:
        self.sent.append((to, text))
        if self.echo:
            print(f"  [SMS → {to}] {text}")


@dataclass
class ConsoleVoice:
    """Déclenche l'appel. En production : opérateur voix + transcription en direct,
    et le même `Qualifier` que le canal écrit produit chaque réplique."""

    calls: list[tuple[str, str]] = field(default_factory=list)
    echo: bool = False

    def start_call(self, to: str, lead_id: str) -> None:
        self.calls.append((to, lead_id))
        if self.echo:
            print(f"  [APPEL → {to}] (lead {lead_id}) — simulé ici par écrit")


@dataclass
class ConsoleMailer:
    sent: list[tuple[str, str, str]] = field(default_factory=list)
    echo: bool = False

    def send(self, to: str, subject: str, body: str) -> None:
        self.sent.append((to, subject, body))
        if self.echo:
            print(f"  [E-MAIL → {to}] {subject}")
