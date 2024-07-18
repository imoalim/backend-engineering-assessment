#!/bin/bash

# Quiz erstellen
echo "Erstelle ein Quiz"
curl -X POST http://127.0.0.1:8000/quiz/quizzes/ -H "Content-Type: application/json" -d '{"title": "Sample Quiz"}'

# Zeige alle Quizze
echo "Zeige alle Quizze"
curl -X GET http://127.0.0.1:8000/quiz/quizzes/

# Zeige den Fortschritt eines Quizzes
echo "Zeige den Fortschritt eines Quizzes"
curl -X GET http://127.0.0.1:8000/quiz/quizzes/1/progress/

# Einladung akzeptieren
echo "Akzeptiere eine Einladung"
curl -X POST http://127.0.0.1:8000/quiz/participants/1/accept_invitation/

# Quiz einreichen
echo "Reiche ein Quiz ein"
curl -X POST http://127.0.0.1:8000/quiz/participants/1/submit_quiz/

# Zeige alle Teilnahmen
echo "Zeige alle Teilnahmen"
curl -X GET http://127.0.0.1:8000/quiz/participants/
