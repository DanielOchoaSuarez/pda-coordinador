# pda-coordinador

flask --app ./src/coordinador/api run -p 3000

## Variables de entorno

Tomar el archivo .env.example y renombrarlo .env, luego se deben ajustar los valores de las variables de ambiente con la información adecuada al despliegue

## Ejecutar BFF + Sistema PDA

Para ejecutar la prueba de concepto final (Entrega 5) por medio de Docker es necesario realizar los siguientes pasos en el orden establecido:

1. Clonar los repositorios y crear las imagenes Docker:

   - [PDA Orquestador SAGA](https://github.com/DanielOchoaSuarez/pda-coordinador)

     - docker build . -t pda-orquestador-saga

   - [PDA BFF Web](https://github.com/cris10958/pda-bff-web)

     - docker build . -t pda-bff-web

   - [Servicio Catastro]()

     - docker build . -t pda-catastro

   - [Servicio Contractual]()

     - docker build . -t pda-contractual

   - [Servicio Auditoria](https://github.com/abenitezm20/PDA-Servicio-Auditoria)

     - docker build . -t pda-auditoria

2. Ejecutar el siguiente comando que permite levantar todas las aplicaciones necesarias:

```
docker-compose up -d
```

uvicorn src.bff_web.main:app --host localhost --port 8003 --reload
