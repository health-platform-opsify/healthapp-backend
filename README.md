# healthapp-backend (Demo stack) — 2025-10-23

FastAPI service used in the demo environment. CI runs lint/tests/scans on every push/PR.
On merge to `main`, it builds and pushes an image to GHCR and (optionally) bumps the K8s env repo for Argo CD to deploy.


-- create schema (optional)
CREATE SCHEMA IF NOT EXISTS healthcare;

-- table
CREATE TABLE IF NOT EXISTS healthcare.patients (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    dob DATE,
    nhs_number TEXT,
    gender TEXT,
    ethnicity TEXT,
    phone TEXT,
    email TEXT,
    address TEXT,
    vitals JSONB,
    lab_results JSONB,
    comorbidities JSONB,
    medications JSONB,
    prior_admissions INTEGER,
    socioeconomic_status TEXT,
    last_visit TIMESTAMP WITH TIME ZONE,
    imaging JSONB,
    risk_scores JSONB,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now() NOT NULL
);

-- index on NHS number for fast lookups
CREATE INDEX IF NOT EXISTS idx_patients_nhs_number ON healthcare.patients (nhs_number);

-- trigger function to update updated_at timestamp on row updates
CREATE OR REPLACE FUNCTION healthcare.set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- trigger that uses the function
DROP TRIGGER IF EXISTS trg_set_updated_at ON healthcare.patients;
CREATE TRIGGER trg_set_updated_at
BEFORE UPDATE ON healthcare.patients
FOR EACH ROW
EXECUTE FUNCTION healthcare.set_updated_at();




git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/health-platform-opsify/healthapp-backend.git
git push -u origin main

- trigger PR CI


python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
uvicorn app.main:app --reload

git add .
git commit -m "feat(patients): basic CRUD endpoints and tests"
git checkout -m feature/patients
git push -u origin feature/patients