"""Stockage pédagogique en mémoire : perdu au redémarrage du processus."""

from schemas import EtudiantEnregistre

etudiants: list[EtudiantEnregistre] = []
prochain_id: int = 1
