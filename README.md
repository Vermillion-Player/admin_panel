# Vermillion Player - Panel de administración

Panel de administración para gestionar contenidos de Vermillion Player. 

## Tecnologías del proyecto

1. Django: template del panel Jazzmin.
2. PostgresSQL (pendiente - De momento utiliza SQLite)
3. Graphql
4. Autenticación JWT
5. Docker (pendiente)
6. Pytest (pendiente)

## ¿Que contenido gestiona este proyecto?

- Canales (crea canales personalizados para emitir diferente tipos de contenido)
- Programas (crea programas para emitirlos en diferentes canales)
- Temporadas (asocia estas temporadas a sus programas)
- Episodios (crea episodios vinculados a sus canales)
- Películas (crea películas para emitir)
- Videojuegos (proximamente)

NOTA: El contenido multimedia se guarda en un CDN y se asocia al contenido relacionado buscando por carpeta desde el panel (pendiente)


## Despliegue del proyecto (sin contenedores)

Para trabajar sin contenedores el proyecto hacemos lo siguiente en linux o utilizando la shell de Git:

1. Clonar o descargar proyecto en tu máquina: ``git clone https://github.com/Vermillion-Player/admin_panel.git``
2. Crear entorno virtual: ``python -m venv .env``
3. Arrancar entorno virtual: ``source .env/bin/activate``
4. Instalar dependencias: ``pip install -r requirements.txt``
5. Crear migraciones: ``python manage.py makemigrations``
6. Lanzar migraciones: ``python manage.py migrate``
7. Recolectar estáticos: ``python manage.py collectstatic``
8. Crear usuario admin: ``python manage.py createsuperuser``
9. Arrancar servidor: ``python manage.py runserver``

## Rutas de acceso

1. Panel: ``localhost:8000/admin``
2. Graphql: ``localhost:8000/graphql``


## Uso de Graphql

En este aparatdo explico como autenticar en graphql mediante jwt y las queries que se pueden ejecutar

### Autenticación

Para autenticarse utiliza la siguiente mutación:

```json
mutation {
  tokenAuth(username: "prueba", password: "prueba_pass") {
    token
    payload
  }
}
```

Esta te devolverá un token jwt que podrás utilizar en todas las queries. Para ello se hace la petición añadiendo el token al header de la petición con JWT seguido del token (no Bearer).

Para poder hacer la petición en el cliente interactivo de graphql abajo pulsa la pestaña Headers y añade el token del siguiente modo:

```json
{
  "Authorization": "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}

```

NOTA: Si estás usando el cliente interactivo de graphql, puedes ahorrarte este paso iniciando sesión en el panel. De ese modo podrás hacer las queries sin tener que añadir el token.


También dispone de dos mutaciones mas de apoyo:

1. Verificar token (valida si el token esta activo):

```json
mutation {
  verifyToken(token: "eyJ0eXAiOiJKV1QiLC...") {
    payload
  }
}
```

2. Refrescar token (renueva el token para que se pueda reutilizar mas tiempo):

```json
mutation {
  refreshToken(token: "eyJ0eXAiOiJKV1QiLC...") {
    token
    payload
  }
}
```

### Listado de Queries disponibles

#### Canales

1. Listado de canales:

```json
query{
  allChannels{
    id
    name
    description
    logo
    age
    mainCategory{
      id
      name
    }
    otherCategories{
      id
      name
    }
  }
}
```

2. Canal por id:

```json
query{
  channelById(id:1){
    id
    name
    description
    logo
    age
    mainCategory{
      id
      name
    }
    otherCategories{
      id
      name
    }
  }
}
```

#### Categorías

1. Listado de categorías:

```json
query{
  allCategories{
    id
    name
    description
    onlyAdult
    logo
  }
}
```

2. Categoría por id:

```json
query{
  categoryById(id:1){
    id
    name
    description
    onlyAdult
    logo
  }
}
```

#### Actores

1. Listado de actores:

```json
query{
  allActors{
    id
    name
    description
    image
    birthdate
    birthplace
    height
    weight
    genre
    onlyAdult
  }
}
```

2. Actor por id:

```json
query{
  actorById(id:1){
    id
    name
    description
    image
    birthdate
    birthplace
    height
    weight
    genre
    onlyAdult
  }
}
```

#### Películas

1. Listado de peliculas:

```json
query{
  allMovies{
    id
    name
    description
    image
    duration
    releaseDate
    onlyAdult
    cast{
      id
      name
      description
      image
      birthdate
      birthplace
      height
      weight
      genre
      onlyAdult
    }
    channel{
      id
      name
      description
      logo
      age
      mainCategory{
        id
        name
      }
      otherCategories{
        id
        name
      }
    }
  }
}
```

2. Película por id:

```json
query{
  movieById(id:1){
    id
    name
    description
    image
    duration
    releaseDate
    onlyAdult
    cast{
      id
      name
      description
      image
      birthdate
      birthplace
      height
      weight
      genre
      onlyAdult
    }
    channel{
      id
      name
      description
      logo
      age
      mainCategory{
        id
        name
      }
      otherCategories{
        id
        name
      }
    }
  }
}
```

#### Programas

1. Listado de programas:

