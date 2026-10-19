-- Fills existing rows with 'web', then drops the default so new code must set it.
ALTER TABLE users ADD COLUMN signup_source text NOT NULL DEFAULT 'web';
ALTER TABLE users ALTER COLUMN signup_source DROP DEFAULT;
