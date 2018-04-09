git clone https://github.com/victor141516/caddyndex.git /path/to/caddyndex
docker run -d --rm --network caddy-network -v /path/to/caddyndex:/app -v /path/to/Caddyfile:/app/Caddyfile -w /app --name caddyndex python:alpine sh run.sh
