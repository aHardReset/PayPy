# PayPy - Aplicación Bancaria Didáctica

Aplicación bancaria simple para aprender desarrollo full-stack con Python y React.

## Stack Tecnológico

**Backend:**
- Python con FastAPI
- SQLite (sin ORM)
- UV para gestión de dependencias

**Frontend:**
- React + TypeScript
- Vite
- Pico CSS
- Bun

## Requisitos Previos

### 1. Instalar UV (gestor de paquetes Python)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Instalar Bun (runtime JavaScript)
```bash
curl -fsSL https://bun.sh/install | bash
```

Después de instalar, reinicia tu terminal o ejecuta:
```bash
source ~/.zshrc  # o ~/.bashrc en Linux
```

## Configuración del Proyecto

### Backend

1. Navegar al directorio del backend:
```bash
cd backend
```

2. Instalar dependencias (UV creará automáticamente un entorno virtual):
```bash
uv sync
```

3. Inicializar la base de datos:
```bash
uv run python database.py
```

4. Iniciar el servidor:
```bash
uv run uvicorn main:app --reload
```

El backend estará disponible en: `http://localhost:8000`
- API docs: `http://localhost:8000/docs`

### Frontend

1. Navegar al directorio del frontend:
```bash
cd frontend
```

2. Instalar dependencias:
```bash
bun install
```

3. Iniciar el servidor de desarrollo:
```bash
bun run dev
```

El frontend estará disponible en: `http://localhost:5173`

## Estructura del Proyecto

```
paypy/
├── backend/
│   ├── main.py           # FastAPI app y endpoints
│   ├── database.py       # Configuración de DB y datos iniciales
│   ├── repository.py     # Funciones de utilidad para DB
│   └── pyproject.toml    # Dependencias Python
└── frontend/
    ├── src/
    │   ├── pages/        # Componentes de página
    │   ├── components/   # Componentes reutilizables
    │   └── App.tsx       # Componente principal
    └── package.json      # Dependencias Node
```

## Usuarios de Prueba

La base de datos viene pre-poblada con usuarios de prueba:

| Usuario | Contraseña | País |
|---------|-----------|------|
| johnd | password123 | Estados Unidos |
| janes | password456 | Estados Unidos |
| bobj | password789 | Canadá |
| alicew | passwordabc | Estados Unidos |
| carlosg | password321 | México |
| marial | password654 | México |

## Ejercicios para Estudiantes

### Ejercicio 1: Calcular Balance
**Archivo:** `backend/main.py` - función `get_user_info()`

Actualmente el balance siempre retorna 0. Debes:
1. Obtener todas las transacciones usando `repository.get_all_transactions_for_user(user_id)`
2. Sumar todos los montos (`amount`) de las transacciones
3. Actualizar el campo `balance` con el valor calculado

### Ejercicio 2: Mostrar Nombres en Transacciones
**Archivo:** `backend/main.py` - función `get_user_transactions()`

Actualmente retorna una lista vacía. Debes:
1. Descomentar la línea que obtiene las transacciones
2. Para cada transacción, obtener información del remitente y destinatario
3. Usar `repository.get_user_by_id()` para obtener los nicknames
4. Agregar campos `sender_nickname` y `recipient_nickname` a cada transacción
5. Manejar casos donde `sender_id` o `recipient_id` sean `None`

## API Endpoints

- `GET /api/users/{user_id}` - Obtener información del usuario y balance
- `GET /api/users/{user_id}/transactions` - Obtener transacciones del usuario

## Notas de Desarrollo

- El proyecto usa autenticación hardcodeada (user_id=1) por simplicidad didáctica
- La base de datos se crea automáticamente al iniciar el backend
- Hot reload está habilitado en ambos: backend (uvicorn) y frontend (Vite)

## Comandos Útiles

### Backend
```bash
# Instalar dependencias
uv sync

# Ejecutar la app
uv run uvicorn main:app --reload

# Recrear la base de datos
rm paypy.db && uv run python database.py
```

### Frontend
```bash
# Instalar dependencias
bun install

# Modo desarrollo
bun run dev

# Build para producción
bun run build
```

## Solución de Problemas

### "Command not found: uv" o "Command not found: bun"
Reinicia tu terminal o ejecuta `source ~/.zshrc` después de instalar.

### El frontend no se conecta al backend
Verifica que ambos servidores estén corriendo y en los puertos correctos:
- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173`

### Error de TypeScript en el frontend
Reinicia el servidor TypeScript en tu IDE o ejecuta:
```bash
cd frontend
bun install
```
