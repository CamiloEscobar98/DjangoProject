# INFORMACIÓN: PRUEBA TÉCNICA PYTHON DJANGO REST FRAMEWORK

##  Instalación:
1. Construir la imágen de Docker.
```
docker build -t python-django-test .
```
2. Ejecutar el contenedor Docker.
```
docker run -p 8000:8000 docker-django-test
```
3. Abrir la aplicación en localhost:8000


## Rutas API:
- localhost:8000/api/get-token (POST) **Obtener el token necesario para poder acceder a los otros endpoints de la aplicación. Es necesario colocar el username y password del usuario. Este token será utilizado por medio de un Header Authorization con el valor "Token {token}"**
**Response**
```
HTTP 200 OK
Allow: POST
Content-Type: application/json
Vary: Accept

{
  "token": "a616c79fe450fb47d2b7400295bc56e0bf83c311"
}
```


- localhost:8000/api/vulnearbilities (GET) **Obtener las vulnerabilidades sumarizadas desde la API sin incluir las que ya están registradas.**
**Response**
```
HTTP 200 OK
Allow: GET
Content-Type: application/json
Vary: Accept

{
    "count": 218099,
    "results": [
        {
            "id": "CVE-1999-1122",
            "sourceIdentifier": "cve@mitre.org",
            "published": "1989-07-26T04:00:00.000",
            "lastModified": "2018-05-03T01:29:04.817",
            "descriptions": [
                {
                    "lang": "en",
                    "value": "Vulnerability in restore in SunOS 4.0.3 and earlier allows local users to gain privileges."
                }
            ],
            "status": "Modified"
        },
    ]
}
```

- localhost:8000/api/vulnearbilities (POST) **Registro de la vulnerabilidad fixeada. Solamente se requirede del código**
**Response**
```
HTTP 201 Created
Allow: POST
Content-Type: application/json
Vary: Accept

{
    "id": 4,
    "code": "CVE-2000-0564"
}
```

- localhost:8000/api/vulnearbilities/severity?severity=LOW (GET) **Obtener las vulnerabilidades sumarizadas desde la API segun su severidad, estas pueden ser, LOW, MEDIUM, HIGH**
**Response**
```
HTTP 200 OK
Allow: GET
Content-Type: application/json
Vary: Accept

{
    "count": 2426,
    "results": [
        {
            "id": "CVE-2010-1323",
            "sourceIdentifier": "cve@mitre.org",
            "published": "2010-12-02T16:22:20.847",
            "lastModified": "2020-01-21T15:46:02.220",
            "descriptions": [
                {
                    "lang": "en",
                    "value": "MIT Kerberos 5 (aka krb5) 1.3.x, 1.4.x, 1.5.x, 1.6.x, 1.7.x, and 1.8.x through 1.8.3 does not properly determine the acceptability of checksums, which might allow remote attackers to modify user-visible prompt text, modify a response to a Key Distribution Center (KDC), or forge a KRB-SAFE message via certain checksums that (1) are unkeyed or (2) use RC4 keys."
                },
                {
                    "lang": "es",
                    "value": "MIT Kerberos 5 (también conocido como krb5) v1.3.x, v1.4.x, v1.5.x, v1.6.x, v1.7.x, y v1.8.x hasta v1.8.3 no determina correctamente la aceptabilidad de las sumas de comprobación, lo que podría permitir a un atacante remoto modificar el user-visible prompt text, modificar una respuesta para el KDC (Key Distribution Center) o falsificar un mensaje KRB-SAFE mediante ciertas sumas de comprobación que (1) están sin clave o (2) usan claves RC4."
                }
            ],
            "status": "Modified"
        },
        {
            "id": "CVE-2010-1324",
            "sourceIdentifier": "cve@mitre.org",
            "published": "2010-12-02T16:22:20.880",
            "lastModified": "2020-01-21T15:46:02.220",
            "descriptions": [
                {
                    "lang": "en",
                    "value": "MIT Kerberos 5 (aka krb5) 1.7.x and 1.8.x through 1.8.3 does not properly determine the acceptability of checksums, which might allow remote attackers to forge GSS tokens, gain privileges, or have unspecified other impact via (1) an unkeyed checksum, (2) an unkeyed PAC checksum, or (3) a KrbFastArmoredReq checksum based on an RC4 key."
                },
                {
                    "lang": "es",
                    "value": "MIT Kerberos 5 (también conocido como krb5)  v1.7.x y v1.8.x hasta v1.8.3 no determina correctamente la aceptabilidad de las sumas de comprobación, lo que podría permitir a un atacante remoto falsificar GSS tokens, ganar privilegios, o tener otro impacto no especificado mediante (1) una suma de comprobación sin clave, (2) una suma de comprobación PAC sin clave o (3) una suma de comprobación KrbFastArmoredReq basada en una clave de RC4."
                }
            ],
            "status": "Modified"
        },
        {
            "id": "CVE-2014-4407",
            "sourceIdentifier": "product-security@apple.com",
            "published": "2014-09-18T10:55:09.923",
            "lastModified": "2019-03-08T16:06:31.107",
            "descriptions": [
                {
                    "lang": "en",
                    "value": "IOKit in Apple iOS before 8 and Apple TV before 7 does not properly initialize kernel memory, which allows attackers to obtain sensitive memory-content information via an application that makes crafted IOKit function calls."
                },
                {
                    "lang": "es",
                    "value": "IOKit en Apple iOS anterior a 8 y Apple TV anterior a 7 no inicializa debidamente la memoria de kernel, lo que permite a atacantes obtener información sensible de contenido de memoria a través de una aplicación que realiza llamadas manipuladas a funciones IOKit."
                }
            ],
            "status": "Modified"
        },
        {
            "id": "CVE-2014-3566",
            "sourceIdentifier": "secalert@redhat.com",
            "published": "2014-10-15T00:55:02.137",
            "lastModified": "2023-02-13T00:40:46.353",
            "descriptions": [
                {
                    "lang": "en",
                    "value": "The SSL protocol 3.0, as used in OpenSSL through 1.0.1i and other products, uses nondeterministic CBC padding, which makes it easier for man-in-the-middle attackers to obtain cleartext data via a padding-oracle attack, aka the \"POODLE\" issue."
                },
                {
                    "lang": "es",
                    "value": "El protocolo SSL 3.0, utilizado en OpenSSL hasta 1.0.1i y otros productos, utiliza relleno (padding) CBC no deterministico, lo que facilita a atacantes man-in-the-middle obtener datos en texto plano a través de un ataque de relleno (padding) oracle, también conocido como el problema 'POODLE'."
                }
            ],
            "status": "Modified"
        },
    ]
}
```