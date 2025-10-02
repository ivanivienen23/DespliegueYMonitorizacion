-- db/init.sql
CREATE TABLE IF NOT EXISTS citas (
  id SERIAL PRIMARY KEY,
  paciente VARCHAR(100),
  fecha TIMESTAMP,
  motivo TEXT
);

INSERT INTO citas (paciente, fecha, motivo) VALUES
('Ana Pérez', '2025-10-10 09:00:00', 'Revisión'),
('Luis Gómez', '2025-10-11 10:30:00', 'Vacunación');