```json
query{
  allPrograms{
    id
    name
    description
    image
    age
    mainCategory{
      id
      name
      description
      onlyAdult
      logo
    }
    otherCategories{
      id
      name
      description
      onlyAdult
      logo
    }
    actors{
      id
      name
      description
      image
      birthdate
      birthplace
      height
      weight
      genre
      onlyAdult
    }
    releaseDate
    channel{
      id
      name
      description
      logo
      age
      mainCategory{
        id
        name
      }
      otherCategories{
        id
        name
      }
    }
  }
}
```

2. Programa por id:

```json
query{
  programById(id:1){
    id
    name
    description
    image
    age
    mainCategory{
      id
      name
      description
      onlyAdult
      logo
    }
    otherCategories{
      id
      name
      description
      onlyAdult
      logo
    }
    actors{
      id
      name
      description
      image
      birthdate
      birthplace
      height
      weight
      genre
      onlyAdult
    }
    releaseDate
    channel{
      id
      name
      description
      logo
      age
      mainCategory{
        id
        name
      }
      otherCategories{
        id
        name
      }
    }
  }
}
```

#### Temporadas

1. Listado de temporadas:

```json
query{
  allSeasons{
    id
    name
    description
    image
    program{
      id
      name
      description
      image
      age
      mainCategory{
        id
        name
        description
        onlyAdult
        logo
      }
      otherCategories{
        id
        name
        description
        onlyAdult
        logo
      }
      actors{
        id
        name
        description
        image
        birthdate
        birthplace
        height
        weight
        genre
        onlyAdult
      }
      releaseDate
      channel{
        id
        name
        description
        logo
        age
        mainCategory{
          id
          name
        }
        otherCategories{
          id
          name
        }
      }
    }
    releaseDate
  }
}
```

2. Temporada por id:

```json
query{
  seasonById(id:1){
    id
    name
    description
    image
    program{
      id
      name
      description
      image
      age
      mainCategory{
        id
        name
        description
        onlyAdult
        logo
      }
      otherCategories{
        id
        name
        description
        onlyAdult
        logo
      }
      actors{
        id
        name
        description
        image
        birthdate
        birthplace
        height
        weight
        genre
        onlyAdult
      }
      releaseDate
      channel{
        id
        name
        description
        logo
        age
        mainCategory{
          id
          name
        }
        otherCategories{
          id
          name
        }
      }
    }
    releaseDate
  }
}
```

#### Episodios

1. Listado de episodios:

```json
query{
  allEpisodes{
    id
    name
    description
    image
    duration
    program{
      id
      name
      description
      image
      age
      mainCategory{
        id
        name
        description
        onlyAdult
        logo
      }
      otherCategories{
        id
        name
        description
        onlyAdult
        logo
      }
      actors{
        id
        name
        description
        image
        birthdate
        birthplace
        height
        weight
        genre
        onlyAdult
      }
      releaseDate
      channel{
        id
        name
        description
        logo
        age
        mainCategory{
          id
          name
        }
        otherCategories{
          id
          name
        }
      }
    }
    season{
      id
      name
      description
      image
      program{
        id
        name
        description
        image
        age
        mainCategory{
          id
          name
          description
          onlyAdult
          logo
        }
        otherCategories{
          id
          name
          description
          onlyAdult
          logo
        }
        actors{
          id
          name
          description
          image
          birthdate
          birthplace
          height
          weight
          genre
          onlyAdult
        }
        releaseDate
        channel{
          id
          name
          description
          logo
          age
          mainCategory{
            id
            name
          }
          otherCategories{
            id
            name
          }
        }
      }
      releaseDate
    }
    cast{
      id
      name
      description
      image
      birthdate
      birthplace
      height
      weight
      genre
      onlyAdult
    }
    releaseDate
  }
}
```

2. Episodio por id:

```json
query{
  episodesById(id:1){
    id
    name
    description
    image
    duration
    program{
      id
      name
      description
      image
      age
      mainCategory{
        id
        name
        description
        onlyAdult
        logo
      }
      otherCategories{
        id
        name
        description
        onlyAdult
        logo
      }
      actors{
        id
        name
        description
        image
        birthdate
        birthplace
        height
        weight
        genre
        onlyAdult
      }
      releaseDate
      channel{
        id
        name
        description
        logo
        age
        mainCategory{
          id
          name
        }
        otherCategories{
          id
          name
        }
      }
    }
    season{
      id
      name
      description
      image
      program{
        id
        name
        description
        image
        age
        mainCategory{
          id
          name
          description
          onlyAdult
          logo
        }
        otherCategories{
          id
          name
          description
          onlyAdult
          logo
        }
        actors{
          id
          name
          description
          image
          birthdate
          birthplace
          height
          weight
          genre
          onlyAdult
        }
        releaseDate
        channel{
          id
          name
          description
          logo
          age
          mainCategory{
            id
            name
          }
          otherCategories{
            id
            name
          }
        }
      }
      releaseDate
    }
    cast{
      id
      name
      description
      image
      birthdate
      birthplace
      height
      weight
      genre
      onlyAdult
    }
    releaseDate
  }
}
```


NOTA: Puedes elegir los campos que mostrar. Por ejemplo si del episodio no queremos tanta info podemos hacer una query mas sencilla:

```json
query{
  allEpisodes{
    id
    name
    description
  }
}
```