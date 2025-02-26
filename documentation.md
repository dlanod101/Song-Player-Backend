# Spotify API

## Methods Required

### GET

- Get All Songs
  - ` BASE_URL/list/ `

  - ``` json
        Response
        
        200: [
            {
                "id": 1,
                "song image": "url",
                "song title": "str",
                "song artist": "str",
                "song is_liked": "bool",
                "song audio": "file"
            }, 
            ...
        ]
        404: {
            "message": "Song not found."
        }
        Other: {
            "message": "Encountered an error: {error}"
        }
    ```

- Get Specific Song
  - ` BASE_URL/get/{song_id} `

  - ``` json
        Response
        
        200: {
            "id": 1,
            "song image": "url",
            "song title": "str",
            "song artist": "str",
            "song is_liked": "bool",
            "song audio": "file"
        }
        404: {
            "message": "Song not found."
        }
        Other: {
            "message": "Encountered an error: {error}"
        }
    ```

### POST

- Add a Song
  - ` BASE_URL/create/ `

  - ``` json
        Request
        
        {
            "song image": "url",
            "song title": "str",
            "song artist": "str",
            "song is_liked": "bool",
            "song audio": "file"
        }

        Response
        200: {
            "message": "Song added"
        }
        400: {
            "message": "Song not added. Bad request"
        }
        Other: {
            "message": "Encountered an error: {error}"
        }
    ```

### PUT

- Update  a Song
  - ` BASE_URL/update/{song_id} `

  - ``` json
        Request
        
        {
            "song image": "url",
            "song title": "str",
            "song artist": "str",
            "song is_liked": "bool",
            "song audio": "file"
        }
        
        Response

        200: {
            "id": 1,
            "song image": "url",
            "song title": "str",
            "song artist": "str",
            "song is_liked": "bool",
            "song audio": "file"
        }
        400: {
            "message": "Song not added. Bad request"
        }
        Other: {
            "message": "Encountered an error: {error}"
        }
    ```

### DELETE

- Delete a Song
  - ` BASE_URL/delete/{song_id} `
  
    - ``` json
        Response

        200: {
            "message": "Song Deleted"
        }
        404: {
            "message": "Song not found."
        }
        Other: {
            "message": "Encountered an error: {error}"
        }
      ```

- Delete a list of Songs
  - `BASE_URL/songs/`

    - ``` json
        Request

        {
            "marked_songs": ["id", "id", "id"]
        }

        Response

        200: {
            "message": "Songs Deleted"
        }
        404: {
            "message": "Song not found."
        }
        Other: {
            "message": "Encountered an error: {error}"
        }
      ```

- Delete all Songs
  - `BASE_URL/all_songs/`

    - ``` json
        Response

        200: {
            "message": "All Songs have been Deleted"
        }
        404: {
            "message": "Song not found. Bad request"
        }
        Other: {
            "message": "Encountered an error: {error}"
        }
      ```
