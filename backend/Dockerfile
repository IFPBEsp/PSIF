FROM eclipse-temurin:21-jdk

WORKDIR /app

COPY .mvn .mvn
COPY mvnw pom.xml ./
RUN chmod +x mvnw && ./mvnw dependency:go-offline

COPY . .
RUN chmod +x docker-entrypoint.sh

EXPOSE 8080

CMD ["bash", "/app/docker-entrypoint.sh"]
