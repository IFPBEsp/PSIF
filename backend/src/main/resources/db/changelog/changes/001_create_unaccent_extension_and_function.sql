--liquibase formatted sql

--changeset dario:001-create-unaccent-extension
CREATE EXTENSION IF NOT EXISTS unaccent;
--rollback DROP EXTENSION IF EXISTS unaccent;

--changeset dario:002-create-immutable-unaccent-function splitStatements:false
CREATE OR REPLACE FUNCTION immutable_unaccent(text)
  RETURNS text
  LANGUAGE sql
  IMMUTABLE PARALLEL SAFE STRICT
AS $$ SELECT public.unaccent('public.unaccent', $1) $$;
--rollback DROP FUNCTION IF EXISTS immutable_unaccent(text);
