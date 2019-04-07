#!/bin/sh

while IFS='' read -r line
do
    name="$(echo $line | cut -d',' -f1)"
    duration="$(echo $line | cut -d',' -f2)"
    artist="$(echo $line | cut -d',' -f3)"
    album="$(echo $line | cut -d',' -f4)"
    genre="$(echo $line | cut -d',' -f5)"
    track_number="$(echo $line | cut -d',' -f6)"
    curl -X POST -H "Content-Type: application/json" -d "{
        \"name\": \"$name\",
        \"duration\": \"$duration\",
        \"artist\": \"$artist\",
        \"album\": \"$album\",
        \"genre\": \"$genre\",
        \"path\": \"waza\",
        \"track_number\": \"$track_number\"
}" http://localhost:8000/api/songs/
done < misc/song.txt
