CREATE TABLE orders (
  id          serial PRIMARY KEY,
  user_id     integer NOT NULL REFERENCES users (id),
  total_cents integer NOT NULL,
  created_at  timestamptz NOT NULL DEFAULT now()
);
