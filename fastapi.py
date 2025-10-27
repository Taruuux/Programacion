
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr
from typing import Optional, List

app = FastAPI(title="Veterinarios API (memoria)")

# ===== Modelos =====
class VeterinarioBase(BaseModel):
    nombre: str
    colegiado_numero: str
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None
    especialidad: Optional[str] = None
    activo: bool = True

class VeterinarioCreate(VeterinarioBase):
    pass

class VeterinarioUpdate(VeterinarioBase):
    id: int

class VeterinarioRead(VeterinarioBase):
    id: int

# ===== Almacenamiento en memoria =====
DB = {}          # id -> dict
NEXT_ID = 1

# ===== Endpoints =====
@app.post("/veterinarios/create", response_model=VeterinarioRead)
def create_veterinario(payload: VeterinarioCreate):
    global NEXT_ID
    v = payload.model_dump()
    v["id"] = NEXT_ID
    DB[NEXT_ID] = v
    NEXT_ID += 1
    return v

@app.post("/veterinarios/update", response_model=VeterinarioRead)
def update_veterinario(payload: VeterinarioUpdate):
    if payload.id not in DB:
        raise HTTPException(status_code=404, detail="No existe")
    DB[payload.id] = payload.model_dump()
    return DB[payload.id]

@app.get("/veterinarios/all", response_model=List[VeterinarioRead])
def get_veterinarios():
    return list(DB.values())

@app.get("/veterinarios/v_id", response_model=VeterinarioRead)
def get_veterinario_by_id(v_id: int = Query(..., ge=1)):
    v = DB.get(v_id)
    if not v:
        raise HTTPException(status_code=404, detail="No existe")
    return v


