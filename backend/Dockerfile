FROM eclipse-temurin:21-jdk AS dev

WORKDIR /app

COPY .mvn .mvn
COPY mvnw pom.xml ./
RUN chmod +x mvnw && ./mvnw dependency:go-offline

COPY . .
RUN chmod +x docker-entrypoint.sh

EXPOSE 8080

CMD ["bash", "/app/docker-entrypoint.sh"]

FROM eclipse-temurin:21-jdk AS builder

WORKDIR /app

COPY .mvn .mvn
COPY mvnw pom.xml ./
RUN chmod +x mvnw && ./mvnw -B dependency:go-offline

COPY src src
RUN ./mvnw -B package -DskipTests

FROM eclipse-temurin:21-jre-alpine AS prod

RUN addgroup -S app && adduser -S app -G app \
    && apk add --no-cache bash

WORKDIR /app

COPY --from=builder --chown=app:app /app/target/*.jar app.jar
COPY --chown=app:app docker-entrypoint.sh ./docker-entrypoint.sh
RUN chmod +x docker-entrypoint.sh

USER app

EXPOSE 8080

ENTRYPOINT ["bash", "/app/docker-entrypoint.sh", "java", "-jar", "/app/app.jar"]
